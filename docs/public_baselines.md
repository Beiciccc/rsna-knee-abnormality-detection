# Public baseline reference

Snapshot verified on 2026-08-07. Scores and notebook versions can change; follow the links for the current state.

| Public notebook | Version | Public AUC | Runtime | License |
|---|---:|---:|---:|---|
| [RSNA Knee Baseline V1](https://www.kaggle.com/code/pilkwang/rsna-knee-baseline-v1) | V14 | 0.824 | 5,296 s, 2×T4 | Apache-2.0 |
| [DINOv2 at Meniscus Resolution](https://www.kaggle.com/code/wguesdon/rsna-knee-dinov2-at-meniscus-resolution) | V5 | 0.815 | 5,562 s, 2×T4 | Apache-2.0 |
| [Data Structure, EDA and Baseline](https://www.kaggle.com/code/romanrozen/rsna-knee-data-structure-eda-baseline) | V9 | 0.809 | 5,882 s, 2×T4 | Apache-2.0 |
| [Public 4-Fold DINOv2 V4](https://www.kaggle.com/code/hida1211/rsna-knee-public-4-fold-dinov2-v4) | V1 | 0.806 | 6,073 s, 2×T4 | Apache-2.0 |
| [DINOv2 Base Physical-Scale Soup](https://www.kaggle.com/code/fleongg/rsna-knee-dinov2-base-physical-scale-soup) | V5 | 0.768 | 7,231 s, 2×T4 | Apache-2.0 |

The strongest reproducible public reference in this snapshot is V14 at 0.824. Its main ingredients are:

- DINOv2-S image encoder with the last six blocks unfrozen.
- A fixed report-hash one-fifth holdout, with separate 224 px and 336 px single-model runs trained for ten epochs; the final submission uses the 336 px model.
- A 130 mm physical crop rendered at 336 px.
- Three adjacent slices per input slot and six sequence/anatomy slots.
- Public report-derived weak labels, with greater weight on the 58 reviewed studies.
- Backbone learning rate `8e-6`, head learning rate `1e-3`, and batch size 8.

The notebook's reported resolution comparison favored 336 px over 224 px on its holdout. The reviewed subset is very small, so validation results should be interpreted together with grouped out-of-fold checks and the public leaderboard.

## Data cautions

- Slice file names are identifiers, not an ordering guarantee. Geometry-aware ordering should use DICOM orientation and position, with `InstanceNumber` only as a fallback.
- Duplicate report text can leak weak-label information across random folds. Grouping by a normalized report hash is a safer validation split.
- Metadata-only validation can learn scanner or site identity. Scanner-grouped validation is useful as a shortcut diagnostic.
- The scoring test set has no reports, so text can supervise image training but cannot be required at inference.
- Runtime and memory estimates must use approximately 1,300 hidden test studies, not the three visible examples.
