# Result Reporting and Error Learning

## Evidence status

- `UNVERIFIED`: supplied or generated information has not been checked against artifacts.
- `EXPLORATORY`: valid development evidence that may have influenced selection.
- `VERIFIED`: directly supported by inspected artifacts and validation checks.
- `CONFIRMATORY`: produced under a frozen protocol on protected evidence with prespecified decision rules.
- `BLOCKED`: a necessary artifact, authority, or validation step is unavailable.

## Result report

Record:

- research-contract identifier and hash;
- code commit, resolved configuration, environment, data and artifact hashes;
- every run, seed, failure, exclusion, retry, and protocol deviation;
- primary and secondary metrics with uncertainty where appropriate;
- comparison conditions and resource use;
- evidence status, limitations, and next decisive step.

Separate direct observations from derived summaries and scientific interpretation.

## Verified error-learning record

Capture:

- symptom and impact;
- minimal reproducer and evidence location;
- root cause and contributing conditions;
- why existing checks missed it;
- fix and regression test;
- verification outcome and residual risk;
- reusable prevention rule and scope.

Do not record speculation as a durable lesson. A failing test should fail for the intended reason before the fix and pass after it.

## Memory discipline

Update long-term research memory only when evidence is verified or a human explicitly approves the statement. Keep synthetic exercises, hypothetical values, and unresolved user claims out of project evidence.

## Evidence basis

- National Academies, *Reproducibility and Replicability in Science*, 2019.
- Sandve et al., *Ten Simple Rules for Reproducible Computational Research*, 2013.
- Peng, *Reproducible Research in Computational Science*, Science, 2011.
- Feathers, *Working Effectively with Legacy Code*, 2004.
