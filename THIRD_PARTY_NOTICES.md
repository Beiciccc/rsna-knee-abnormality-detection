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

## RSNA Knee Research Tony-Sakhawat V1

This repository includes an adapted, zero-output inference notebook derived from two
public Kaggle notebooks released under the Apache License 2.0.

### Tony Li — RSNA Knee infer, Version 1

- **Author:** Tony Li (`tonylica` on Kaggle)
- **Pinned version:** V1, `scriptVersionId=340809629`
- **Source:** https://www.kaggle.com/code/tonylica/rsna-knee-infer?scriptVersionId=340809629
- **Pinned executable-code SHA-256:** `9c460f1f1387f2c7e9bfcf26d24fb10663df80f8cdab4e738c50cb398b46fad7`
- **License:** Apache License 2.0
- **Contribution used:** checkpoint-compatible preprocessing, DINOv2 model, slot-attention
  head, and fold-rank inference.

### Sakhawat Hossen — Knee RSNA, Version 1

- **Author:** Sakhawat Hossen (`sakhawathossen` on Kaggle)
- **Pinned version:** V1, `scriptVersionId=340853917`
- **Source:** https://www.kaggle.com/code/sakhawathossen/knee-rsna?scriptVersionId=340853917
- **Pinned notebook SHA-256:** `fc5465a8b7bc1e36f693e29acf2216f1225c2a8f4278aed0f089252138346e28`
- **Pinned executable-code SHA-256:** `9ebc90c30036e11934da4e35d209033d6b927409c6cb717d0bf567daf36f3625`
- **License:** Apache License 2.0
- **Contribution used:** public notebook source, including overlapping-window test-time
  averaging and hybrid rank aggregation.

The submitted V1 source for `beicicc/rsna-knee-research-tony-sakhawat-v1` has notebook
SHA-256 `413886d8535f1f9f1849f9fa5c68f591346cbcbc1e4b3d8a4a9fc9a235076daf`,
metadata SHA-256 `1b2e7dde71f40537541f656b75a6bc74e1f2ae85c88b714b5633b86778c316b7`,
and executable-code SHA-256
`9ebc90c30036e11934da4e35d209033d6b927409c6cb717d0bf567daf36f3625`.
The public copy at
`notebooks/public/rsna-knee-research-tony-sakhawat-v1/research_tony_sakhawat_v1_0836.ipynb`
makes two documentation-only changes: it corrects the Tony V1 code hash in the provenance
cell and replaces one generic process term in an upstream attribution note with
`implementation`. Its executable code is unchanged. The corrected public notebook
SHA-256 is `90d0fb834db5259439de91d2515b306b63c527ec8591e7d87c626ad5d7225700`.

The Apache License 2.0 text is already provided in `LICENSES/Apache-2.0.txt`.
The external dependencies are referenced by their public Kaggle identifiers only:

- `metaresearch/dinov2/PyTorch/small/1` — Apache License 2.0.
- `tonylica/rsna2026-models/2` — Kaggle reports the license as `Unknown`.

No checkpoint, pretrained weight, model bundle, competition data, DICOM file, report,
generated prediction, or output CSV is redistributed. This is an inference-code release;
it does not claim end-to-end training reproducibility.

## RSNA Knee Research Prvsiyan V9 guarded reproduction

This repository includes a zero-output source release derived from public Apache-2.0
Kaggle notebooks.

### Prvsiyan — RSNA Knee: read the report, then the knee, Version 9

- **Pinned version:** V9, `scriptVersionId=340808178`
- **Source:** https://www.kaggle.com/code/prvsiyan/rsna-knee-read-the-report-then-the-knee?scriptVersionId=340808178
- **Pinned notebook SHA-256:** `37d6c51268dcab2b530701331db2f140971c841c66e2fb012b221949471ed460`
- **Pinned executable-code SHA-256:** `709d6a03a35e1897e68e7a2b09efa3a47a3961d01dd00e3a4c433133218d62cc`
- **License:** Apache License 2.0

### Pilkwang Kim — RSNA Knee baseline v1, Version 14

- **Pinned version:** V14, `scriptVersionId=340738955`
- **Source:** https://www.kaggle.com/code/pilkwang/rsna-knee-baseline-v1?scriptVersionId=340738955
- **Pinned notebook SHA-256:** `67e874fa121b2f163a090bf598815f00441789e1699772c78f96eaa1f5ba60be`
- **License:** Apache License 2.0
- **Attribution reason:** substantial contiguous source overlap was independently
  observed. This conservative credit does not assert an undocumented direct fork.

The validated project source is `beicicc/rsna-knee-research-prvsiyan-v9-safe-reproduction` V1,
`scriptVersionId=340921674`. Its submitted-source notebook SHA-256
is `fb899b2afa4b52f1560ef98b9b46fb4f733354fb2ca3e38bed51f1afb455b659`, executable-code SHA-256 is `8aac800581107ff84295c4854b46aa4c25d6d2fc1816555627fcaec1567ba62b`, and
executable AST SHA-256 is `853c48b85dba9c5a6585af51b5940bea8b7922f20caf05add1e7f5d9ade1a25f`. The zero-output public source has
notebook SHA-256 `146d68a8fc9696a03d602b5d307782f96d6b73c9cd5f83a814185789cd236ead`; only its first provenance markdown cell and
notebook-level release metadata differ from the validated source.

The runtime references `metaresearch/dinov2/PyTorch/small/1` and
`metaresearch/dinov2/PyTorch/base/1`, both Apache-2.0. No DINOv2 weight, competition CSV,
DICOM file, report, label table, generated prediction, or other runtime output is
redistributed.

## RSNA Knee Research Renta V5 guarded reproduction

This repository includes a zero-output derivative of Pilkwang V15 under the Apache
License 2.0 and credits Renta V5 for the target-pooling configuration.

### Pilkwang Kim — RSNA Knee baseline v1, Version 15

- **Author:** Pilkwang Kim (`pilkwang` on Kaggle)
- **Pinned version:** V15, `scriptVersionId=340906482`
- **Source:** https://www.kaggle.com/code/pilkwang/rsna-knee-baseline-v1?scriptVersionId=340906482
- **Pinned notebook SHA-256:** `b32a9155fcc73c519e75e78c08e07d30393efc591c2798a3e40ca92f39832bb8`
- **Pinned executable-code SHA-256:** `7412ee5106a6bacfdfaa35e30675377f8cf981b1ddcd6cbe23f512fc03690931`
- **Pinned executable AST SHA-256:** `bda094e029abfd2fa0bc24b9916bb6cb091c44c07f99b89c66b6577a81c58853`
- **License:** Apache License 2.0

### renta.k — Renta V5 target-pooling configuration

- **Kaggle account:** `renta0426`
- **Pinned version:** V5, `scriptVersionId=341057541`
- **Source:** https://www.kaggle.com/code/renta0426/rsna-knee-baseline-v1-fracture-tta-pool-probe?scriptVersionId=341057541
- **Pinned notebook SHA-256:** `88dd523c444013b9d8c13dc958d193cb19fd4d53f535356a1d6e36f6bbd9bec1`
- **Pinned executable-code SHA-256:** `f8e993b9c1950b7baf4ba1838268d516b3e4e1e77275d01905123361a12a0e72`
- **Pinned executable AST SHA-256:** `574919df4c061dc3f5d972d12dadd6c305b00d5b11c9b4950143e41ec0ec4da5`
- **Contribution used:** maximum-probability pooling across ten windows for Fracture and
  Contusion; probability-mean pooling for the other ten targets.

The validated project source is `beicicc/rsna-knee-research-renta-v5-safe-reproduction` V2,
`scriptVersionId=341145955`. Its source notebook SHA-256 is
`740740e0e6052170150cdc0d0d97ae2477baff57c0dced06002ddaee4fb92f29`, executable-code SHA-256 is `c05d18066e69e15bc5097850bb35605287e6b5efc0f070417c72f52960e7d7c9`, and
executable AST SHA-256 is `7f062d9491ed664a54e6da5ba5935e7332bd9cf6cbe9b687d9c7d397db709c76`. The zero-output public source has
notebook SHA-256 `6d582ad4c79fe944958b100566e67311f3a3967d55744e79c28575557e57bd7e`; only two markdown cells and notebook-level
release metadata differ from the validated source.

EXP004 V1 stopped during checkpoint validation without an ordinary output or submission.
The public weight package contains exactly two legitimate top-level payload variants:
17 files include an exact 12-target list and three omit that optional field. V2 accepts
only those variants, validates every present target list, and completed all 20 members
over all ten windows.

Runtime dependencies are referenced through immutable public Kaggle identifiers and are
not redistributed:

- `pilkwang/rsna-knee-weights/1` — CC0 1.0.
- `pilkwang/rsna-knee-llm-labels/1` — CC0 1.0.
- `pilkwang/pilkwang-public-dataset-for-notebooks-figures/22` — Apache License 2.0.
- `metaresearch/dinov2/PyTorch/small/1` — Apache License 2.0.

No checkpoint, pretrained weight, competition CSV, DICOM file, report, per-study label,
generated prediction, log, or other runtime output is redistributed.
