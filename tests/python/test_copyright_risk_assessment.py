"""
Unit tests for copyright risk assessment.
"""

import unittest

from src.python.copyright_risk_assessment import assess_risk


class TestCopyrightRiskAssessment(unittest.TestCase):
    """Copyright risk assessment tests."""

    def test_known_ip_prompt(self):
        """TC-001 known IP prompt."""

        result = assess_risk(
            {
                "prompt": "Mario style character"
            }
        )

        self.assertTrue(result["review_required"])
        self.assertIn(
            "revise_prompt",
            result["recommended_actions"],
        )

    def test_reference_candidates(self):
        """TC-002 reference candidates."""

        result = assess_risk(
            {
                "prompt": "fantasy mage",
                "reference_candidates": [
                    "ExistingCharacterA"
                ],
            }
        )

        self.assertTrue(result["review_required"])

    def test_unknown_license(self):
        """TC-003 unknown source license."""

        result = assess_risk(
            {
                "source_images": [
                    {
                        "path": "sample.png",
                        "license": "unknown",
                    }
                ]
            }
        )

        self.assertIn(
            "verify_source_license",
            result["recommended_actions"],
        )

    def test_insufficient_evidence(self):
        """TC-004 insufficient evidence."""

        result = assess_risk(
            {
                "prompt": "original fantasy character"
            }
        )

        self.assertTrue(
            len(result["insufficient_evidence"]) > 0
        )

    def test_local_only_behavior(self):
        """TC-006 local-only behavior."""

        result = assess_risk({})

        self.assertEqual(
            result["external_request_count"],
            0,
        )


if __name__ == "__main__":
    unittest.main()
