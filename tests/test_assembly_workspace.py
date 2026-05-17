"""Assembly workspace tests."""

import pytest

from src.python.assembly_workspace import (
    AssemblyWorkspace,
)


def test_select_component() -> None:
    """ASM-001: select allowed component."""

    workspace = AssemblyWorkspace(
        workspace_id="assembly-001"
    )

    workspace.select_component(
        slot_name="body",
        component_id="body-001",
        source_sansavrm="SansaVRM_A",
        assembly_allowed=True,
    )

    assert "body" in workspace.selected_components


def test_select_denied_component() -> None:
    """ASM-002: denied component selection."""

    workspace = AssemblyWorkspace(
        workspace_id="assembly-002"
    )

    with pytest.raises(ValueError):
        workspace.select_component(
            slot_name="hair",
            component_id="hair-001",
            source_sansavrm="SansaVRM_B",
            assembly_allowed=False,
        )


def test_build_provenance_graph() -> None:
    """ASM-003: provenance graph generation."""

    workspace = AssemblyWorkspace(
        workspace_id="assembly-003"
    )

    workspace.select_component(
        slot_name="body",
        component_id="body-001",
        source_sansavrm="SansaVRM_A",
        assembly_allowed=True,
    )

    workspace.select_component(
        slot_name="clothing",
        component_id="clothing-001",
        source_sansavrm="SansaVRM_C",
        assembly_allowed=True,
    )

    graph = workspace.build_provenance_graph()

    assert graph["body"]["source_sansavrm"] == "SansaVRM_A"
    assert graph["clothing"]["source_sansavrm"] == "SansaVRM_C"


def test_add_conflict() -> None:
    """ASM-004: conflict diagnostics."""

    workspace = AssemblyWorkspace(
        workspace_id="assembly-004"
    )

    workspace.add_conflict(
        conflict_type="commercial_conflict",
        message="commercial policy conflict",
        source_components=[
            "body-001",
            "hair-001",
        ],
    )

    assert len(workspace.conflicts) == 1
