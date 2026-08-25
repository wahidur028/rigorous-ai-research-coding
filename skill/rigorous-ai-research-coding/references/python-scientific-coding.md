# Python Scientific Coding

## Contract and structure

- Validate schemas, shapes, axes, units, dtypes, devices, missing values, and legal ranges at boundaries.
- Use explicit exceptions for critical checks. Python can remove `assert` statements under optimized execution.
- Keep scientific transformations separate from filesystem, network, logging, and orchestration code.
- Prefer small functions with explicit inputs and returned outputs over hidden mutable state.
- Keep raw inputs immutable. Write derived data and results to versioned locations.
- Save the fully resolved configuration used by each run, not only defaults or command-line overrides.
- Pass random-number generators or seeds explicitly. Avoid untracked global randomness.

## Change discipline

1. Reproduce or characterize existing behavior.
2. Add a failing test for the defect or unmet contract.
3. Make one conceptually coherent change.
4. Run targeted tests, then the relevant broader suite.
5. Compare outputs, performance, and resource use against the reference.
6. Preserve a rollback path through version control and immutable artifacts.

Refactoring validated code is legitimate when characterization and regression tests protect the behavior that matters. “Never refactor” is not a safety strategy.

## Failure behavior

- Fail loudly on invalid scientific inputs unless the contract defines recovery.
- Attach context to errors without exposing secrets or dumping unrestricted data.
- Bound retries and record every terminal failure.
- Do not convert missing, infinite, or malformed values into plausible defaults silently.

## Test portfolio

- Unit tests: formulas, preprocessing, metrics, parsers, and boundary conditions.
- Property or metamorphic tests: invariants across transformations and generated inputs.
- Integration tests: components, storage, configuration, and device transitions.
- End-to-end smoke tests: a tiny complete run that proves wiring, not scientific quality.
- Regression tests: every verified defect that could recur.
- Differential tests: optimized implementation versus a simple trusted reference.

## Evidence basis

- Wilson et al., *Best Practices for Scientific Computing*, PLOS Biology, 2014.
- Wilson et al., *Good Enough Practices in Scientific Computing*, PLOS Computational Biology, 2017.
- Sandve et al., *Ten Simple Rules for Reproducible Computational Research*, PLOS Computational Biology, 2013.
- Irving et al., *Research Software Engineering with Python*, 2021.
- Kanewala and Bieman, *Testing Scientific Software: A Systematic Literature Review*, Information and Software Technology, 2014.
- Python documentation, *Built-in Constants* and `-O` optimization behavior.
