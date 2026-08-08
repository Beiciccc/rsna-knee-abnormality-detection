# Exp001 — Pilkwang V14 anchor

This directory contains the zero-output public snapshot of
`beicicc/rsna-knee-exp001-pilkwang-v14-anchor`, V2.

The notebook reproduces Pilkwang Kim's `RSNA Knee baseline v1`, V14
(`scriptVersionId=340738955`) as the first scored anchor for this project. V1 received a
Tesla P100 (`sm_60`) that was incompatible with the notebook's PyTorch build; the ordinary
run failed and no submission was made. V2 adds environment-only guards: it requires the
requested Tesla T4 (`sm_75`) before data I/O, verifies that the PyTorch build includes
that architecture, runs a CUDA forward/backward/optimizer preflight, and re-raises
runtime exceptions. The model and experiment settings are unchanged.

- Upstream source: https://www.kaggle.com/code/pilkwang/rsna-knee-baseline-v1?scriptVersionId=340738955
- Upstream SHA-256: `67e874fa121b2f163a090bf598815f00441789e1699772c78f96eaa1f5ba60be`
- Exp001 V1 SHA-256: `44e8be4c483a28432ed2a3e64170ad45839e3555d6f38cffdabe18d7c1f3dfdd`
- Exp001 V2 SHA-256: `53416002b264b4e53086466114a955905d224e735b1544bcb692e88c5e094a9c`
- Derivative Kaggle notebook: https://www.kaggle.com/code/beicicc/rsna-knee-exp001-pilkwang-v14-anchor
- License: Apache-2.0; see the repository's `LICENSES/Apache-2.0.txt` and
  `THIRD_PARTY_NOTICES.md`.

The notebook expects the competition input, the public weak-label dataset, the optional
public figure dataset, and the attached DINOv2 Small model listed in
`kernel-metadata.json`. None of those data or model artifacts is included here.

The V2 official submission reference and Public AUC are recorded in the repository's
experiment and public-score ledgers.
