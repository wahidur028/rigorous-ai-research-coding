---
name: rigorous-ai-research-coding
description: Evidence-first Python research engineering for implementing, reviewing, debugging, testing, optimizing, and reproducing scientific code in machine learning, deep learning, generative AI, time-series analysis, and reinforcement learning. Use only when the user explicitly invokes $rigorous-ai-research-coding or @rigorous-ai-research-coding. Do not invoke implicitly for ordinary coding or research requests.
---

# Rigorous AI Research Coding

Build trustworthy Python research software while preserving the approved scientific design. Treat code, data, configurations, logs, and results as evidence-bearing artifacts rather than mere implementation details.

## Establish the boundary

Proceed independently for implementation, refactoring, debugging, profiling, code review, data-pipeline construction, split audits, configuration, testing, reproducibility capture, experiment execution, and result packaging.

Stop and ask the user to invoke `$rigorous-ml-research`, or provide an approved research contract, before changing any of these:

- research question, hypothesis, or intended claim;
- target population, causal interpretation, or scope of generalization;
- dataset inclusion criteria or train/validation/test allocation;
- baselines, primary metrics, estimands, statistical plan, or decision rules;
- scientific interpretation or conclusion.

Do not block a small coding task merely because no research contract exists. State the boundary and avoid making scientific decisions implicitly.

## Inspect before editing

1. Read repository instructions, relevant source, configuration, tests, entry points, and existing result formats.
2. Identify the scientific invariant the code is meant to preserve.
3. Reconcile conflicts among prose, equations, configuration, code, and tests. Report unresolved conflicts.
4. Mark missing information as `UNKNOWN`; never fabricate a value or result.
5. Reproduce current behavior when practical before modifying it.

Use these evidence labels when they materially clarify status: `DIRECT OBSERVATION`, `USER-REPORTED`, `DERIVED`, `EXTERNAL EVIDENCE`, `ASSUMPTION`, `HYPOTHESIS`, and `UNKNOWN`.

## Build a computational contract

Before consequential implementation, make the following explicit:

- input/output schemas, tensor shapes, axes, units, dtypes, devices, and missing-value rules;
- time semantics, indexing conventions, masks, boundary behavior, and ordering constraints;
- stochastic components, random-number generators, seeds, and acceptable nondeterminism;
- data splits, protected evaluation data, fitting boundaries, and contamination controls;
- baseline behavior, metrics, estimands, resource budgets, tolerances, and failure policy.

Record the contract in configuration or adapt `assets/research-contract.template.json`.

## Implement and validate

1. Preserve a runnable reference behavior or characterization test.
2. Make the smallest complete change that satisfies the contract.
3. Enforce critical invariants with explicit validation and exceptions. Do not rely on Python `assert` for production or scientific correctness checks because optimized execution can remove assertions.
4. Test in layers: unit, property/metamorphic, integration, end-to-end smoke, regression, and scientific acceptance as appropriate.
5. Compare optimized or vectorized code against a simple trusted reference on edge cases and randomized small cases.
6. Capture provenance: code revision, resolved configuration, data/artifact hashes, environment, seeds, hardware-relevant details, and failures.
7. Produce a result bundle that distinguishes observed outputs from interpretation and records protocol deviations.

Use the deterministic utilities in `scripts/` when applicable. Run each utility with `--help` before first use.

## Load only the relevant domain guidance

- General Python and software practices: `references/python-scientific-coding.md`
- Equations, tensors, numerical methods, or tolerances: `references/mathematical-numerical-validation.md`
- ML or deep-learning experiments: `references/ml-dl-coding.md`
- LLMs, generative AI, RAG, agents, or LLM judges: `references/generative-ai-coding.md`
- Forecasting, temporal data, or backtesting: `references/time-series-coding.md`
- Reinforcement or offline reinforcement learning: `references/reinforcement-learning-coding.md`
- Statistical comparisons or uncertainty: `references/statistics-and-comparison.md`
- Result claims, failures, or reusable lessons: `references/result-reporting-and-error-learning.md`

## Use the bundled utilities

- Validate a resolved experiment configuration with `scripts/validate_experiment_config.py`.
- Audit split identifiers, groups, fingerprints, and temporal ordering with `scripts/audit_data_splits.py`.
- Capture a non-secret environment snapshot with `scripts/capture_environment.py`.
- Create SHA-256 manifests with `scripts/hash_artifacts.py`.
- Validate the structure and evidence status of a result bundle with `scripts/validate_result_bundle.py`.

These checks support review; they do not prove scientific validity.

## Report completion

Return a compact report with:

- `IMPLEMENTED`: files and behavior changed;
- `SCIENTIFIC INVARIANTS`: what was preserved or enforced;
- `VALIDATION`: commands run and exact outcomes;
- `EVIDENCE STATUS`: exploratory, verified, confirmatory, blocked, or unverified;
- `LIMITATIONS`: missing checks, nondeterminism, or unresolved risks;
- `NEXT DECISIVE STEP`: the smallest action that most reduces uncertainty.

Never imply a test ran when it did not. Never call an exploratory result confirmatory.

## Learn from verified errors

After a consequential failure:

1. Preserve the failing input, command, configuration, traceback, and environment.
2. Minimize the reproducer without changing the failure mechanism.
3. Separate symptom, root cause, contributing conditions, and detection gap.
4. Add the smallest durable regression or invariant check.
5. Verify the fix and relevant non-regression behavior.
6. Record a reusable lesson using `assets/error-learning-record.template.md` only when supported by evidence.

Reserve the term *active learning* for methods that choose observations to label. Call this process the *verified error-learning loop*. Update long-term research memory only with verified or explicitly human-approved lessons.

## Prohibited behavior

- Do not fabricate evidence, citations, metrics, seeds, hardware, or execution results.
- Do not use protected test data for model, prompt, checkpoint, threshold, or hyperparameter selection.
- Do not report the best seed, prompt, checkpoint, or subset as if it were prespecified.
- Do not choose a statistical procedure merely because a preliminary test or observed p-value is favorable.
- Do not silently catch failures, silently drop records, or silently change scientific defaults.
- Do not overwrite raw data or irreplaceable outputs.
- Do not capture secrets, tokens, credentials, or unrestricted environment variables in artifacts.
- Do not convert association into causation or empirical performance into a universal guarantee.
- Do not write synthetic tests or hypothetical results into project research memory.
