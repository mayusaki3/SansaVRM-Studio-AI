"""
SansaVRM Studio AI
Copyright Risk Assessment PoC

This module provides a minimal local-only copyright
risk assessment implementation.
"""

from typing import Dict, List

KNOWN_IP_TERMS = {
    "mario",
    "pokemon",
    "pikachu",
    "gundam",
    "disney",
}



def contains_known_ip(prompt: str) -> bool:
    """
    Check whether prompt contains known IP terms.
    """

    lower = prompt.lower()

    return any(term in lower for term in KNOWN_IP_TERMS)



def assess_risk(data: Dict) -> Dict:
    """
    Perform minimal copyright risk assessment.

    Args:
        data: Input metadata.

    Returns:
        Assessment result.
    """

    prompt = data.get("prompt", "")
    reference_candidates: List[str] = data.get(
        "reference_candidates", []
    )
    source_images = data.get("source_images", [])

    review_required = False
    reasons = []
    recommendations = []
    insufficient_evidence = []

    if contains_known_ip(prompt):
        review_required = True
        reasons.append("known_ip_term_detected")
        recommendations.append("revise_prompt")

    if reference_candidates:
        review_required = True
        reasons.append("reference_candidates_present")

    for source_image in source_images:
        if source_image.get("license") == "unknown":
            review_required = True
            reasons.append("unknown_source_license")
            recommendations.append("verify_source_license")

    if not reference_candidates:
        insufficient_evidence.append(
            "reference_candidates_not_provided"
        )

    return {
        "review_required": review_required,
        "matched_reasons": reasons,
        "recommended_actions": list(set(recommendations)),
        "insufficient_evidence": insufficient_evidence,
        "limitations": [
            "image similarity not implemented"
        ],
        "local_processing": True,
        "external_request_count": 0,
    }
