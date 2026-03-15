# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GeocodeAutocompleteParams"]


class GeocodeAutocompleteParams(TypedDict, total=False):
    q: Required[str]
    """Partial address query"""

    lat: float
    """Focus latitude"""

    limit: int
    """Maximum results (default 10, max 20)"""

    lng: float
    """Focus longitude"""
