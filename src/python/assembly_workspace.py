"""
SansaVRM Studio AI
Assembly Workspace PoC

This module manages interactive assembly state.
"""

from dataclasses import dataclass, field


@dataclass
class SelectedComponent:
    """Selected component entry."""

    slot_name: str
    component_id: str
    source_sansavrm: str


@dataclass
class AssemblyConflict:
    """Assembly conflict diagnostics."""

    conflict_type: str
    message: str
    source_components: list[str] = field(default_factory=list)


@dataclass
class AssemblyWorkspace:
    """Assembly workspace state."""

    workspace_id: str
    selected_components: dict[str, SelectedComponent] = field(
        default_factory=dict
    )
    conflicts: list[AssemblyConflict] = field(
        default_factory=list
    )

    def select_component(
        self,
        slot_name: str,
        component_id: str,
        source_sansavrm: str,
        assembly_allowed: bool,
    ) -> None:
        """
        Select component for assembly slot.

        Args:
            slot_name: Assembly slot.
            component_id: Component ID.
            source_sansavrm: Source SansaVRM.
            assembly_allowed: Governance result.

        Raises:
            ValueError:
                If assembly is denied.
        """

        if assembly_allowed is False:
            raise ValueError(
                "assembly denied for component: "
                f"{component_id}"
            )

        self.selected_components[slot_name] = SelectedComponent(
            slot_name=slot_name,
            component_id=component_id,
            source_sansavrm=source_sansavrm,
        )

    def build_provenance_graph(self) -> dict:
        """Build provenance graph."""

        graph = {}

        for slot_name, component in (
            self.selected_components.items()
        ):
            graph[slot_name] = {
                "component_id": component.component_id,
                "source_sansavrm": component.source_sansavrm,
            }

        return graph

    def add_conflict(
        self,
        conflict_type: str,
        message: str,
        source_components: list[str],
    ) -> None:
        """Add assembly conflict."""

        self.conflicts.append(
            AssemblyConflict(
                conflict_type=conflict_type,
                message=message,
                source_components=source_components,
            )
        )
