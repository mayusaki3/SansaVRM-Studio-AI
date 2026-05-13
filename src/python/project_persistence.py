"""
SansaVRM Studio AI
Project Persistence PoC
"""

import json
import zipfile
from pathlib import Path
from dataclasses import asdict

from src.python.project_workspace import (
    ProjectWorkspace,
)


class PersistenceError(Exception):
    """Raised when persistence fails."""



def save_project(
    workspace: ProjectWorkspace,
    root_path: str,
) -> None:
    """
    Save project workspace.
    """

    root = Path(root_path)

    (root / "workflow_runs").mkdir(
        parents=True,
        exist_ok=True,
    )

    (root / "artifacts").mkdir(
        parents=True,
        exist_ok=True,
    )

    project_json = {
        "project_id": workspace.project_id,
        "project_name": workspace.project_name,
        "schema_version": workspace.schema_version,
        "local_only_default": workspace.local_only_default,
        "artifact_registry_path": (
            "artifacts/artifact_registry.json"
        ),
        "workflow_runs_path": "workflow_runs",
    }

    with open(
        root / "project.json",
        "w",
        encoding="utf-8",
    ) as fp:
        json.dump(project_json, fp, indent=2)

    artifact_registry = {
        "schema_version": workspace.schema_version,
        "artifacts": [
            asdict(a)
            for a in workspace.artifacts.values()
        ],
    }

    with open(
        root / "artifacts" / "artifact_registry.json",
        "w",
        encoding="utf-8",
    ) as fp:
        json.dump(artifact_registry, fp, indent=2)

    for workflow_run in workspace.workflow_runs.values():
        with open(
            root
            / "workflow_runs"
            / f"{workflow_run.workflow_run_id}.json",
            "w",
            encoding="utf-8",
        ) as fp:
            json.dump(asdict(workflow_run), fp, indent=2)



def export_project_package(
    root_path: str,
    output_zip_path: str,
) -> None:
    """
    Export project package.
    """

    root = Path(root_path)

    with zipfile.ZipFile(
        output_zip_path,
        "w",
        zipfile.ZIP_DEFLATED,
    ) as zf:
        for path in root.rglob("*"):
            if path.is_file():
                zf.write(path, path.relative_to(root))



def validate_project_import(
    root_path: str,
) -> None:
    """
    Validate imported project.
    """

    root = Path(root_path)

    if not (root / "project.json").exists():
        raise PersistenceError(
            "project.json not found"
        )
