from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_SCRIPT = (
    PROJECT_ROOT
    / "notebooks"
    / "public"
    / "rsna-knee-submission-validator"
    / "rsna_knee_submission_validator.py"
)
SPEC = importlib.util.spec_from_file_location("public_validator", NOTEBOOK_SCRIPT)
assert SPEC is not None and SPEC.loader is not None
PUBLIC_VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PUBLIC_VALIDATOR)


class PublicNotebookTests(unittest.TestCase):
    def test_resolves_competitions_mount_layout(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            input_root = Path(temp_dir)
            competition_dir = (
                input_root / "competitions" / PUBLIC_VALIDATOR.COMPETITION_SLUG
            )
            competition_dir.mkdir(parents=True)
            (competition_dir / "test.csv").touch()
            (competition_dir / "sample_submission.csv").touch()

            self.assertEqual(
                PUBLIC_VALIDATOR.resolve_competition_dir(input_root),
                competition_dir,
            )

    def test_rejects_missing_competition_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            with self.assertRaisesRegex(FileNotFoundError, "inspected"):
                PUBLIC_VALIDATOR.resolve_competition_dir(Path(temp_dir))


if __name__ == "__main__":
    unittest.main()
