"""
Unit tests for project persistence.
"""

import tempfile
import unittest
from pathlib import Path

from src.python.project_workspace import (
    ProjectWorkspace,
)
from src.python.project_persistence import (
    PersistenceError,
    export_project_package,
    save_project,
    validate_project_import,
)


class TestProjectPersistence(unittest.TestCase):
    """Project persistence tests."""

    def test_save_project(self):
        """TC-PERSIST-001 project save."""

        workspace = ProjectWorkspace(
            project_id="prj-001",
            project_name="sample",
            schema_version="0.1.0",
            local_only_default=True,
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            save_project(workspace, tmpdir)

            self.assertTrue(
                (Path(tmpdir) / "project.json").exists()
            )

    def test_export_project_package(self):
        """TC-PERSIST-004 export package."""

        workspace = ProjectWorkspace(
            project_id="prj-001",
            project_name="sample",
            schema_version="0.1.0",
            local_only_default=True,
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            save_project(workspace, tmpdir)

            output_zip = (
                Path(tmpdir)
                / "sample.svsa-project.zip"
            )

            export_project_package(
                tmpdir,
                str(output_zip),
            )

            self.assertTrue(output_zip.exists())

    def test_missing_project_json(self):
        """TC-PERSIST-006 missing project.json."""

        with tempfile.TemporaryDirectory() as tmpdir:
            with self.assertRaises(PersistenceError):
                validate_project_import(tmpdir)


if __name__ == "__main__":
    unittest.main()
