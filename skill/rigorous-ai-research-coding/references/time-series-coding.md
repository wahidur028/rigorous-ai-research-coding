# Time-Series Coding

## Establish the clocks

Track separately when relevant:

- event time: when the phenomenon occurred;
- observation time: when it was measured;
- availability time: when the value could be used;
- decision time: when the forecast or action was made.

No feature may use information unavailable at decision time.

## Evaluation design

- Define target, horizon, forecast origin, update frequency, window policy, and information set.
- Use chronological holdout or rolling-origin evaluation appropriate to the deployment process.
- Fit preprocessing and model selection within each training window.
- Add gaps or embargoes where overlapping labels or delayed availability create leakage.
- Account for revisions, time zones, daylight-saving changes, missing intervals, and overlapping horizons.
- Report performance by horizon and meaningful regime, not only one aggregate.

Random cross-validation is not automatically valid for temporal prediction. Justify any method that breaks chronology.

## Comparisons and backtests

- Include naive, seasonal-naive, and other domain-relevant baselines.
- Inspect residual dependence and changing regimes.
- Preserve every searched window, feature set, threshold, and model.
- For trading or operational backtests, model transaction costs, slippage, latency, capacity, and the causal information clock.
- Report the total number of strategies or configurations tried to expose selection pressure.

## Evidence basis

- Hyndman and Athanasopoulos, *Forecasting: Principles and Practice*, 3rd ed., 2021.
- Tashman, *Out-of-Sample Tests of Forecasting Accuracy*, International Journal of Forecasting, 2000.
- Cerqueira et al., *Evaluating Time Series Forecasting Models*, Machine Learning, 2020.
- Bailey et al., *The Probability of Backtest Overfitting*, Journal of Computational Finance, 2017.
