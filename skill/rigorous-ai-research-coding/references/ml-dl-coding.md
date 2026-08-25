# ML and Deep-Learning Coding

## Data boundary

- Define the unit of statistical independence: sample, subject, site, document, device, trajectory, or time block.
- Split before fitting preprocessing, feature selection, normalization, tokenization statistics, or imputation.
- Keep protected test data inaccessible to tuning code and record split manifests and hashes.
- Audit identifier, group, near-duplicate, fingerprint, and temporal overlap.

## Fair comparison

- Give methods comparable data access, tuning opportunity, compute budgets, stopping rules, and preprocessing.
- Preserve the full search history and selection rule; do not report only the winner.
- Prespecify the primary metric, meaningful-effect threshold, repetitions, and decision rule for confirmatory work.
- Report variation across relevant randomness sources, not only a favorable seed.

## Training and evaluation

- Record software versions, hardware-relevant settings, seeds, nondeterministic operations, and failed runs.
- Save checkpoints by a prespecified validation rule; never select by protected-test performance.
- Test metrics on hand-calculated examples, ties, empty classes, masks, and label ordering.
- Include calibration, subgroup, distribution-shift, and resource measures when the intended use requires them.
- State the achieved reproducibility level: repeatable in the same environment, reproducible in an independent environment, or not yet independently checked.

## Evidence basis

- Kapoor and Narayanan, *Leakage and the Reproducibility Crisis in Machine-Learning-Based Science*, Patterns, 2023.
- Pineau et al., *Improving Reproducibility in Machine Learning Research*, JMLR, 2021.
- Bouthillier et al., *Accounting for Variance in Machine Learning Benchmarks*, MLSys, 2021.
- Reimers and Gurevych, *Reporting Score Distributions Makes a Difference*, EMNLP, 2017.
- The REFORMS checklist, *Reporting Standards for Machine Learning Based Science*, Science Advances, 2024.
- PyTorch documentation, *Reproducibility*.
