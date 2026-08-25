# Reinforcement-Learning Coding

## Define the interaction

- State the MDP or POMDP elements: observations, states if available, actions, transitions, rewards, discount, horizon, and initial-state distribution.
- Distinguish environment termination from time-limit truncation in code, targets, and metrics.
- Pin environment name, version, wrappers, preprocessing, reward transformations, and evaluation policy.
- Test on tiny deterministic environments where expected values or optimal behavior are known.

## Comparison discipline

- Use multiple prespecified seeds and retain full learning curves and failed runs.
- Define checkpoint selection and evaluation episodes before protected evaluation.
- Compare equal environment interactions and report compute or wall-clock cost when relevant.
- Use robust aggregate metrics and uncertainty across tasks rather than relying only on mean final return.
- Separate training exploration from deterministic or standardized evaluation behavior.

## Offline RL

- Version and hash the dataset and behavior-policy information when available.
- Audit action coverage, support mismatch, episode boundaries, terminal flags, and reward construction.
- Do not infer deployment safety from a single off-policy estimate.

## Evidence basis

- Sutton and Barto, *Reinforcement Learning: An Introduction*, 2nd ed., 2018.
- Henderson et al., *Deep Reinforcement Learning That Matters*, AAAI, 2018.
- Agarwal et al., *Deep Reinforcement Learning at the Edge of the Statistical Precipice*, NeurIPS, 2021.
- Patterson et al., *Empirical Design in Reinforcement Learning*, JMLR, 2024.
- Gymnasium documentation, *Handling Time Limits*.
