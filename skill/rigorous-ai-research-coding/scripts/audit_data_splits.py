#!/usr/bin/env python3
"""Audit CSV data splits for identifier, group, fingerprint, and time leakage."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path


def parse_time(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        normalized = value.replace("Z", "+00:00")
        return datetime.fromisoformat(normalized).timestamp()


def overlaps(rows: list[dict[str, str]], column: str) -> list[dict[str, object]]:
    mapping: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        value = row.get(column, "").strip()
        if value:
            mapping[value].add(row["split"].strip())
    return [
        {column: value, "splits": sorted(splits)}
        for value, splits in sorted(mapping.items())
        if len(splits) > 1
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--group-column")
    parser.add_argument("--fingerprint-column")
    parser.add_argument("--time-column")
    parser.add_argument("--past-splits", nargs="+", default=["train"])
    parser.add_argument("--future-splits", nargs="+", default=["val", "validation", "test"])
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    details: dict[str, object] = {}
    try:
        with args.manifest.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            fields = reader.fieldnames or []
            required = {"record_id", "split"}
            missing = sorted(required - set(fields))
            if missing:
                raise ValueError(f"Missing required columns: {', '.join(missing)}")
            for optional in (args.group_column, args.fingerprint_column, args.time_column):
                if optional and optional not in fields:
                    raise ValueError(f"Requested column is absent: {optional}")
            rows = list(reader)
    except (OSError, ValueError, csv.Error) as error:
        print(json.dumps({"status": "FAIL", "errors": [str(error)], "warnings": []}, indent=2, sort_keys=True))
        return 1

    if not rows:
        errors.append("Manifest has no data rows")
    empty_core = [index + 2 for index, row in enumerate(rows) if not row["record_id"].strip() or not row["split"].strip()]
    if empty_core:
        errors.append(f"Rows with empty record_id or split: {empty_core[:20]}")

    for column, label in [("record_id", "record identifier"), (args.group_column, "group"), (args.fingerprint_column, "fingerprint")]:
        if not column:
            continue
        found = overlaps(rows, column)
        details[f"{column}_overlap"] = found
        if found:
            errors.append(f"{len(found)} {label} value(s) occur across multiple splits")

    if args.time_column:
        parsed: list[tuple[str, float]] = []
        for index, row in enumerate(rows):
            raw = row[args.time_column].strip()
            if not raw:
                warnings.append(f"Empty {args.time_column} at CSV row {index + 2}")
                continue
            try:
                parsed.append((row["split"].strip(), parse_time(raw)))
            except ValueError:
                errors.append(f"Unparseable {args.time_column} at CSV row {index + 2}: {raw}")
        past = [value for split, value in parsed if split in set(args.past_splits)]
        future = [value for split, value in parsed if split in set(args.future_splits)]
        if past and future:
            details["temporal_boundary"] = {"latest_past": max(past), "earliest_future": min(future)}
            if max(past) >= min(future):
                errors.append("Temporal ordering violation: a past-split time is not earlier than every future-split time")
        else:
            warnings.append("Temporal audit lacked rows in either past or future split sets")

    split_counts: dict[str, int] = defaultdict(int)
    for row in rows:
        split_counts[row["split"].strip()] += 1
    details["row_count"] = len(rows)
    details["split_counts"] = dict(sorted(split_counts.items()))
    payload = {"status": "PASS" if not errors else "FAIL", "errors": errors, "warnings": warnings, "details": details}
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
