# Selection and changes

| Source archive | Original notebook | Portfolio treatment |
|---|---|---|
| HW1 | No notebook supplied; PDF only | Excluded from this notebook portfolio |
| HW2 | `Tic-Tac-Toe.ipynb` | Reviewed; omitted to prioritize more substantial comparisons |
| HW2 | `CSP_Nonogram_Student.ipynb` | Included as `nonogram_csp_solver_comparison.ipynb`, with required Python helpers |
| HW3 | `fmapp.ipynb` | Included as `bayesian_network_inference_and_decisions.ipynb` |
| HW3 | `hmm_dna.ipynb` | Excluded: normalizing filtering beliefs and then summing them reports a sequence likelihood of 1; sequence-likelihood scaling needs repair and validation |
| HW4 | `ml_core.ipynb` | Selected NumPy linear-model and feature-engineering sections only |
| HW4 | `westeros.ipynb` | Included as `decision_trees_and_random_forests.ipynb`, with its CSV |
| HW5 | `MDP.ipynb` | Included as `policy_and_value_iteration.ipynb` |
| HW5 | `qlearning_sarsa.ipynb` | Included as `taxi_q_learning_vs_sarsa.ipynb` |

## Changes beyond renaming

- Added descriptive titles, setup instructions, scope notes and course attribution. Removed student IDs, blank author placeholders and embedded institutional branding while retaining provenance here.
- Removed the original `NeuralNetworkScratch` section: its `fit` delegates to scikit-learn's `MLPClassifier`. The unavailable local MNIST dependency is removed with that section. No new scratch neural network was substituted.
- Corrected linear-model documentation on `predict_proba` shape, perceptron parameter shape, and unconditional convergence claims. Preserved the submitted learning implementations and experiment parameters.
- Renamed the Bayesian posterior routine to `exact_posterior`: its implementation is enumeration, not factor-based variable elimination. The optional elimination-order argument remains for existing call compatibility; enumeration does not use it.
- Replaced the RL process-pool experiment driver with a sequential loop for notebook portability. Removed text claiming that every configuration reached 100% success; the supplied fixed-epsilon SARSA output was 95%. Added single-run and RNG limitations. Algorithms and hyperparameters are retained.
- Repaired Nonogram propagation: arrangements respect current domains; failed AC-3 branches restore pruned domains; MRV counts change only when membership changes; attempted values are visited in stable order; an erroneous unprune is removed. Removed broad claims that AC-3 was faster and invalidated old timings after these changes.
- Disabled optional animations by default. Discarded stale submitted execution outputs before checking the curated notebooks.
- Omitted worksheet PDFs, Python bytecode caches and external local-file paths.

These are course-derived educational implementations. Publication here should not be interpreted as a claim to have designed the algorithms, authored all scaffolding, or completed independent research.
