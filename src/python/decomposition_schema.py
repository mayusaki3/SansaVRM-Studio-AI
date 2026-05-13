"""
SansaVRM Studio AI
Decomposition Schema Validator PoC

This module provides a minimal local validator implementation
for decomposition schema structures.
"""

from typing import Dict, List

VALID_ASSET_TYPES = {
    "humanoid_character",
    "non_humanoid_character",
    "animal",
    "creature",
    "robot",
    "mech",
    "vehicle",
    "furniture",
    "building",
    "prop",
    "environment_asset",
}

VALID_LAYER_TYPES = {
    "base_structure",
    "outer_surface",
    "covering",
    "appendage",
    "accessory",
    "internal_mechanism",
    "movable_part",
    "hidden_part",
    "material_region",
    "effect_region",
}

VALID_SOURCES = {
    "visible",
    "hidden",
    "inferred",
    "generated",
    "author_verified",
}


class ValidationError(Exception):
    """Raised when decomposition schema validation fails."""



def validate_asset_type(asset_type: str) -> None:
    """
    Validate asset type.

    Args:
        asset_type: Asset type string.

    Raises:
        ValidationError: If asset type is unsupported.
    """

    if asset_type not in VALID_ASSET_TYPES:
        raise ValidationError(f"Unsupported asset_type: {asset_type}")



def validate_layers(layers: List[Dict]) -> None:
    """
    Validate decomposition layers.

    Args:
        layers: Layer list.

    Raises:
        ValidationError: If validation fails.
    """

    seen_ids = set()

    for layer in layers:
        layer_id = layer.get("layer_id")
        layer_type = layer.get("layer_type")
        source = layer.get("source")

        if layer_id in seen_ids:
            raise ValidationError(f"Duplicated layer_id: {layer_id}")

        seen_ids.add(layer_id)

        if layer_type not in VALID_LAYER_TYPES:
            raise ValidationError(
                f"Unsupported layer_type: {layer_type}"
            )

        if source not in VALID_SOURCES:
            raise ValidationError(
                f"Unsupported source: {source}"
            )



def validate_decomposition_schema(data: Dict) -> Dict:
    """
    Validate decomposition schema.

    Args:
        data: Schema data.

    Returns:
        Validation result dictionary.
    """

    validate_asset_type(data["asset_type"])
    validate_layers(data.get("layers", []))

    return {
        "success": True,
        "validated_asset_type": data["asset_type"],
        "layer_count": len(data.get("layers", [])),
    }
