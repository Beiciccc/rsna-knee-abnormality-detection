# RSNA Knee — Renta V5 guarded reproduction

Zero-output Apache-2.0 source release of the 20-member DINOv2-small rank ensemble
evaluated as EXP004.

- Validated source: `beicicc/rsna-knee-research-renta-v5-safe-reproduction` V2,
  `scriptVersionId=341145955`.
- Public source: V3, `scriptVersionId=341169759`.
- Submitted-source notebook SHA-256: `740740e0e6052170150cdc0d0d97ae2477baff57c0dced06002ddaee4fb92f29`.
- Executable-code SHA-256: `c05d18066e69e15bc5097850bb35605287e6b5efc0f070417c72f52960e7d7c9`.
- Executable AST SHA-256: `7f062d9491ed664a54e6da5ba5935e7332bd9cf6cbe9b687d9c7d397db709c76`.
- Validated output SHA-256: `78f0499655c92a0de5486b15c69e546e269e9def647e0d7ea3ec11a16d66ee89`.
- Public source notebook SHA-256: `6d582ad4c79fe944958b100566e67311f3a3967d55744e79c28575557e57bd7e`.

The exact Renta V5 rule takes the maximum probability across ten overlapping windows for
Fracture and Contusion and retains probability-mean pooling for the other ten targets.
Each target is then rank-averaged over 20 members. EXP004 V1 exposed two legitimate
checkpoint payload variants: 17 files include the exact target list and three omit that
optional field. V2 accepts only those two exact schemas, verifies the target list when
present, and retains the tensor, recipe, identity, and fingerprint checks. V2 completed
all 20 members over all ten windows.

The public notebook differs from the validated V2 source only in two markdown cells and
notebook-level release metadata. Executable code is unchanged. Pilkwang V15 source and the
Renta V5 configuration are credited in the notebook and repository notice. The CC0 weight
and label datasets and Apache-2.0 figures and DINOv2-small model are referenced through
their public Kaggle identifiers only. No competition data, report, DICOM file, label row,
prediction CSV, checkpoint, or model weight is included.
