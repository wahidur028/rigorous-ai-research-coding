#!/usr/bin/env python3
"""Create a deterministic SHA-256 manifest for files and directories."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def collect_files(inputs: list[Path], output: Path) -> list[Path]:
    files: set[Path] = set()
    output_resolved = output.resolve()
    for item in inputs:
        if not item.exists():
            raise FileNotFoundError(f"Missing input: {item}")
        if item.is_file():
            candidates = [item]
        else:
            candidates = [path for path in item.rglob("*") if path.is_file()]
        for candidate in candidates:
            if candidate.resolve() != output_resolved:
                files.add(candidate.resolve())
    return sorted(files, key=lambda path: str(path))


def atomic_json_write(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")
        temporary = Path(handle.name)
    os.replace(temporary, path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="Files or directories to hash")
    parser.add_argument("--output", type=Path, default=Path("artifact-manifest.json"))
    args = parser.parse_args()

    try:
        files = collect_files(args.paths, args.output)
        entries = [
            {"path": str(path), "size_bytes": path.stat().st_size, "sha256": sha256_file(path)}
            for path in files
        ]
        payload = {
            "algorithm": "sha256",
            "created_at_utc": datetime.now(timezone.utc).isoformat(),
            "files": entries,
        }
        atomic_json_write(args.output, payload)
    except (OSError, ValueError) as error:
        print(json.dumps({"status": "FAIL", "errors": [str(error)]}, sort_keys=True))
        return 1

    print(json.dumps({"status": "PASS", "file_count": len(entries), "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
