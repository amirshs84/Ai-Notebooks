# AI Algorithms Portfolio

A curated collection of completed Artificial Intelligence coursework at **Sharif University of Technology**, covering supervised learning, constraint satisfaction, probabilistic reasoning, dynamic programming, and reinforcement learning.

**Portfolio owner:** Amirhossein Hashemi Shahroodi · [@amirshs84](https://github.com/amirshs84)

The emphasis is on implementing algorithms, visualizing their behavior, and interpreting experiments. These are educational projects derived from course assignments, not independent research papers or production systems. Course-provided scaffolding and datasets are acknowledged in [ATTRIBUTION.md](ATTRIBUTION.md).

## Explore the notebooks

| Notebook | What it does | Main techniques |
|---|---|---|
| [Linear models and feature engineering](notebooks/01_linear_models/linear_models_and_feature_engineering.ipynb) | Fits regression and classification models, visualizes decision boundaries, and explores polynomial features on circles, spirals, and checkerboards. | NumPy gradient descent, perceptron updates, logistic regression, one-vs-rest classification |
| [Decision trees and random forests](notebooks/02_tree_ensembles/decision_trees_and_random_forests.ipynb) | Classifies a supplied fictional Westeros dataset using scratch implementations and scikit-learn baselines; reports held-out accuracy, confusion matrices and feature importance. | Gini/entropy splits, recursive trees, bootstrap aggregation, random feature subsets, majority voting |
| [Nonogram CSP solver comparison](notebooks/03_constraint_solving/nonogram_csp_solver_comparison.ipynb) | Solves two Nonogram puzzles and compares search effort, pruning, backtracking and runtime. | Backtracking, forward checking, minimum remaining values, line-based AC-3-style propagation |
| [Bayesian network inference and decisions](notebooks/04_probabilistic_reasoning/bayesian_network_inference_and_decisions.ipynb) | Models a fictional ride-hailing surge decision, estimates a conditional probability table, computes exact posteriors and MAP explanations, and compares expected utilities. | D-separation, maximum-likelihood counts, exact enumeration, MAP, value of perfect information |
| [Policy and value iteration](notebooks/05_dynamic_programming/policy_and_value_iteration.ipynb) | Optimizes transfers between two car-rental locations and betting policies for the gambler's problem, with policy and value plots. | Finite MDPs, Poisson demand, policy evaluation/improvement, Bellman updates |
| [Taxi: Q-learning vs SARSA](notebooks/06_reinforcement_learning/taxi_q_learning_vs_sarsa.ipynb) | Compares two temporal-difference algorithms under fixed and decaying epsilon-greedy exploration at four training budgets. | Tabular Q-learning, SARSA, greedy evaluation, return/episode-length curves |

**Suggested reading order:** tree ensembles → reinforcement learning → constraint solving → Bayesian inference → linear models → dynamic programming. The first three provide a quick overview of implementation and experimental work.

## Run locally

Python **3.11 or newer** is recommended. Create an environment and install the dependencies:

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS / Linux:
# source .venv/bin/activate
python -m pip install -r requirements.txt
python -m jupyterlab
```

Open a notebook and execute its cells from top to bottom. **Use the notebook's own folder as its working directory:** the tree example reads `westeros_records.csv` next to the notebook, and the CSP example imports the adjacent `models.py` and `utils.py`.

- The linear-model datasets are generated in memory; no MNIST download is needed.
- The Westeros CSV is included as supplied with the course exercise.
- The Bayesian notebook regenerates its synthetic CSV with seed 42. It is an illustrative simulation, not actual ride-hailing data.
- The Nonogram baseline may take several minutes on the larger puzzle.
- Taxi runs 16 training configurations: 4 algorithm/exploration combinations at 500, 1,000, 3,000 and 5,000 episodes. Runs execute sequentially for Windows/Jupyter portability.
- Animations are disabled by default to keep execution and GitHub previews manageable. Set `RUN_ANIMATIONS = True` in the relevant cell to enable them. Taxi animations also require **FFmpeg**; pygame is installed through the Gymnasium toy-text extra. No video encoder is required for the numerical experiments.

## How to interpret the results

- **Scratch vs library implementations:** the linear regression, perceptron, logistic regression, decision tree and random forest learning implementations are written in the notebooks. Scikit-learn is also used for dataset generation, feature transformations, metrics and explicitly labeled tree/forest baselines. The original neural-network section was a wrapper around `MLPClassifier`; it is excluded rather than advertised as a neural network written from scratch.
- **Generalization:** the linear-model decision-boundary examples display training accuracy. The tree notebook uses one 80/20 split; its comparisons are illustrative, and the scratch and library models do not have identical hyperparameters. Encoding categories before splitting also exposes the test set's category vocabulary; a stronger evaluation would fit preprocessing on training data only.
- **Probabilistic inference:** the submitted posterior routine enumerates the joint distribution. It is named `exact_posterior` here, not variable elimination. The six-variable Boolean network makes enumeration practical; this is not a scalability claim.
- **MDP approximation:** car-rental Poisson counts are truncated at the notebook's `POISSON_UPPER_BOUND`; omitted tail probability is not renormalized. The computed policy solves this approximate model. The gambler policy uses rounded action values for tie breaking.
- **Reinforcement learning:** greedy evaluation uses 20 fixed-seed episodes. Training randomness is not fully seeded in the submitted implementation, so reruns vary. Single runs and small evaluation sets do not establish algorithm superiority, convergence, or robustness; multiple training seeds and uncertainty intervals are future improvements.
- **Constraint solving:** domain compatibility, rollback after failed propagation, and MRV bookkeeping were repaired during curation. Old submitted timings are not used as benchmarks for the revised solver. AC-3-style propagation can reduce search but also has overhead.

## Validation

All six notebooks passed cell-by-cell execution with regenerated text and plots. Focused checks cover 324 small CSP cases and 60 Bayesian posterior queries. See [VALIDATION.md](VALIDATION.md) for the exact scope and execution environment.

## Curation and provenance

See [CURATION.md](CURATION.md) for the selection, original filenames, and changes. The original uploaded submissions remain separate. Personal student identifiers, worksheet PDFs, template branding, cache files, and unrelated assets are excluded.

This repository does not grant a blanket license over course-provided materials. Attribution is preserved; redistribution rights remain with the respective authors.
