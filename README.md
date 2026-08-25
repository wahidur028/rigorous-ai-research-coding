# Rigorous AI Research Coding

An evidence-first, manually invoked ChatGPT/Codex skill for trustworthy Python research engineering across machine learning, deep learning, generative AI, time-series analysis, and reinforcement learning.

The skill helps an AI agent implement, review, debug, test, profile, reproduce, and package research code without silently changing the approved scientific design. It is a discipline layer, not a guarantee that code or conclusions are correct.

## Why this exists

Research code can execute successfully while leaking protected data, mistranslating equations, hiding failed runs, selecting favorable seeds, or overstating exploratory results. This skill makes the agent explicitly manage computational contracts, scientific invariants, provenance, test boundaries, uncertainty, and verified error learning.

## Activation and shared-account safety

The skill is intentionally manual-only:

```yaml
policy:
  allow_implicit_invocation: false
```

It should run only when a user explicitly selects it or writes:

```text
Use $rigorous-ai-research-coding to implement and validate this research code.
```

Uploading or installing it does not authorize automatic use in unrelated chats. Other users on a shared account can see or choose the skill if the installation is shared, but it is not supposed to trigger implicitly.

## Scientific boundary

This skill owns implementation and computational validation. It does **not** independently change research questions, hypotheses, datasets or splits, baselines, primary metrics, statistical plans, decision rules, or scientific conclusions.

When one of those decisions must change, invoke `$rigorous-ml-research` separately or provide an approved research contract. This boundary prevents a coding agent from redesigning the study as an invisible side effect of implementation.

## Coverage

- Python scientific software and numerical validation
- ML/DL data boundaries, reproducibility, fair comparison, and seed handling
- Generative-AI provenance, prompt search, LLM judges, RAG, and agent controls
- Time-series information clocks, rolling evaluation, leakage, and backtests
- RL termination semantics, environment versioning, multiple seeds, and offline-RL support
- Statistical comparison, multiplicity, selection bias, and evidence status
- Reproducible result bundles and a verified error-learning loop

## Repository layout

```text
skill/rigorous-ai-research-coding/
├── SKILL.md
├── agents/openai.yaml
├── assets/
├── references/
└── scripts/
docs/
evals/
tests/
.github/workflows/validate.yml
```

## Install or upload

Download the release asset named `Rigorous_AI_Research_Coding_Skill_v0.1.0-beta.zip`. Upload that ZIP to the skill/plugin area without extracting it if the interface accepts skill archives. If the interface requires a directory, extract it and upload the single `rigorous-ai-research-coding` folder.

Do not place the GitHub repository ZIP in the skill installer; it contains documentation, tests, and repository metadata in addition to the installable skill.

## Use it

Examples:

```text
Use $rigorous-ai-research-coding to audit this training pipeline for leakage and reproducibility risks. Do not change the scientific design.
```

```text
Use $rigorous-ai-research-coding to implement this approved equation, add reference tests, and report numerical limitations.
```

```text
Use $rigorous-ai-research-coding with the attached research contract to run the experiment and create a validated result bundle.
```

Do not invoke the skill for a request that is only about choosing a research question or claiming novelty; use a scientific-research workflow first.

## Deterministic utilities

The skill includes standard-library Python tools to:

- validate experiment configuration;
- audit data splits for identifier, group, fingerprint, and temporal overlap;
- capture a non-secret environment snapshot;
- hash artifacts with SHA-256;
- validate result-bundle structure and evidence-status consistency.

These utilities detect specified structural problems. They cannot prove absence of leakage, correctness of an implementation, or validity of a scientific conclusion.

## Validation status

Version `0.1.0-beta` has structural validation, Python compilation, command-line smoke tests, positive and negative unit tests, archive inspection, and manual-only activation checks. It has not yet completed independent forward-agent evaluation across real research repositories. Therefore it is a beta, not a validated `1.0.0` release.

See [VALIDATION_REPORT.md](VALIDATION_REPORT.md) and [evals/behavior_cases.md](evals/behavior_cases.md).

The expected checksum of the installable release ZIP is recorded in [RELEASE_ASSET_SHA256.txt](RELEASE_ASSET_SHA256.txt).

## Evidence basis

The design is grounded in published work on scientific computing, reproducibility, numerical validation, ML reporting, generative-AI evaluation, forecasting, reinforcement learning, and statistical interpretation. See [docs/SCIENTIFIC_EVIDENCE_BASIS.md](docs/SCIENTIFIC_EVIDENCE_BASIS.md).

## Limitations

- A skill can guide behavior but cannot guarantee that an agent reads every artifact or that underlying tools behave deterministically.
- Structural validators cannot replace domain expertise, code review, protected evaluation, statistical review, or independent replication.
- Closed generative-AI services may change without exposing a stable version.
- Manual-only activation is a behavioral policy, not per-user access control on a shared account.

## Contributing and citation

See [CONTRIBUTING.md](CONTRIBUTING.md). Citation metadata is provided in [CITATION.cff](CITATION.cff).

## License

MIT License. See [LICENSE](LICENSE).
