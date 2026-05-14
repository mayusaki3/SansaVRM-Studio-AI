"""
SansaVRM Studio AI
Local Server PoC
"""

from dataclasses import asdict

from fastapi import FastAPI

from src.python.project_workspace import (
    ProjectWorkspace,
)
from src.python.workflow_engine import WorkflowEngine


app = FastAPI()

workspace = ProjectWorkspace(
    project_id="prj-demo",
    project_name="demo_project",
    schema_version="0.1.0",
    local_only_default=True,
)

engine = WorkflowEngine(workspace)


@app.get("/api/health")
def health():
    """Health check endpoint."""

    return {
        "status": "ok"
    }


@app.get("/api/project")
def project_summary():
    """Project summary endpoint."""

    return {
        "project_id": workspace.project_id,
        "project_name": workspace.project_name,
        "schema_version": workspace.schema_version,
        "artifact_count": len(workspace.artifacts),
        "workflow_run_count": len(
            workspace.workflow_runs
        ),
    }


@app.get("/api/artifacts")
def artifacts():
    """Artifact registry endpoint."""

    return {
        "artifacts": [
            asdict(a)
            for a in workspace.artifacts.values()
        ]
    }


@app.get("/api/workflow-runs")
def workflow_runs():
    """Workflow run endpoint."""

    return {
        "workflow_runs": [
            asdict(r)
            for r in workspace.workflow_runs.values()
        ]
    }


@app.get("/api/workflow-graph")
def workflow_graph():
    """Workflow dependency graph endpoint."""

    return {
        "dependency_graph": {
            k: asdict(v)
            for k, v in engine.dependency_graph.items()
        }
    }
