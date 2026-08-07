from __future__ import annotations

import csv
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from validate_submission import (  # noqa: E402
    EXPECTED_COLUMNS,
    TARGET_COLUMNS,
    ValidationError,
    validate_submission,
)


def write_csv(path: Path, header: list[str], rows: list[list[str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)


class ValidateSubmissionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.submission_path = self.root / "submission.csv"
        self.test_csv_path = self.root / "test.csv"
        self.study_ids = ["study-a", "study-b"]
        write_csv(
            self.test_csv_path,
            ["StudyInstanceUID"],
            [[study_id] for study_id in self.study_ids],
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write_submission(self, ids: list[str], value: str = "0.5") -> None:
        rows = [[study_id, *([value] * len(TARGET_COLUMNS))] for study_id in ids]
        write_csv(self.submission_path, EXPECTED_COLUMNS, rows)

    def test_valid_submission(self) -> None:
        self.write_submission(self.study_ids)
        self.assertEqual(
            validate_submission(self.submission_path, self.test_csv_path), 2
        )

    def test_rejects_out_of_range_probability(self) -> None:
        self.write_submission(self.study_ids, value="1.01")
        with self.assertRaisesRegex(ValidationError, "outside"):
            validate_submission(self.submission_path, self.test_csv_path)

    def test_rejects_wrong_study_order(self) -> None:
        self.write_submission(list(reversed(self.study_ids)))
        with self.assertRaisesRegex(ValidationError, "order differs"):
            validate_submission(self.submission_path, self.test_csv_path)


if __name__ == "__main__":
    unittest.main()
