"""
Unit tests for workflow engine.
"""

import unittest

from src.python.project_workspace import (
    Artifact,
    ProjectWorkspace,
    ValidationError,
    WorkflowRun,
    WorkflowStep,
)
from src.python.workflow_engine import WorkflowEngine


class TestWorkflowEngine(unittest.TestCase):
    """Workflow engine tests."""

    def setUp(self):
        """Setup workspace."""

        self.workspace = ProjectWorkspace(
            project_id="prj-001",
            project_name="sample",
            schema_version="0.1.0",
            local_only_default=True,
        )

        self.engine = WorkflowEngine(self.workspace)

    def test_missing_input_artifact(self):
        """TC-WE-001 missing input artifact."""

        workflow_run = WorkflowRun(
            workflow_run_id="run-001",
            workflow_type="decomposition",
            status="running",
            local_only=True,
        )

        step = WorkflowStep(
            step_id="step-001",
            step_type="decomposition",
            status="pending",
            input_artifacts=["missing-artifact"],
        )

        output_artifact = Artifact(
            artifact_id="artifact-001",
            artifact_type="decomposition_result",
            path="artifacts/test.json",
        )

        with self.assertRaises(ValidationError):
            self.engine.execute_step(
                workflow_run,
                step,
                output_artifact,
            )

    def test_dependency_graph_update(self):
        """TC-WE-002 dependency graph update."""

        source_artifact = Artifact(
            artifact_id="artifact-source-001",
            artifact_type="source_image",
            path="artifacts/source.png",
        )

        self.workspace.register_artifact(source_artifact)

        workflow_run = WorkflowRun(
            workflow_run_id="run-001",
            workflow_type="decomposition",
            status="running",
            local_only=True,
        )

        step = WorkflowStep(
            step_id="step-001",
            step_type="decomposition",
            status="pending",
            input_artifacts=["artifact-source-001"],
        )

        output_artifact = Artifact(
            artifact_id="artifact-decomp-001",
            artifact_type="decomposition_result",
            path="artifacts/decomp.json",
        )

        self.engine.execute_step(
            workflow_run,
            step,
            output_artifact,
        )

        self.assertIn(
            "artifact-decomp-001",
            self.engine.dependency_graph,
        )

    def test_rerun_generates_new_artifact(self):
        """TC-WE-003 rerun artifact generation."""

        source_artifact = Artifact(
            artifact_id="artifact-source-001",
            artifact_type="source_image",
            path="artifacts/source.png",
        )

        self.workspace.register_artifact(source_artifact)

        workflow_run = WorkflowRun(
            workflow_run_id="run-001",
            workflow_type="decomposition",
            status="running",
            local_only=True,
        )

        original_step = WorkflowStep(
            step_id="step-001",
            step_type="decomposition",
            status="completed",
            input_artifacts=["artifact-source-001"],
        )

        rerun_step = WorkflowStep(
            step_id="step-002",
            step_type="decomposition",
            status="pending",
            input_artifacts=["artifact-source-001"],
        )

        rerun_artifact = Artifact(
            artifact_id="artifact-decomp-002",
            artifact_type="decomposition_result",
            path="artifacts/decomp2.json",
        )

        self.engine.rerun_step(
            workflow_run,
            original_step,
            rerun_step,
            rerun_artifact,
        )

        self.assertIn(
            "artifact-decomp-002",
            self.workspace.artifacts,
        )


if __name__ == "__main__":
    unittest.main()
