#!/usr/bin/env python3
"""Validate structure and internal evidence-status consistency of a result bundle."""

from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path
from typing import Any


REQUIRED = {"project_id", "contract_hash", "code_commit", "config_hash", "dataset_hashes", "environment", "runs", "failed_runs", "validation_checks", "protocol_deviations", "evidence_status"}
STATUSES = {"UNVERIFIED", "EXPLORATORY", "VERIFIED", "CONFIRMATORY", "BLOCKED"}
HEX64 = re.compile(r"^[0-9a-fA-F]{64}$")
GIT_HASH = re.compile(r"^[0-9a-fA-F]{7,64}$")


def validate(bundle: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    missing = sorted(REQUIRED - bundle.keys())
    if missing:
        errors.append(f"Missing top-level keys: {', '.join(missing)}")
    for name in ("contract_hash", "config_hash"):
        if not HEX64.fullmatch(str(bundle.get(name, ""))):
            errors.append(f"{name} must contain 64 hexadecimal digits")
    if not GIT_HASH.fullmatch(str(bundle.get("code_commit", ""))):
        errors.append("code_commit must contain 7 to 64 hexadecimal digits")
    if bundle.get("evidence_status") not in STATUSES:
        errors.append(f"evidence_status must be one of: {', '.join(sorted(STATUSES))}")

    runs = bundle.get("runs")
    if not isinstance(runs, list):
        errors.append("runs must be a list")
        runs = []
    run_ids: set[str] = set()
    observed_seeds: list[int] = []
    for index, run in enumerate(runs):
        if not isinstance(run, dict):
            errors.append(f"runs[{index}] must be an object")
            continue
        run_id = str(run.get("run_id", ""))
        if not run_id:
            errors.append(f"runs[{index}].run_id is required")
        elif run_id in run_ids:
            errors.append(f"Duplicate run_id: {run_id}")
        run_ids.add(run_id)
        seed = run.get("seed")
        if not isinstance(seed, int) or isinstance(seed, bool):
            errors.append(f"runs[{index}].seed must be an integer")
        else:
            observed_seeds.append(seed)
        if run.get("status") != "completed":
            errors.append(f"runs[{index}].status must be completed; failed runs belong in failed_runs")
        metrics = run.get("metrics")
        if not isinstance(metrics, dict) or not metrics:
            errors.append(f"runs[{index}].metrics must be a non-empty object")
        else:
            for metric, value in metrics.items():
                if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(float(value)):
                    errors.append(f"runs[{index}].metrics.{metric} must be a finite number")

    expected = bundle.get("expected_seeds")
    if expected is not None:
        if not isinstance(expected, list) or not all(isinstance(seed, int) and not isinstance(seed, bool) for seed in expected):
            errors.append("expected_seeds must be a list of integers")
        elif sorted(expected) != sorted(observed_seeds):
            warnings.append("Observed completed-run seeds do not match expected_seeds")

    checks = bundle.get("validation_checks")
    deviations = bundle.get("protocol_deviations")
    status = bundle.get("evidence_status")
    if status in {"VERIFIED", "CONFIRMATORY"}:
        if not isinstance(checks, list) or not checks:
            errors.append(f"{status} evidence requires validation_checks")
        elif any(not isinstance(check, dict) or check.get("status") != "PASS" for check in checks):
            errors.append(f"{status} evidence cannot contain unresolved validation checks")
        if not isinstance(deviations, list):
            errors.append("protocol_deviations must be a list")
        elif any(not isinstance(item, dict) or item.get("resolved") is not True for item in deviations):
            errors.append(f"{status} evidence cannot contain unresolved protocol deviations")
    if status == "CONFIRMATORY" and bundle.get("failed_runs"):
        warnings.append("Confirmatory bundle includes failed runs; explain prespecified handling")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.bundle.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("Bundle root must be an object")
        errors, warnings = validate(data)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        errors, warnings = [str(error)], []
    payload = {"status": "PASS" if not errors else "FAIL", "errors": errors, "warnings": warnings}
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
