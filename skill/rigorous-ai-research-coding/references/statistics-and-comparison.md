# Statistics and Comparison

## Specify before computing

- Define the estimand, evaluation unit, pairing or clustering, primary metric, meaningful-effect threshold, variation sources, selection process, multiplicity, and study stage.
- Match uncertainty to the data-generating and evaluation units. Do not treat correlated observations as independent.
- Preserve pairing between methods when they evaluate the same examples, subjects, seeds, tasks, or time periods.
- Distinguish sampling uncertainty, seed variation, hyperparameter-selection variation, and measurement error.

## Avoid automated test shopping

Do not use a mechanical Shapiro-Wilk/Levene decision tree to select a favorable parametric or nonparametric test. Assumptions follow from the design, estimand, sample size, dependence, and robustness analysis; preliminary tests do not erase those considerations.

## Selection and multiplicity

- Record all variants, prompts, metrics, subgroups, checkpoints, and comparisons examined.
- Use a prespecified confirmatory family and appropriate multiplicity control when many claims are tested.
- Treat post-selection estimates and intervals as exploratory unless the selection process is modeled or independent confirmation is obtained.
- A significance test cannot repair a test set already used for selection.

## Interpretation

- Report effect estimates and compatible uncertainty, not only p-values.
- Statistical significance does not imply practical importance, truth, or replication.
- Failure to reject does not establish equality; use an equivalence or noninferiority design when that is the question.
- State whether the analysis is exploratory, verified, confirmatory, or blocked.

## Evidence basis

- Wasserstein and Lazar, *The ASA Statement on p-Values*, The American Statistician, 2016.
- Wasserstein, Schirm, and Lazar, *Moving to a World Beyond p < 0.05*, The American Statistician, 2019.
- Benjamini and Hochberg, *Controlling the False Discovery Rate*, JRSS B, 1995.
- Rochon, Gondan, and Kieser, *To Test or Not to Test: Preliminary Assessment of Normality*, Statistics in Medicine, 2012.
- Delacre et al., *Why Psychologists Should by Default Use Welch's t-test Instead of Student's t-test*, International Review of Social Psychology, 2017.
