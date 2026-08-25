# Contributing

Contributions are welcome when they improve scientific reliability, clarity, portability, or evaluation coverage.

## Before proposing a change

1. Open an issue describing the failure mode or missing use case.
2. Distinguish published evidence, direct observation, inference, and preference.
3. Explain which scientific invariant or user behavior should change.
4. Avoid adding broad rules based only on one anecdote.

## Pull-request requirements

- Keep `SKILL.md` concise and route detailed guidance to `references/`.
- Preserve manual-only activation unless a major version explicitly changes that policy.
- Add or update an evaluation case for behavioral changes.
- Add regression tests for script changes.
- Run `python tests/test_skill_scripts.py` and the skill validator.
- Do not include credentials, private datasets, fabricated results, or copyrighted full-text sources.
- State limitations and unsuccessful validation attempts.

Scientific-design changes should cite an authoritative book, standard, or peer-reviewed paper where feasible. Citation alone is not sufficient: explain how the source supports the proposed rule and where its scope ends.
