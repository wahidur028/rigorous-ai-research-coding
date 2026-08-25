# Mathematical and Numerical Validation

## Formalize before translating

- Define symbols, domains, indices, units, random variables, conditioning information, and boundary cases.
- Separate definitions, assumptions, derivations, estimators, and empirical claims.
- Distinguish necessary conditions from sufficient conditions and population quantities from finite-sample estimates.
- Try a counterexample before accepting a universal claim.

## Map mathematics to code

For every consequential equation, state:

- tensor shape and meaning of each axis;
- elementwise versus matrix operation;
- reduction axes and normalization denominator;
- mask semantics, padding behavior, and empty-set behavior;
- indexing convention and boundary handling;
- units and dimensional consistency.

Do not treat successful NumPy or tensor broadcasting as evidence that the mathematical axes are correct.

## Numerical reliability

- Estimate scale, conditioning, and plausible error propagation.
- Check cancellation, overflow, underflow, loss of significance, and precision conversions.
- Use stable formulations such as log-sum-exp where justified.
- Define absolute and relative tolerances from the numerical problem and decision consequence, not convenience.
- Compare against higher precision, an analytic solution, or an independent reference on tractable cases.
- Treat deterministic output as distinct from numerical accuracy.

## Verification hierarchy

- Code verification: the equations were implemented correctly.
- Solution verification: discretization and numerical error are controlled.
- Model validation: the mathematical model adequately represents the target system for the intended use.
- Uncertainty analysis: important inputs, approximations, and stochastic variation are propagated or bounded.

Passing one layer does not establish the others.

## Evidence basis

- Higham, *Accuracy and Stability of Numerical Algorithms*, 2nd ed., 2002.
- Goldberg, *What Every Computer Scientist Should Know About Floating-Point Arithmetic*, ACM Computing Surveys, 1991.
- Oberkampf and Roy, *Verification and Validation in Scientific Computing*, 2010.
- NumPy documentation, *Broadcasting*.
