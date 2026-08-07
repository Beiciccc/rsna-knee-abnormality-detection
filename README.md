# RSNA Knee Abnormality Detection

Public code and experiment records for the [RSNA Knee Abnormality Detection competition](https://www.kaggle.com/competitions/rsna-knee-abnormality-detection).

The challenge is to predict twelve clinically important knee abnormalities from MRI studies. Each study contains several DICOM series and an associated radiology report. Submissions are evaluated with the macro-average ROC AUC across the twelve targets.

## Repository contents

- [`docs/competition.md`](docs/competition.md): task, data, metric, and submission constraints.
- [`docs/public_baselines.md`](docs/public_baselines.md): reproducible public reference models and scores.
- [`scripts/validate_submission.py`](scripts/validate_submission.py): structural validation for `submission.csv`.
- [`tests/test_validate_submission.py`](tests/test_validate_submission.py): synthetic tests for the validator.
- [`notebooks/public/rsna-knee-submission-validator`](notebooks/public/rsna-knee-submission-validator): Kaggle-ready public validator.
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

Original code in this repository is released under the MIT License. Competition data and third-party assets remain governed by their respective terms.
