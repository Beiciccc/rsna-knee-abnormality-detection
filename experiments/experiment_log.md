# Experiment log

This ledger records validated experiments and official Kaggle submissions. Scores are copied only after they appear in the official submissions table.

| ID | Date (UTC) | Hypothesis | Main change | Validation | Kaggle notebook version | Submission ref | Public AUC | Status |
|---|---|---|---|---|---|---|---:|---|
| EXP001 | 2026-08-08 01:41:59.297 | Establish a reproducible public V14 anchor before controlled variants. | V2 adds exact T4 architecture and CUDA forward/backward/optimizer preflight plus hard failure on runtime exceptions; model and experiment settings are unchanged. | V1 ordinary run received Tesla P100 (`sm_60`), failed compatibility, and was not submitted; V2 passed the Tesla T4 (`sm_75`) preflight; selected r336 output validated with 3 studies, 12 targets, exact schema and order, finite values in `[0, 1]`, and SHA-256 `aa380a3d43ade50c3b5024b07a7068ca2001d8ceef9508c60a3111cf2641afe0`. | `beicicc/rsna-knee-exp001-pilkwang-v14-anchor` V2 | `55338077` | 0.825 | COMPLETE |
