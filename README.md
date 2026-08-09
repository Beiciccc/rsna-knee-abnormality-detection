# RSNA Knee Abnormality Detection

Public code and experiment records for the [RSNA Knee Abnormality Detection competition](https://www.kaggle.com/competitions/rsna-knee-abnormality-detection).

The challenge is to predict twelve clinically important knee abnormalities from MRI studies. Each study contains several DICOM series and an associated radiology report. Submissions are evaluated with the macro-average ROC AUC across the twelve targets.

## Repository contents

- [`docs/competition.md`](docs/competition.md): task, data, metric, and submission constraints.
- [`docs/public_baselines.md`](docs/public_baselines.md): reproducible public reference models and scores.
- [`scripts/validate_submission.py`](scripts/validate_submission.py): structural validation for `submission.csv`.
- [`tests/test_validate_submission.py`](tests/test_validate_submission.py): synthetic tests for the validator.
- [`notebooks/public/rsna-knee-submission-validator`](notebooks/public/rsna-knee-submission-validator): Kaggle-ready public validator.
- [`notebooks/public/rsna-knee-exp001-pilkwang-v14-anchor`](notebooks/public/rsna-knee-exp001-pilkwang-v14-anchor): scored Exp001 V2 reproduction anchor with full Apache-2.0 provenance and GPU compatibility preflight.
- [`notebooks/public/rsna-knee-research-tony-sakhawat-v1`](notebooks/public/rsna-knee-research-tony-sakhawat-v1): scored EXP002 V1 inference anchor with dual Apache-2.0 attribution and an external, non-redistributed checkpoint dependency.
- [`notebooks/public/rsna-knee-research-prvsiyan-v9-safe-reproduction`](notebooks/public/rsna-knee-research-prvsiyan-v9-safe-reproduction): scored EXP003 five-arm DINOv2 rank-ensemble source with Apache-2.0 attribution.
- [`notebooks/public/rsna-knee-research-renta-v5-safe-reproduction`](notebooks/public/rsna-knee-research-renta-v5-safe-reproduction): scored EXP004 20-member DINOv2-small source with Apache-2.0 Pilkwang attribution and Renta V5 configuration credit.
- [`experiments/experiment_log.md`](experiments/experiment_log.md): factual experiment and submission history.
- [`results/public_scores.md`](results/public_scores.md): official public leaderboard results.

Validated training and inference notebooks will be added as reproducible milestones. Competition data, medical images, model weights, and generated predictions are not included.

## Validation

```bash
python scripts/validate_submission.py submission.csv --test-csv /path/to/test.csv
python -m unittest discover -s tests
```

The validator checks the exact column schema, study identifiers and order, unique IDs, finite probabilities, and the `[0, 1]` range.

## Data access

Download the data directly from Kaggle after joining the competition and accepting its rules. Do not redistribute the competition data.

## License

Original code in this repository is released under the MIT License. Competition data and third-party assets remain governed by their respective terms. Derivative experiment notebooks identified in [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) are distributed under Apache-2.0 with attribution; the repository's original MIT-licensed files remain under the MIT License. Runtime dependencies and competition data remain subject to their source terms and are not redistributed.
