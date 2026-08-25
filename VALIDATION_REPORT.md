# Validation Report

## Release candidate

- Skill: `rigorous-ai-research-coding`
- Version: `0.1.0-beta`
- Validation date: 2026-08-25
- Evidence status: `VERIFIED` for the checks listed below; `NOT TESTED` for independent forward-agent behavior across real repositories.

## Checks performed

| Check | Outcome |
|---|---|
| Skill frontmatter and directory structure via the skill-creator validator | PASS |
| Python compilation for all five bundled scripts | PASS |
| `--help` smoke test for every bundled script | PASS |
| Dependency-free deterministic test suite under normal Python | 10/10 PASS |
| Same deterministic test suite under optimized Python (`python -O`) | 10/10 PASS |
| Manual-only policy (`allow_implicit_invocation: false`) | PASS |
| Default prompt contains explicit `$rigorous-ai-research-coding` invocation | PASS |
| Positive experiment-configuration validation | PASS |
| Invalid confirmatory configuration rejection | PASS |
| Malformed configuration rejection without traceback | PASS |
| Clean group and chronological split audit | PASS |
| Deliberate cross-split group leakage detection | PASS |
| SHA-256 artifact-manifest creation | PASS |
| Environment capture excludes unrestricted environment variables | PASS |
| Exploratory result-bundle validation | PASS |
| Unsupported verified status without validation checks is rejected | PASS |
| ZIP integrity and expected top-level directory inspection | PASS |

## What these checks establish

They establish that the packaged skill has valid structure, explicit manual-only activation metadata, executable standard-library utilities, and expected behavior on the included positive and negative test fixtures.

## What they do not establish

- They do not prove that every future agent response will obey the skill.
- They do not prove scientific validity, absence of leakage, numerical correctness, or reproducibility of an external project.
- They do not constitute independent replication.
- The behavioral cases in `evals/behavior_cases.md` have not yet been executed repeatedly across representative real repositories.

## Release decision

`RELEASE AS BETA`

Do not label this version `1.0.0` until the safety-critical behavioral cases pass across repeated fresh sessions and at least two representative research repositories, with failures and reviewer judgments retained.
