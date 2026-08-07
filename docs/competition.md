# Competition reference

Verified against the official Kaggle competition pages on 2026-08-07.

## Task

Predict a per-study probability for each of twelve knee MRI findings:

1. ACL injury
2. MCL injury
3. Medial meniscus tear
4. Lateral meniscus tear
5. Medial-compartment osteoarthritis
6. Lateral-compartment osteoarthritis
7. Patellofemoral osteoarthritis
8. Joint effusion
9. Synovitis
10. Baker's cyst
11. Bone contusion
12. Fracture

The training set includes 4,407 MRI studies, 24,371 series, and multilingual free-text radiology reports. Only 58 studies have complete image-reviewed condition labels, so the reports can provide additional weak supervision. The scoring test set contains approximately 1,300 studies and has no reports.

## Data layout

- `train.csv`: study identifier, report, and twelve binary targets. The live file does not contain `PatientSex`; the host confirmed that it was removed from the CSV and may instead be read from DICOM metadata ([discussion 733423](https://www.kaggle.com/competitions/rsna-knee-abnormality-detection/discussion/733423)).
- `train_series.csv`: series identifier, fluid sensitivity, fat suppression, and anatomical plane.
- `train_series/<StudyInstanceUID>/<SeriesInstanceUID>/<SOPInstanceUID>.dcm`: DICOM slices.
- The scoring test set contains approximately 1,300 studies and replaces the small example test set at runtime.

MRI intensity, orientation, resolution, compression, sequence length, scanner protocol, and site distribution vary across studies.

The reports can be ambiguous or internally inconsistent. The host states that the reviewed labels were assigned independently by two musculoskeletal radiologists with a third reader resolving disagreements ([discussion 733491](https://www.kaggle.com/competitions/rsna-knee-abnormality-detection/discussion/733491)). Report-derived labels should therefore be treated as noisy supervision rather than ground truth.

## Evaluation

The score is the unweighted mean of the twelve per-target ROC AUC values:

```text
Final Score = (1 / 12) * sum(AUC_i for i in 1..12)
```

The required output columns are:

```text
StudyInstanceUID,ACL,MCL,Medial Meniscus,Lateral Meniscus,Medial OA,Lateral OA,PF OA,Effusion,Synovitis,Baker's,Contusion,Fracture
```

## Submission constraints

- Notebook-only submissions.
- CPU or GPU runtime must not exceed 9 hours.
- Internet access must be disabled.
- Publicly and freely available external data and pretrained models are allowed.
- The output file must be named `submission.csv`.
- Up to five submissions per day and two selected final submissions.

The final submission deadline is 2026-10-22 23:59 UTC. Always recheck the live competition pages before relying on dates or limits.

## Data policy

The competition data is governed by the competition rules and MIRA data license. This repository does not redistribute the supplied CSV files, DICOM studies, radiology reports, or other competition data.
