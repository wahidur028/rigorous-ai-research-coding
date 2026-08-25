#!/usr/bin/env python3
"""Dependency-free tests for the bundled deterministic utilities."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "rigorous-ai-research-coding"
SCRIPTS = SKILL / "scripts"


def run(script: str, *arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(SCRIPTS / script), *arguments], capture_output=True, text=True, check=False)


class SkillScriptTests(unittest.TestCase):
    def test_manual_only_policy(self) -> None:
        content = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn("allow_implicit_invocation: false", content)
        self.assertIn("$rigorous-ai-research-coding", content)

    def test_valid_experiment_config_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = SKILL / "assets" / "experiment-config.template.json"
            data = json.loads(source.read_text(encoding="utf-8"))
            data["scientific_contract"]["sha256"] = "a" * 64
            path = Path(directory) / "config.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            result = run("validate_experiment_config.py", str(path))
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_invalid_confirmatory_config_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            data = json.loads((SKILL / "assets" / "experiment-config.template.json").read_text(encoding="utf-8"))
            data["scientific_contract"]["sha256"] = "a" * 64
            data["stage"] = "confirmatory"
            path = Path(directory) / "config.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            result = run("validate_experiment_config.py", str(path))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("protected_test", result.stdout)

    def test_malformed_data_config_fails_cleanly(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            data = json.loads((SKILL / "assets" / "experiment-config.template.json").read_text(encoding="utf-8"))
            data["scientific_contract"]["sha256"] = "a" * 64
            data["data"] = []
            path = Path(directory) / "config.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            result = run("validate_experiment_config.py", str(path))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("data must be an object", result.stdout)
            self.assertNotIn("Traceback", result.stderr)

    def test_split_overlap_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "split.csv"
            path.write_text("record_id,split,group_id\na,train,p1\nb,test,p1\n", encoding="utf-8")
            result = run("audit_data_splits.py", str(path), "--group-column", "group_id")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("multiple splits", result.stdout)

    def test_clean_split_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "split.csv"
            path.write_text("record_id,split,group_id,time\na,train,p1,1\nb,test,p2,2\n", encoding="utf-8")
            result = run("audit_data_splits.py", str(path), "--group-column", "group_id", "--time-column", "time")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_hash_manifest_is_created(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            artifact = root / "artifact.txt"
            artifact.write_text("evidence", encoding="utf-8")
            output = root / "manifest.json"
            result = run("hash_artifacts.py", str(artifact), "--output", str(output))
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            data = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(len(data["files"][0]["sha256"]), 64)

    def test_environment_excludes_environment_variables(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "environment.json"
            result = run("capture_environment.py", "--output", str(output), "--packages", "pip")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            data = json.loads(output.read_text(encoding="utf-8"))
            self.assertNotIn("environment_variables", data)
            self.assertIn("security_note", data)

    def test_verified_bundle_requires_checks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            data = json.loads((SKILL / "assets" / "result-bundle.template.json").read_text(encoding="utf-8"))
            data.update({"contract_hash": "a" * 64, "config_hash": "b" * 64, "code_commit": "abcdef1", "evidence_status": "VERIFIED"})
            path = Path(directory) / "bundle.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            result = run("validate_result_bundle.py", str(path))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("requires validation_checks", result.stdout)

    def test_exploratory_bundle_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            data = json.loads((SKILL / "assets" / "result-bundle.template.json").read_text(encoding="utf-8"))
            data.update({"contract_hash": "a" * 64, "config_hash": "b" * 64, "code_commit": "abcdef1", "evidence_status": "EXPLORATORY", "expected_seeds": []})
            path = Path(directory) / "bundle.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            result = run("validate_result_bundle.py", str(path))
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
