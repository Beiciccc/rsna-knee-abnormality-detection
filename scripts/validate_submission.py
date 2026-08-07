#!/usr/bin/env python3
"""Validate an RSNA Knee Abnormality Detection submission file."""

from __future__ import annotations

import argparse
import csv
import math
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


class ValidationError(ValueError):
    """Raised when a submission violates the expected contract."""


def _read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.is_file():
        raise ValidationError(f"File not found: {path}")

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValidationError(f"Missing CSV header: {path}")
        return list(reader.fieldnames), list(reader)


def _require_unique(values: Iterable[str], label: str) -> None:
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
    """Validate schema, identifiers, order, and probabilities; return row count."""

    if submission_path.name != "submission.csv":
        raise ValidationError("Competition output must be named submission.csv")

    submission_header, submission_rows = _read_rows(submission_path)
    if submission_header != EXPECTED_COLUMNS:
        raise ValidationError(
            "Submission columns must exactly match the official schema and order. "
            f"Expected {EXPECTED_COLUMNS}; found {submission_header}"
        )
    if not submission_rows:
        raise ValidationError("Submission contains no prediction rows")

    test_header, test_rows = _read_rows(test_csv_path)
    if "StudyInstanceUID" not in test_header:
        raise ValidationError("test.csv is missing StudyInstanceUID")
    if not test_rows:
        raise ValidationError("test.csv contains no study rows")

    submission_ids = [row["StudyInstanceUID"].strip() for row in submission_rows]
    test_ids = [row["StudyInstanceUID"].strip() for row in test_rows]
    if any(not study_id for study_id in submission_ids):
        raise ValidationError("Submission contains a blank StudyInstanceUID")
    if any(not study_id for study_id in test_ids):
        raise ValidationError("test.csv contains a blank StudyInstanceUID")

    _require_unique(submission_ids, "submission StudyInstanceUID values")
    _require_unique(test_ids, "test StudyInstanceUID values")
    if submission_ids != test_ids:
        missing = sorted(set(test_ids) - set(submission_ids))[:5]
        extra = sorted(set(submission_ids) - set(test_ids))[:5]
        if missing or extra:
            raise ValidationError(
                f"Study IDs do not match test.csv; missing={missing}, extra={extra}"
            )
        raise ValidationError("Study IDs match but row order differs from test.csv")

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
                    f"Row {row_number}, {column}: probability {probability} is outside [0, 1]"
                )

    return len(submission_rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("submission", type=Path, help="Path to submission.csv")
    parser.add_argument(
        "--test-csv",
        required=True,
        type=Path,
        help="Path to the matching runtime test.csv",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        row_count = validate_submission(args.submission, args.test_csv)
    except ValidationError as exc:
        print(f"INVALID: {exc}")
        return 1
    print(f"VALID: {row_count} studies, {len(TARGET_COLUMNS)} targets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
