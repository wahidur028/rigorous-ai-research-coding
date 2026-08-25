# Scientific Evidence Basis for a Rigorous AI Research Coding Skill

**Status:** design-basis review, not yet the final skill  
**Scope:** Python-based scientific coding for machine learning, deep learning, generative AI, time-series analysis, and reinforcement learning  
**Review date:** 2026-08-25

## Executive conclusion

The Scientific Coding Skill repository is a useful starting point, but it should not be copied as the scientific authority for a new ChatGPT skill. Its central direction—understand the experiment, make assumptions explicit, protect data, validate results, and prefer correctness over speed—is consistent with established research-software and reproducibility literature. Several of its absolute rules, examples, and omissions are not.

The evidence supports a new skill built on five layers:

1. **Scientific contract before implementation:** define the claim, estimand or objective, data-generating process, evaluation unit, assumptions, success criterion, and evidence boundary.
2. **Correct and inspectable computation:** explicit shapes, axes, units, dtypes, devices, clocks, randomness, numerical tolerances, failure states, and resolved configuration.
3. **Domain-specific experimental integrity:** separate controls for ordinary ML/DL, generative AI, time series, and reinforcement learning.
4. **Claim-level validation:** verification, validation, uncertainty, rival explanations, selection accounting, and protected confirmation.
5. **Verified error-learning loop:** preserve only confirmed lessons with their evidence, scope, and invalidation conditions.

No published paper proves that this exact ChatGPT skill will improve research. The literature establishes the practices the skill should enforce. The completed skill must still be evaluated prospectively on a preregistered suite of flawed and valid research-coding tasks before it can be called effective.

## 1. Review method

### 1.1 Evidence included

The review prioritizes:

- published books from established scientific and technical publishers;
- peer-reviewed journal and conference papers;
- consensus or standards-oriented reports;
- official language and framework documentation for exact software behavior.

Blog posts, generic coding advice, and repository popularity were not treated as scientific validation. Official documentation supports facts about a platform—for example, that Python optimization removes `assert` statements—but does not by itself establish a general scientific methodology.

### 1.2 Internal evidence labels

These labels organize this review; they are not a published evidence-grading standard.

| Label | Meaning |
|---|---|
| **Strongly supported** | Convergent support from authoritative books, consensus guidance, or multiple peer-reviewed studies |
| **Supported with conditions** | The direction is supported, but the rule depends on design, domain, cost, or implementation context |
| **Direct software fact** | Verified behavior in official technical documentation |
| **Design synthesis** | A proposed agent rule derived from the literature; it requires prospective testing as a skill behavior |

## 2. Audit of the inherited principles

### 2.1 Principle-by-principle verdict

| Inherited idea | Verdict | Evidence-based replacement |
|---|---|---|
| Understand the experiment before writing code | **Strongly supported** | First reconstruct the scientific question, claim type, data and split structure, evaluation unit, baselines, assumptions, and decision criterion. Ask only questions whose answers could change the implementation or conclusion. |
| Act as a scientific collaborator, not a passive code generator | **Supported with conditions** | Inspect available artifacts first; then challenge consequential ambiguities, formalize assumptions, and propose falsifying tests. Do not create conversational friction for inconsequential choices. |
| Fail loudly; crashing is always better | **Requires rewrite** | Fail fast on violated scientific invariants and corrupted evidence. Handle expected operational failures explicitly with bounded retries, checkpoints, and failure logs. Never turn a failure into plausible-looking scientific data. |
| Never use defaults for experimental parameters | **Requires rewrite** | Defaults are acceptable only when visible, versioned, scientifically justified, and included in a saved resolved configuration. Hidden or changing defaults are prohibited. |
| Make units, shapes, assumptions, and axes explicit | **Strongly supported** | Extend the contract to dtype, device, coordinate system, mask semantics, missingness, indexing convention, timestamp meaning, information-availability time, and batch/sequence/channel axes. |
| Correctness before performance | **Supported with conditions** | Establish a reference oracle, invariants, and numerical tolerances before optimization. Profile before optimizing; validate mixed precision, vectorization, compilation, distribution, and approximation against the reference. |
| Raw data are immutable | **Strongly supported** | Preserve a canonical raw artifact or authoritative reference with hashes and access metadata. Produce versioned derived data; do not overwrite the canonical source. Ethical or legal restrictions may prevent public release but not internal provenance. |
| Every result must be exactly reproducible | **Scientifically incorrect as a universal rule** | Provenance is mandatory. Require exact computational reruns when feasible; otherwise require numerical or statistical consistency within declared tolerances. Keep **reproducibility** distinct from independent **replicability**. |
| Validate against reality, not only against specifications | **Strongly supported but incomplete** | Separate code verification, numerical verification, model validation, and uncertainty assessment. Use analytical cases, limiting cases, properties, metamorphic relations, regression tests, simulations, and protected real data as appropriate. |
| Statistical honesty | **Strongly supported** | Define the estimand, evaluation unit, primary metric, practical threshold, uncertainty procedure, multiplicity plan, and selection process before confirmatory analysis. Report effects and uncertainty, not only thresholds or p-values. |
| Use established libraries; do not reinvent everything | **Supported with conditions** | Prefer maintained libraries after verifying versions, assumptions, numerical behavior, licenses, and domain suitability. A popular library is not evidence that the scientific use is correct. |
| Do not refactor validated code | **Incorrect as a blanket rule** | Protect validated behavior with characterization, unit, integration, and regression tests; make small reviewable changes; require parity evidence. Indefinitely preserving unmaintainable code creates technical debt and new scientific risk. |

### 2.2 Why the strongest corrections are necessary

#### Exact reproducibility is not universal

The National Academies distinguishes computational reproducibility—consistent results using the same data, methods, code, and conditions—from replicability across studies using new data. “Consistent” need not mean bitwise identity across hardware, libraries, or stochastic pipelines. [The National Academies report](https://nap.nationalacademies.org/catalog/25303/reproducibility-and-replicability-in-science) and [PyTorch’s reproducibility documentation](https://docs.pytorch.org/docs/stable/notes/randomness.html) both contradict a universal promise of exact identity. The skill should demand complete provenance and declare the attainable reproduction level:

- **bitwise**: identical bytes under a frozen environment;
- **numerical**: agreement within justified absolute/relative or domain tolerances;
- **statistical**: results compatible under a prespecified stochastic comparison;
- **replicative**: the scientific conclusion persists with new data or an independent implementation.

#### Python `assert` cannot guard scientific evidence

Python’s `-O` option removes `assert` statements and code conditional on `__debug__`. This is a [direct language behavior](https://docs.python.org/3/using/cmdline.html#cmdoption-O). Therefore:

- use explicit exceptions for input validation, split integrity, unit/shape checks, impossible values, and artifact consistency;
- reserve `assert` for developer-only conditions that may safely disappear in optimized execution;
- test critical validators under ordinary and optimized Python execution.

#### The broadcasting example needs correction

NumPy compares trailing dimensions for equality or the value `1`; incompatible dimensions normally raise an error. The general expression `(n,) * (n, 3)` does **not** silently broadcast for arbitrary `n`; it usually fails and only aligns in special shapes such as `n = 3`. The rule should teach explicit axis contracts and shape tests using the actual [NumPy broadcasting rules](https://numpy.org/doc/stable/user/basics.broadcasting.html), not preserve a misleading example.

#### Automatic Shapiro/Levene gating is not a safe statistical template

A generic sequence of Shapiro–Wilk test, then Levene test, then selection of Student/Welch/nonparametric testing treats the observed data as an automatic test-selection engine. Simulation work shows that preliminary normality testing changes the conditional error behavior of the subsequent analysis; assumptions cannot be certified merely because a preliminary test is nonsignificant. [Rochon, Gondan, and Kieser (2012)](https://bmcmedresmethodol.biomedcentral.com/articles/10.1186/1471-2288-12-81) analyze this two-stage problem. [Delacre et al. (2017)](https://rips-irsp.com/articles/10.5334/irsp.82) show why Welch’s test is often a safer default than switching based on observed variance tests.

The skill must instead ask:

1. What is the estimand?
2. What is the independent evaluation unit?
3. Is the comparison paired, clustered, repeated, temporal, or adaptively selected?
4. Which assumptions follow from the design and data-generating process?
5. Which uncertainty procedure matches that structure?

No statistical test should be selected solely from a metric table.

#### Validated code can be changed safely

Scientific software needs change control, not permanent immobilization. Regression tests protect previously observed behavior, while characterization tests document behavior before changes. [Peng et al. (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8128694/) discuss unit and regression testing of scientific software; [Feathers’ *Working Effectively with Legacy Code*](https://www.oreilly.com/library/view/working-effectively-with/0131177052/) develops tests for safe changes. In ML systems, configuration debt, data dependencies, feedback loops, and entanglement themselves create risk, as described by [Sculley et al. (2015)](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems).

The proper rule is: **freeze the scientific behavior, not the code structure**.

## 3. Canonical principles for the new skill

The following principles should be the normative core of the final skill.

### P1. Evidence boundary before action

Classify each material statement as direct observation, user report, derivation, external evidence, hypothesis, assumption, or unknown. Do not turn user certainty, filenames, plausible values, or prior chat output into verified evidence.

### P2. Scientific contract before code

Before substantive implementation, state the research question, claim type, target population or environment, data-generating process, estimand/objective, evaluation unit, candidate explanations, protected evidence, and decision rule. The level of formality should match the stakes.

### P3. Mathematical contract

Define symbols, domains, dimensions, units, indices, random variables, conditioning, loss/objective, constraints, and boundary conditions. Separate:

- definitions from assumptions;
- sufficient from necessary conditions;
- population quantities from estimators;
- theoretical guarantees from empirical observations.

Attempt a counterexample before claiming a universal guarantee.

### P4. Information-availability integrity

Every feature, label, normalization statistic, retrieval result, human annotation, reward, and external signal must have an availability time. Code may use only information available at the simulated decision point. This generalizes train/test leakage control to temporal forecasting, retrieval-augmented generation, and reinforcement learning.

### P5. Explicit computational semantics

Inputs and outputs must specify shapes, axes, units, dtype, device, missing-value semantics, ordering, masks, timestamps, and allowed ranges. Runtime scientific invariants use explicit exceptions, not removable assertions.

### P6. Complete resolved configuration

Every run must save the fully resolved configuration, including inherited defaults, data and code identities, environment, hardware, seeds, deterministic settings, numerical precision, model revision, and evaluation protocol. A command line alone is insufficient when defaults are hidden.

### P7. Layered validation

Use the relevant layers:

1. static checks and type/schema validation;
2. unit tests;
3. analytical or hand-computed cases;
4. limit, symmetry, invariance, conservation, and dimensional checks;
5. metamorphic/property tests when a direct oracle is unavailable;
6. regression and characterization tests;
7. end-to-end integration tests;
8. protected empirical validation;
9. independent replication when the claim requires it.

Scientific software often has an “oracle problem,” so example-based unit tests alone are insufficient. This conclusion is supported by the [systematic review of scientific-software testing](https://pmc.ncbi.nlm.nih.gov/articles/PMC4128280/) and the numerical-analysis treatment in [Higham’s *Accuracy and Stability of Numerical Algorithms*](https://epubs.siam.org/doi/10.1137/1.9780898718027).

### P8. Numerical integrity

Reason explicitly about finite precision, conditioning, stability, cancellation, overflow/underflow, reduction order, accumulation precision, and tolerance selection. Use `isclose`-style tolerances only when their scale and scientific meaning are justified. [Goldberg (1991)](https://dl.acm.org/doi/10.1145/103162.103163) and [Higham (2002)](https://epubs.siam.org/doi/10.1137/1.9780898718027) establish why real arithmetic cannot be assumed in floating-point computation.

### P9. Verification is not validation

“The code solves the equations correctly” is different from “the equations or model adequately represent the intended system.” The skill must label code verification, solution/numerical verification, model validation, and uncertainty separately, following the framework developed in [Oberkampf and Roy’s *Verification and Validation in Scientific Computing*](https://www.cambridge.org/core/books/verification-and-validation-in-scientific-computing/05CA1F8F3CCB5AE5445FDF55239A0183).

### P10. Fair comparison and selection accounting

Comparisons require equal information, preprocessing, tuning opportunity, compute accounting, stopping rules, and evaluation access unless differences are part of the claim. Record the full number of candidates, prompts, seeds, checkpoints, backtests, or analyses considered. The best observed result after extensive search is not equivalent to a prespecified comparison.

### P11. Uncertainty and practical significance

Report effects, uncertainty, and practical relevance. A p-value is not the probability that the hypothesis is true and does not measure effect size. Avoid binary “significant/not significant” reasoning; report the analysis design and all material results. See the [ASA statement on p-values](https://doi.org/10.1080/00031305.2016.1154108) and its [2019 follow-up](https://doi.org/10.1080/00031305.2019.1583913). Multiplicity controls such as [Benjamini–Hochberg](https://academic.oup.com/jrsssb/article/57/1/289/7035855) apply under stated objectives and assumptions; they are not a universal post-processing ritual.

### P12. Immutable provenance, versioned derivation

Preserve canonical raw sources, hashes, licensing/access restrictions, transformations, intermediate identities, and raw values underlying figures and tables. The workflow recommendations in [Sandve et al. (2013)](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285), [Wilson et al. (2014)](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745), and [Wilson et al. (2017)](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510) support this traceability.

### P13. Transparent data and model documentation

Record dataset motivation, composition, collection, preprocessing, intended use, known limitations, subgroup concerns, and maintenance. Record model purpose, training/evaluation conditions, intended and out-of-scope uses, performance by relevant groups or conditions, and limitations. [Datasheets for Datasets](https://dl.acm.org/doi/10.1145/3458723), [Model Cards](https://dl.acm.org/doi/10.1145/3287560.3287596), and the [FAIR principles](https://www.nature.com/articles/sdata201618) provide established documentation foundations.

### P14. Safe, reviewable evolution

Make small changes; preserve baselines and reference artifacts; add characterization tests before altering poorly understood behavior; perform parity and sensitivity checks; document intentional scientific changes separately from refactoring.

### P15. Conservative scientific writing

Match every sentence to its evidence strength. Distinguish observation, association, prediction, explanation, and causal effect. State uncertainty, boundary conditions, rival explanations, null or adverse results, and what remains unknown. Never write “proves,” “guarantees,” “state of the art,” or “generalizes” unless the evidence and claim domain justify those words.

### P16. Verified error-learning loop

After a consequential failure or correction:

1. preserve the failing artifact and context;
2. identify the proximal bug and deeper process cause;
3. add the smallest regression test that would have caught it;
4. record the lesson, evidence, scope, owner/approval, and invalidation condition;
5. re-run affected validations;
6. promote the lesson to project memory only after verification or human approval.

This is a **design synthesis** from regression testing, provenance, and scientific change-control practices. It should not be called active learning. In established ML terminology, [Settles’ *Active Learning*](https://link.springer.com/book/10.1007/978-3-031-01560-1) concerns a learner selecting informative unlabeled examples for an oracle to label.

## 4. Domain-specific requirements

### 4.1 Python scientific-computing module

The skill should require:

- explicit exceptions for scientific invariants;
- tests for shapes, axes, units, dtype, device, finite values, ordering, and missingness;
- controlled randomness using recorded generator state or seed lineage;
- a fully resolved configuration artifact;
- pinned or captured dependency versions and relevant system libraries;
- immutable inputs and atomic/versioned outputs;
- no bare `except`, silent fallback, or substitution of missing data with plausible values;
- reference and optimized implementations for consequential vectorization, mixed precision, compilation, or parallelism;
- profiling before performance optimization;
- unit, property/metamorphic, regression, and end-to-end tests selected by scientific risk;
- raw numerical values behind every plot and table.

The evidence base includes [*Research Software Engineering with Python*](https://third-bit.com/py-rse/), the Wilson scientific-computing papers, the scientific-software testing review, and numerical-analysis sources above.

### 4.2 ML/DL module

The ordinary ML/DL workflow must add:

- split design based on the independent unit: subject, group, site, time, event, document, or environment;
- fitting of preprocessing, feature selection, imputation, augmentation policy, calibration, and threshold selection within the training/development boundary;
- protected test data that do not influence model, prompt, checkpoint, or analysis selection;
- explicit baseline rationale and equal tuning opportunity;
- reporting of all material seeds and stochastic sources, not a single favorable run;
- distributional summaries or intervals, not only the best score;
- complete hyperparameter search spaces, budgets, early stopping, checkpoint rules, and number of trials;
- ablations tied to causal questions about components, not cosmetic removal tables;
- subgroup, shift, calibration, failure, and resource evaluation when relevant;
- data/model documentation and leakage audit.

The [REFORMS checklist](https://www.science.org/doi/10.1126/sciadv.adk3452) contains 32 reporting items across eight modules for validity, reproducibility, and generalizability. [Kapoor and Narayanan (2023)](https://www.sciencedirect.com/science/article/pii/S2666389923001599) document leakage across many scientific fields. [Bouthillier et al. (2021)](https://proceedings.mlsys.org/paper_files/paper/2021/hash/0184b0cd3cfb185989f858a1d9f5c1eb-Abstract.html) show that data sampling, initialization, and hyperparameter choice materially affect benchmarks. [Reimers and Gurevych (2017)](https://aclanthology.org/D17-1035/) show why reporting one score for a stochastic model is inadequate. The [NeurIPS reproducibility program report](https://jmlr.org/papers/v22/20-303.html) supports code, data, hyperparameter, and reporting controls.

### 4.3 Generative-AI module

Generative-AI evaluation must treat model calls and evaluators as stochastic, versioned measurement instruments. Record:

- provider, exact model/revision or reported alias, access date, region if relevant, and API/framework version;
- system/developer/user prompts, templates, retrieval context, few-shot examples, tools, and prompt hashes;
- decoding parameters, seed if supported, maximum tokens, stopping rules, safety settings, retry policy, and concurrency;
- raw outputs, refusals, invalid responses, timeouts, retries, and parsing failures as separate events;
- evaluation sample construction, contamination status, and temporal cutoff assumptions;
- repeated samples when generation randomness affects the claim;
- judge model, judge prompt, candidate order, randomization, rubric, parsing, and judge failures;
- calibration of automated judges against blinded human judgments for the target task;
- accuracy/quality plus calibration, robustness, bias/fairness, toxicity/safety, latency, token use, and cost when relevant;
- protected prompts/examples for final confirmation.

[HELM](https://openreview.net/forum?id=iO4LZibEqW) demonstrates multidimensional, transparent language-model evaluation rather than reliance on one aggregate score. [Zheng et al. (2023)](https://papers.nips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html) document position and other biases in LLM-based judging. [Deng et al. (2024)](https://aclanthology.org/2024.naacl-long.482/) show why benchmark contamination must be considered, especially for opaque training corpora.

Closed model APIs can change without a user-controlled version. The skill must therefore avoid promising independent exact reproducibility and instead preserve observable request/response provenance and state the model-version uncertainty.

### 4.4 Time-series module

Time-series research must define four clocks when applicable:

1. observation/event time;
2. data-availability or publication time;
3. prediction/decision time;
4. action/execution time.

The skill should require:

- a target, horizon, origin, update/retraining schedule, window rule, and information set;
- chronological or rolling-origin evaluation when nonstationarity or real deployment demands it;
- fold-local fitting of transformations and model selection;
- explicit handling of gaps, embargoes, overlapping labels, revisions, late-arriving data, seasonality, and missing intervals;
- naive and domain-standard forecast baselines;
- results by horizon and period, plus interval/calibration assessment when probabilistic forecasts are claimed;
- regime/shift sensitivity and residual diagnostics;
- a complete trial ledger for repeated backtests or strategy searches;
- transaction costs, slippage, latency, capacity, and execution assumptions for trading/decision systems.

[Tashman (2000)](https://doi.org/10.1016/S0169-2070(00)00065-0) analyzes split rules, rolling origins/windows, updating, recalibration, and multiple test periods. [Cerqueira, Torgo, and Mozetič (2020)](https://link.springer.com/article/10.1007/s10994-020-05910-7) find that order-preserving out-of-sample methods are most accurate under nonstationarity, while some cross-validation approaches may be appropriate for stationary series. Therefore, “random cross-validation is always invalid” would also be too absolute. [Bailey et al.](https://www.risk.net/journal-of-computational-finance/2471206/the-probability-of-backtest-overfitting) show why selecting among many backtests can produce overfitting.

### 4.5 Reinforcement-learning module

RL code must formalize the task as an MDP or POMDP when appropriate:

\[
(\mathcal S, \mathcal A, P, R, \gamma, \rho_0),
\]

and document observation, action, reward, transition, termination, and truncation semantics. It should require:

- environment, wrapper, task, simulator, and dependency versions;
- reward construction and scale, action bounds, observation normalization, and hidden state;
- correct distinction between termination and time-limit truncation in bootstrapping;
- separate training and evaluation environments/episodes and no evaluation adaptation unless declared;
- multiple independent seeds and preserved learning curves, not only the best checkpoint;
- prespecified checkpoint-selection and evaluation-episode rules;
- equal environment steps, wall-clock/compute reporting, and hyperparameter-search budgets across methods;
- strong baselines and implementation parity checks;
- interval estimates and robust aggregate summaries across tasks;
- support/coverage diagnostics, behavior-policy provenance, and off-policy estimator assumptions for offline RL;
- simulator-to-real and safety boundaries when claims extend beyond simulation.

[Sutton and Barto’s textbook](https://mitpress.mit.edu/9780262039246/reinforcement-learning/) supplies the mathematical foundation. [Henderson et al. (2018)](https://ojs.aaai.org/index.php/aaai/article/view/11694) document reproducibility and reporting problems in deep RL. [Agarwal et al. (2021)](https://papers.nips.cc/paper/2021/hash/f514cec81cb148559cf475e7426eed5e-Abstract.html) show that point estimates from few runs can be unreliable and develop interval/performance-profile recommendations. [Patterson et al. (2024)](https://jmlr.org/papers/v25/23-0183.html) provide a comprehensive treatment of empirical RL design. The termination/truncation consequence is also documented in the official [Gymnasium time-limit guide](https://gymnasium.farama.org/tutorials/gymnasium_basics/handling_time_limits/).

## 5. Proposed skill architecture

The final skill should be concise at the entry point and use progressive disclosure.

```text
rigorous-ai-research-coding/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── 01_scientific_contract.md
│   ├── 02_mathematical_and_numerical_thinking.md
│   ├── 03_python_research_software.md
│   ├── 04_ml_dl_experimental_integrity.md
│   ├── 05_generative_ai_evaluation.md
│   ├── 06_time_series_validation.md
│   ├── 07_reinforcement_learning_validation.md
│   ├── 08_statistics_and_uncertainty.md
│   ├── 09_critical_scientific_writing.md
│   └── 10_verified_error_learning.md
├── scripts/
│   ├── validate_experiment_manifest.py
│   ├── audit_split_integrity.py
│   ├── capture_environment.py
│   └── check_result_bundle.py
└── assets/
    ├── experiment_manifest.template.yaml
    ├── result_bundle.schema.json
    ├── model_evaluation_card.template.md
    └── error_learning_record.template.md
```

### Entry-point behavior

Because the account is shared, the skill description should preserve manual invocation. It should activate only when a user explicitly selects or names the skill. Once active, it should:

1. inspect project artifacts before asking questions;
2. establish the evidence and scientific contract;
3. route to the relevant domain reference;
4. implement the smallest scientifically complete change;
5. run risk-matched validation;
6. report evidence, unknowns, failures, and next decisive step;
7. update project memory only with verified, consequential lessons and only when authorized.

## 6. How the skill itself must be validated

### 6.1 What cannot be claimed yet

The literature validates the underlying practices, not the behavioral effectiveness of a prompt/skill bundle. Before publication, do not claim that the skill “guarantees rigorous research,” “prevents hallucination,” or “works perfectly.”

### 6.2 Prospective evaluation suite

Freeze the skill version and test it against a balanced corpus with expected decisions and rationales.

| Test family | Required cases | Pass condition |
|---|---|---|
| Activation isolation | Explicit invocation, ordinary coding without invocation, another user/project | Activates only on the declared trigger and does not leak project memory |
| Evidence integrity | Missing experiment ID, synthetic result, conflicting artifacts, user-provided “realistic” numbers | Refuses fabrication; labels source status; requests decisive evidence |
| Python correctness | `assert` under `-O`, shape/axis ambiguity, NaN/Inf, dtype/device mismatch, silent fallback | Uses durable validation and exposes failure |
| Numerical reasoning | cancellation, ill-conditioning, tolerance misuse, mixed-precision change | Identifies risk and validates against a reference or bound |
| ML/DL integrity | preprocessing leakage, group leakage, test-set selection, one favorable seed, unequal tuning budgets | Detects the flaw and proposes protected confirmation |
| Generative AI | prompt drift, LLM-judge position bias, retries hidden as successes, contamination unknown | Records instrument conditions and limits the conclusion |
| Time series | future feature, revised data, random split under drift, repeated backtest selection | Enforces clock/information-set integrity and selection accounting |
| RL | truncation treated as terminal, best seed only, different environment steps, evaluation adaptation | Corrects semantics and demands fair interval-based evaluation |
| Writing | causal overclaim, “proves” from one run, p-value-only conclusion, hidden null result | Rewrites claim to match evidence and uncertainty |
| Error learning | synthetic failure, verified bug, invalidated old lesson | Stores only approved evidence with scope and invalidation conditions |

### 6.3 Evaluation protocol

1. Define the rubric and expected failure class before running the skill.
2. Include positive controls so the skill does not reject every task.
3. Use paraphrased and adversarial variants to avoid memorizing test wording.
4. Score detection, scientific correctness, calibration, actionability, and unnecessary obstruction separately.
5. Have at least two qualified reviewers independently rate ambiguous cases and adjudicate disagreements.
6. Record model version, skill commit, project instructions, available files, and full outputs.
7. Treat modifications made after viewing test failures as development; evaluate the frozen revision on a protected test set.
8. Publish limitations and all material failures, not only showcase examples.

### 6.4 Minimum release gate

A public `v1.0.0` should require:

- no critical evidence-fabrication or leakage miss on the protected suite;
- no use of removable `assert` for critical runtime validation in included scripts;
- every script passing unit and integration tests under supported Python versions;
- correct manual activation and project isolation;
- all citations checked against the rule they support;
- documented limitations and unsupported domains;
- a reproducible release manifest with hashes.

## 7. Source map

### Scientific computing, software, and provenance

- Greg Wilson et al., [“Best Practices for Scientific Computing”](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745), *PLOS Biology*, 2014.
- Greg Wilson et al., [“Good Enough Practices in Scientific Computing”](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510), *PLOS Computational Biology*, 2017.
- Geir K. Sandve et al., [“Ten Simple Rules for Reproducible Computational Research”](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285), *PLOS Computational Biology*, 2013.
- Damien Irving et al., [*Research Software Engineering with Python*](https://www.routledge.com/Research-Software-Engineering-with-Python-Building-software-that-makes-research-possible/Irving-Hertweck-Johnston-Ostblom-Wickham-Wilson/p/book/9780367698324), CRC Press, 2021.
- National Academies of Sciences, Engineering, and Medicine, [*Reproducibility and Replicability in Science*](https://nap.nationalacademies.org/catalog/25303/reproducibility-and-replicability-in-science), 2019.
- Upulee Kanewala and James M. Bieman, [“Testing Scientific Software: A Systematic Literature Review”](https://pmc.ncbi.nlm.nih.gov/articles/PMC4128280/), *Information and Software Technology*, 2014.
- Zhe Peng et al., [“Unit and Regression Tests of Scientific Software”](https://pmc.ncbi.nlm.nih.gov/articles/PMC8128694/), 2021.
- Michael Feathers, [*Working Effectively with Legacy Code*](https://www.oreilly.com/library/view/working-effectively-with/0131177052/), Prentice Hall, 2004.

### Mathematics, numerical analysis, and validation

- Nicholas J. Higham, [*Accuracy and Stability of Numerical Algorithms*, 2nd ed.](https://epubs.siam.org/doi/10.1137/1.9780898718027), SIAM, 2002.
- David Goldberg, [“What Every Computer Scientist Should Know About Floating-Point Arithmetic”](https://dl.acm.org/doi/10.1145/103162.103163), *ACM Computing Surveys*, 1991.
- William L. Oberkampf and Christopher J. Roy, [*Verification and Validation in Scientific Computing*](https://www.cambridge.org/core/books/verification-and-validation-in-scientific-computing/05CA1F8F3CCB5AE5445FDF55239A0183), Cambridge University Press.

### ML/DL validity and reporting

- Joelle Pineau et al., [“Improving Reproducibility in Machine Learning Research”](https://jmlr.org/papers/v22/20-303.html), *JMLR*, 2021.
- Sayash Kapoor et al., [“REFORMS: Consensus-based Recommendations for Machine-learning-based Science”](https://www.science.org/doi/10.1126/sciadv.adk3452), *Science Advances*, 2024.
- Sayash Kapoor and Arvind Narayanan, [“Leakage and the Reproducibility Crisis in Machine-learning-based Science”](https://www.sciencedirect.com/science/article/pii/S2666389923001599), *Patterns*, 2023.
- Xavier Bouthillier et al., [“Accounting for Variance in Machine Learning Benchmarks”](https://proceedings.mlsys.org/paper_files/paper/2021/hash/0184b0cd3cfb185989f858a1d9f5c1eb-Abstract.html), *MLSys*, 2021.
- Nils Reimers and Iryna Gurevych, [“Reporting Score Distributions Makes a Difference”](https://aclanthology.org/D17-1035/), *EMNLP*, 2017.
- David Sculley et al., [“Hidden Technical Debt in Machine Learning Systems”](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems), *NeurIPS*, 2015.
- Timnit Gebru et al., [“Datasheets for Datasets”](https://dl.acm.org/doi/10.1145/3458723), *Communications of the ACM*, 2021.
- Margaret Mitchell et al., [“Model Cards for Model Reporting”](https://dl.acm.org/doi/10.1145/3287560.3287596), *FAT\** 2019.

### Statistics

- Ronald L. Wasserstein and Nicole A. Lazar, [“The ASA Statement on p-Values”](https://doi.org/10.1080/00031305.2016.1154108), *The American Statistician*, 2016.
- Ronald L. Wasserstein, Allen L. Schirm, and Nicole A. Lazar, [“Moving to a World Beyond p < 0.05”](https://doi.org/10.1080/00031305.2019.1583913), *The American Statistician*, 2019.
- Yoav Benjamini and Yosef Hochberg, [“Controlling the False Discovery Rate”](https://academic.oup.com/jrsssb/article/57/1/289/7035855), *JRSS B*, 1995.
- Justine Rochon, Matthias Gondan, and Meinhard Kieser, [“To Test or Not to Test”](https://bmcmedresmethodol.biomedcentral.com/articles/10.1186/1471-2288-12-81), *BMC Medical Research Methodology*, 2012.
- Marie Delacre et al., [“Why Psychologists Should by Default Use Welch’s t-test”](https://rips-irsp.com/articles/10.5334/irsp.82), *International Review of Social Psychology*, 2017.

### Generative AI

- Percy Liang et al., [“Holistic Evaluation of Language Models”](https://openreview.net/forum?id=iO4LZibEqW), *Transactions on Machine Learning Research*, 2023.
- Lianmin Zheng et al., [“Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena”](https://papers.nips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html), *NeurIPS*, 2023.
- Chunyuan Deng et al., [“Investigating Data Contamination in Modern Benchmarks for Large Language Models”](https://aclanthology.org/2024.naacl-long.482/), *NAACL*, 2024.

### Time series

- Rob J. Hyndman and George Athanasopoulos, [*Forecasting: Principles and Practice*, 3rd ed.](https://otexts.com/fpp3/).
- Leonard J. Tashman, [“Out-of-sample Tests of Forecasting Accuracy”](https://doi.org/10.1016/S0169-2070(00)00065-0), *International Journal of Forecasting*, 2000.
- Vitor Cerqueira, Luís Torgo, and Igor Mozetič, [“Evaluating Time Series Forecasting Models”](https://link.springer.com/article/10.1007/s10994-020-05910-7), *Machine Learning*, 2020.
- David H. Bailey et al., [“The Probability of Backtest Overfitting”](https://www.risk.net/journal-of-computational-finance/2471206/the-probability-of-backtest-overfitting), *Journal of Computational Finance*.

### Reinforcement learning

- Richard S. Sutton and Andrew G. Barto, [*Reinforcement Learning: An Introduction*, 2nd ed.](https://mitpress.mit.edu/9780262039246/reinforcement-learning/), MIT Press, 2018.
- Peter Henderson et al., [“Deep Reinforcement Learning That Matters”](https://ojs.aaai.org/index.php/aaai/article/view/11694), *AAAI*, 2018.
- Rishabh Agarwal et al., [“Deep Reinforcement Learning at the Edge of the Statistical Precipice”](https://papers.nips.cc/paper/2021/hash/f514cec81cb148559cf475e7426eed5e-Abstract.html), *NeurIPS*, 2021.
- Andrew Patterson et al., [“Empirical Design in Reinforcement Learning”](https://jmlr.org/papers/v25/23-0183.html), *JMLR*, 2024.

## Final design decision

Build a new manual-only ChatGPT skill from these corrected principles. Reuse the original repository’s high-level intent, but do not inherit its absolute claims, statistical recipe, critical use of `assert`, broadcasting example, Claude-specific structure, or lack of domain controls. The final skill should be judged by a protected behavioral evaluation, not by how convincing its prose sounds.
