"""
Unit tests for project workspace.
"""

import unittest

from src.python.project_workspace import (
    Artifact,
    ProjectWorkspace,
    ValidationError,
    WorkflowRun,
    WorkflowStep,
)


class TestProjectWorkspace(unittest.TestCase):
    """Project workspace tests."""

    def test_register_workflow_run(self):
        """TC-PROJ-002 workflow run registration."""

        workspace = ProjectWorkspace(
            project_id="prj-001",
            project_name="sample",
            schema_version="0.1.0",
            local_only_default=True,
        )

        workflow_run = WorkflowRun(
            workflow_run_id="run-001",
            workflow_type="ai_preprocess",
            status="completed",
            local_only=True,
        )

        workspace.register_workflow_run(workflow_run)

        self.assertIn("run-001", workspace.workflow_runs)

    def test_invalid_status(self):
        """TC-SCHEMA-004 invalid status."""

        workflow_run = WorkflowRun(
            workflow_run_id="run-001",
            workflow_type="ai_preprocess",
            status="invalid_status",
            local_only=True,
        )

        with self.assertRaises(ValidationError):
            workflow_run.validate()

    def test_artifact_registration(self):
        """Artifact registry test."""

        workspace = ProjectWorkspace(
            project_id="prj-001",
            project_name="sample",
            schema_version="0.1.0",
            local_only_default=True,
        )

        artifact = Artifact(
            artifact_id="artifact-001",
            artifact_type="source_image",
            path="artifacts/source/test.png",
        )

        workspace.register_artifact(artifact)

        self.assertIn("artifact-001", workspace.artifacts)

    def test_workflow_step_validation(self):
        """Workflow step validation."""

        step = WorkflowStep(
            step_id="step-001",
            step_type="decomposition",
            status="completed",
            input_artifacts=["artifact-input-001"],
            output_artifacts=["artifact-output-001"],
        )

        step.validate()


if __name__ == "__main__":
    unittest.main()
