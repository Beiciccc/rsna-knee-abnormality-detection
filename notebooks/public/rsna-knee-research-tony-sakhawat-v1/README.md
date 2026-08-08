# EXP002 — Tony/Sakhawat V1 inference anchor

This directory contains the zero-output public copy prepared from
`beicicc/rsna-knee-research-tony-sakhawat-v1`, V1. It preserves the submitted executable
code exactly while making two documentation-only changes before publication: correcting
Tony V1's provenance hash and replacing one generic process term in an upstream
attribution note with `implementation`.

## Pinned sources

- Tony Li, [RSNA Knee infer, V1](https://www.kaggle.com/code/tonylica/rsna-knee-infer?scriptVersionId=340809629),
  `scriptVersionId=340809629`, executable-code SHA-256
  `9c460f1f1387f2c7e9bfcf26d24fb10663df80f8cdab4e738c50cb398b46fad7`.
- Sakhawat Hossen, [Knee RSNA, V1](https://www.kaggle.com/code/sakhawathossen/knee-rsna?scriptVersionId=340853917),
  `scriptVersionId=340853917`, notebook SHA-256
  `fc5465a8b7bc1e36f693e29acf2216f1225c2a8f4278aed0f089252138346e28`,
  executable-code SHA-256
  `9ebc90c30036e11934da4e35d209033d6b927409c6cb717d0bf567daf36f3625`.

Both upstream notebooks are released under Apache-2.0. The submitted V1 notebook SHA-256
is `413886d8535f1f9f1849f9fa5c68f591346cbcbc1e4b3d8a4a9fc9a235076daf`; its metadata
SHA-256 is `1b2e7dde71f40537541f656b75a6bc74e1f2ae85c88b714b5633b86778c316b7`.
The documentation-corrected public notebook SHA-256 is
`90d0fb834db5259439de91d2515b306b63c527ec8591e7d87c626ad5d7225700`, and its executable
code remains `9ebc90c30036e11934da4e35d209033d6b927409c6cb717d0bf567daf36f3625`.

## Dependency and reproduction boundary

The notebook references `metaresearch/dinov2/PyTorch/small/1` under Apache-2.0 and the
external checkpoint dependency `tonylica/rsna2026-models/2`, whose Kaggle license is
reported as `Unknown`. Neither dependency is copied into this repository. No checkpoint,
pretrained weight, model bundle, competition data, DICOM content, report, or generated
prediction is included.

This release preserves inference code and attribution only. It does not provide the
training code, training recipe, or licensed training artifacts needed for an end-to-end
training reproduction, and it makes no such reproducibility claim. Official submission
facts are recorded in the repository ledgers only after the corresponding row is complete.

See the repository's `LICENSES/Apache-2.0.txt` and `THIRD_PARTY_NOTICES.md`.
