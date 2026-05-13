"""
Unit tests for decomposition schema validator.
"""

import unittest

from src.python.decomposition_schema import (
    ValidationError,
    validate_decomposition_schema,
)


class TestDecompositionSchema(unittest.TestCase):
    """Decomposition schema validator tests."""

    def test_valid_schema(self):
        """TC-DEC-001 valid schema."""

        result = validate_decomposition_schema(
            {
                "asset_type": "humanoid_character",
                "layers": [
                    {
                        "layer_id": "body",
                        "layer_type": "base_structure",
                        "source": "visible",
                    }
                ],
            }
        )

        self.assertTrue(result["success"])

    def test_invalid_asset_type(self):
        """TC-DEC-002 invalid asset type."""

        with self.assertRaises(ValidationError):
            validate_decomposition_schema(
                {
                    "asset_type": "unknown_asset_type",
                    "layers": [],
                }
            )

    def test_inferred_source(self):
        """TC-DEC-003 inferred source."""

        result = validate_decomposition_schema(
            {
                "asset_type": "mech",
                "layers": [
                    {
                        "layer_id": "inner_frame",
                        "layer_type": "internal_mechanism",
                        "source": "inferred",
                    }
                ],
            }
        )

        self.assertTrue(result["success"])

    def test_duplicated_layer_id(self):
        """TC-DEC-004 duplicated layer id."""

        with self.assertRaises(ValidationError):
            validate_decomposition_schema(
                {
                    "asset_type": "animal",
                    "layers": [
                        {
                            "layer_id": "fur",
                            "layer_type": "outer_surface",
                            "source": "visible",
                        },
                        {
                            "layer_id": "fur",
                            "layer_type": "material_region",
                            "source": "visible",
                        },
                    ],
                }
            )


if __name__ == "__main__":
    unittest.main()
