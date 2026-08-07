# SPDX-License-Identifier: MIT
"""Validate the official example submission and write submission.csv."""

from __future__ import annotations

import csv
import math
import shutil
from pathlib import Path
from typing import Iterable


TARGET_COLUMNS = [
    "ACL",
    "MCL",
    "Medial Meniscus",
    "Lateral Meniscus",
    "Medial OA",
    "Lateral OA",
    "PF OA",
    "Effusion",
    "Synovitis",
    "Baker's",
    "Contusion",
    "Fracture",
]
EXPECTED_COLUMNS = ["StudyInstanceUID", *TARGET_COLUMNS]
COMPETITION_SLUG = "rsna-knee-abnormality-detection"


class ValidationError(ValueError):
    """Raised when a submission violates the expected contract."""


def read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValidationError(f"Missing CSV header: {path}")
        return list(reader.fieldnames), list(reader)


def require_unique(values: Iterable[str], label: str) -> None:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    if duplicates:
        sample = ", ".join(sorted(duplicates)[:5])
        raise ValidationError(f"Duplicate {label}: {sample}")


def validate_submission(submission_path: Path, test_csv_path: Path) -> int:
    if submission_path.name != "submission.csv":
        raise ValidationError("Competition output must be named submission.csv")

    submission_header, submission_rows = read_rows(submission_path)
    if submission_header != EXPECTED_COLUMNS:
        raise ValidationError(
            f"Expected columns {EXPECTED_COLUMNS}; found {submission_header}"
        )
    if not submission_rows:
        raise ValidationError("Submission contains no prediction rows")

    test_header, test_rows = read_rows(test_csv_path)
    if "StudyInstanceUID" not in test_header:
        raise ValidationError("test.csv is missing StudyInstanceUID")

    submission_ids = [row["StudyInstanceUID"].strip() for row in submission_rows]
    test_ids = [row["StudyInstanceUID"].strip() for row in test_rows]
    if any(not study_id for study_id in submission_ids + test_ids):
        raise ValidationError("Blank StudyInstanceUID found")
    require_unique(submission_ids, "submission StudyInstanceUID values")
    require_unique(test_ids, "test StudyInstanceUID values")
    if submission_ids != test_ids:
        raise ValidationError("Submission IDs or row order differ from test.csv")

    for row_number, row in enumerate(submission_rows, start=2):
        for column in TARGET_COLUMNS:
            raw_value = row[column].strip()
            try:
                probability = float(raw_value)
            except ValueError as exc:
                raise ValidationError(
                    f"Row {row_number}, {column}: not a number ({raw_value!r})"
                ) from exc
            if not math.isfinite(probability):
                raise ValidationError(
                    f"Row {row_number}, {column}: probability is not finite"
                )
            if not 0.0 <= probability <= 1.0:
                raise ValidationError(
                    f"Row {row_number}, {column}: {probability} is outside [0, 1]"
                )

    return len(submission_rows)


def resolve_competition_dir(input_root: Path) -> Path:
    """Resolve both Kaggle competition mount layouts without a broad scan."""

    candidates = [
        input_root / COMPETITION_SLUG,
        input_root / "competitions" / COMPETITION_SLUG,
    ]
    for candidate in candidates:
        if (candidate / "test.csv").is_file() and (
            candidate / "sample_submission.csv"
        ).is_file():
            return candidate
    inspected = ", ".join(str(candidate) for candidate in candidates)
    raise FileNotFoundError(f"Competition files not found; inspected: {inspected}")


def main() -> None:
    competition_dir = resolve_competition_dir(Path("/kaggle/input"))
    test_csv = competition_dir / "test.csv"
    sample_submission = competition_dir / "sample_submission.csv"
    output_submission = Path("/kaggle/working/submission.csv")

    shutil.copyfile(sample_submission, output_submission)
    validated_rows = validate_submission(output_submission, test_csv)
    print(f"Input directory: {competition_dir}")
    print(f"VALID: {validated_rows} studies, {len(TARGET_COLUMNS)} targets")


if __name__ == "__main__":
    main()
