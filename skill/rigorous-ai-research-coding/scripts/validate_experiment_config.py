#!/usr/bin/env python3
"""Validate the minimum structure of a research experiment configuration."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


REQUIRED = {"project_id", "task_domain", "scientific_contract", "data", "experiment", "reproducibility", "outputs"}
DOMAINS = {"scientific-python", "ml", "dl", "genai", "time-series", "rl", "hybrid"}
HEX64 = re.compile(r"^[0-9a-fA-F]{64}$")


def load_document(path: Path) -> dict[str, Any]:
    if path.suffix.lower() == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
    elif path.suffix.lower() in {".yaml", ".yml"}:
        try:
            import yaml  # type: ignore
        except ImportError as error:
            raise ValueError("YAML input requires PyYAML; use JSON or install PyYAML") from error
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    else:
        raise ValueError("Configuration must be JSON, YAML, or YML")
    if not isinstance(data, dict):
        raise ValueError("Configuration root must be an object")
    return data


def validate(config: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    missing = sorted(REQUIRED - config.keys())
    if missing:
        errors.append(f"Missing top-level keys: {', '.join(missing)}")
    if config.get("task_domain") not in DOMAINS:
        errors.append(f"task_domain must be one of: {', '.join(sorted(DOMAINS))}")

    contract = config.get("scientific_contract")
    if not isinstance(contract, dict):
        errors.append("scientific_contract must be an object")
    else:
        contract_hash = contract.get("sha256")
        if contract_hash and not HEX64.fullmatch(str(contract_hash)):
            errors.append("scientific_contract.sha256 must contain 64 hexadecimal digits")

    reproducibility = config.get("reproducibility")
    if not isinstance(reproducibility, dict):
        errors.append("reproducibility must be an object")
    else:
        seeds = reproducibility.get("seeds")
        if not isinstance(seeds, list) or not seeds or not all(isinstance(seed, int) and not isinstance(seed, bool) for seed in seeds):
            errors.append("reproducibility.seeds must be a non-empty list of integers")
        elif len(seeds) != len(set(seeds)):
            errors.append("reproducibility.seeds must be unique")

    data = config.get("data")
    if not isinstance(data, dict):
        errors.append("data must be an object")
        data = {}
    experiment = config.get("experiment")
    if not isinstance(experiment, dict):
        errors.append("experiment must be an object")
        experiment = {}
    if not isinstance(config.get("outputs"), dict):
        errors.append("outputs must be an object")

    stage = str(config.get("stage", "exploratory")).lower()
    if stage not in {"exploratory", "confirmatory"}:
        errors.append("stage must be exploratory or confirmatory")
    if stage == "confirmatory":
        if data.get("protected_test") is not True:
            errors.append("confirmatory configuration requires data.protected_test=true")
        if not config.get("frozen_at"):
            errors.append("confirmatory configuration requires frozen_at")
        if not experiment.get("primary_metric"):
            errors.append("confirmatory configuration requires experiment.primary_metric")
        if not experiment.get("decision_rules"):
            errors.append("confirmatory configuration requires experiment.decision_rules")
    elif data.get("protected_test") is True:
        warnings.append("Exploratory stage declares protected_test=true; verify that development cannot access it")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path)
    args = parser.parse_args()
    try:
        errors, warnings = validate(load_document(args.config))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        errors, warnings = [str(error)], []
    payload = {"status": "PASS" if not errors else "FAIL", "errors": errors, "warnings": warnings}
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
