#!/usr/bin/env python3
"""Capture a non-secret, machine-readable research environment snapshot."""

from __future__ import annotations

import argparse
import importlib.metadata
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


def run_command(command: list[str]) -> tuple[int, str]:
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=15, check=False)
    except (OSError, subprocess.SubprocessError) as error:
        return 1, str(error)
    return result.returncode, result.stdout.strip()


def git_snapshot() -> dict:
    code, root = run_command(["git", "rev-parse", "--show-toplevel"])
    if code != 0:
        return {"available": False}
    _, commit = run_command(["git", "rev-parse", "HEAD"])
    _, status = run_command(["git", "status", "--porcelain"])
    return {"available": True, "root": root, "commit": commit, "dirty": bool(status)}


def gpu_snapshot() -> dict:
    if shutil.which("nvidia-smi") is None:
        return {"nvidia_smi_available": False}
    code, output = run_command([
        "nvidia-smi",
        "--query-gpu=name,uuid,driver_version,memory.total",
        "--format=csv,noheader,nounits",
    ])
    if code != 0:
        return {"nvidia_smi_available": True, "query_succeeded": False, "error": output}
    devices = []
    for row in output.splitlines():
        fields = [field.strip() for field in row.split(",")]
        if len(fields) == 4:
            devices.append({"name": fields[0], "uuid": fields[1], "driver_version": fields[2], "memory_mib": fields[3]})
    return {"nvidia_smi_available": True, "query_succeeded": True, "devices": devices}


def package_snapshot(selected: list[str] | None) -> dict[str, str]:
    installed = {dist.metadata.get("Name", dist.metadata["Name"]): dist.version for dist in importlib.metadata.distributions()}
    if not selected:
        return dict(sorted(installed.items(), key=lambda item: item[0].lower()))
    normalized = {name.lower(): (name, version) for name, version in installed.items()}
    result: dict[str, str] = {}
    for requested in selected:
        match = normalized.get(requested.lower())
        result[requested] = match[1] if match else "NOT_INSTALLED"
    return result


def atomic_json_write(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")
        temporary = Path(handle.name)
    os.replace(temporary, path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("environment.json"))
    parser.add_argument("--packages", nargs="*", help="Capture only these installed package versions; omit for all")
    args = parser.parse_args()

    payload = {
        "captured_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": {"version": sys.version, "implementation": platform.python_implementation(), "executable": sys.executable},
        "platform": {"system": platform.system(), "release": platform.release(), "machine": platform.machine(), "processor": platform.processor()},
        "git": git_snapshot(),
        "gpu": gpu_snapshot(),
        "packages": package_snapshot(args.packages),
        "security_note": "Environment variables and credentials are intentionally excluded.",
    }
    try:
        atomic_json_write(args.output, payload)
    except OSError as error:
        print(json.dumps({"status": "FAIL", "errors": [str(error)]}, sort_keys=True))
        return 1
    print(json.dumps({"status": "PASS", "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
