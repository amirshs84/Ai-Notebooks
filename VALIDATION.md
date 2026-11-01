# Validation

All six curated notebooks were executed cell by cell in fresh Python processes on 2026-11-01, using a non-interactive Matplotlib backend. Text output and plots were regenerated; optional animations were not executed. A Jupyter kernel could not start in the execution environment, so this validates Python cell execution rather than the Jupyter server or interactive animation UI.

## Results

| Notebook | Status |
|---|---|
| `linear_models_and_feature_engineering.ipynb` | Passed (12 code cells) |
| `decision_trees_and_random_forests.ipynb` | Passed (8 code cells) |
| `nonogram_csp_solver_comparison.ipynb` | Passed (16 code cells) |
| `bayesian_network_inference_and_decisions.ipynb` | Passed (9 code cells) |
| `policy_and_value_iteration.ipynb` | Passed (20 code cells) |
| `taxi_q_learning_vs_sarsa.ipynb` | Passed (10 code cells) |

## Targeted correctness checks

`python verify_algorithms.py` passed:

- All 81 possible combinations of feasible individual row/column clues for 2 x 2 Nonograms, across four solvers: **324 solver checks**, including globally unsatisfiable specifications. Returned grids are checked against clues, and MRV domain counts are checked against actual domain membership.
- Bayesian joint distribution normalization and **60 posterior queries** compared with direct sums over the full joint distribution.

These checks do not prove correctness for all inputs and do not validate every model implementation or statistical conclusion. Larger solver cases are covered by the notebook runs. The Bayesian reference sums share the submitted joint-probability function, so they primarily validate posterior aggregation rather than independently validating the model specification.

## Execution environment

Python 3.12; NumPy 2.3.5; pandas 2.2.3; Matplotlib 3.10.8; scikit-learn 1.8.0; seaborn 0.13.2; Gymnasium 1.1.1; tqdm 4.70.1.

`requirements.txt` pins Gymnasium to retain Taxi-v3 support. Other ranges express compatibility intentions, not a guarantee that every allowed combination has been tested.
