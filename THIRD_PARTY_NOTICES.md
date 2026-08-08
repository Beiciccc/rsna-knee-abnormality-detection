# Third-Party Notices

## RSNA Knee baseline v1, version 14

This repository includes an adapted, zero-output copy of the following work:

- **Work:** RSNA Knee baseline v1
- **Author:** Pilkwang Kim (`pilkwang` on Kaggle)
- **Upstream notebook:** `pilkwang/rsna-knee-baseline-v1`
- **Pinned version:** V14, `scriptVersionId=340738955`
- **Source:** https://www.kaggle.com/code/pilkwang/rsna-knee-baseline-v1?scriptVersionId=340738955
- **Pinned notebook SHA-256:** `67e874fa121b2f163a090bf598815f00441789e1699772c78f96eaa1f5ba60be`
- **License:** Apache License 2.0

The Exp001 V2 derivative is published as
`notebooks/public/rsna-knee-exp001-pilkwang-v14-anchor/exp001_v14_anchor.ipynb`:

- **Kaggle notebook:** `beicicc/rsna-knee-exp001-pilkwang-v14-anchor`, V2
- **V1 notebook SHA-256:** `44e8be4c483a28432ed2a3e64170ad45839e3555d6f38cffdabe18d7c1f3dfdd`
- **V2 notebook SHA-256:** `53416002b264b4e53086466114a955905d224e735b1544bcb692e88c5e094a9c`

V1 was assigned a Tesla P100 with CUDA capability `sm_60`, which was incompatible with
the notebook's PyTorch build. The ordinary run failed and no submission was made.

V2 adds a prominent provenance cell, adapts the Kaggle owner, title, and code-file
metadata, requires the requested Tesla T4 (`sm_75`) before data I/O, checks that the
PyTorch build contains `sm_75`, runs a CUDA forward/backward/optimizer preflight, and
re-raises runtime exceptions. Relative to the pinned upstream notebook, 30 model and
experiment cells are unchanged and three code cells contain these environment-only
guards. The model and experiment settings are unchanged.

The Apache License 2.0 text is provided in `LICENSES/Apache-2.0.txt`. The pinned upstream
notebook contained no embedded copyright header or `NOTICE` file; this notice preserves
the observed author, work, version, source, license, and modification history.

Competition data, DICOM files, reports, per-study labels, generated predictions, model
weights, and the attached weak-label and figure datasets are not redistributed here.
Those inputs remain governed by their own terms and are referenced only through public
Kaggle identifiers in the notebook metadata.
