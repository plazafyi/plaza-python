# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GeocodeReverseParams"]


class GeocodeReverseParams(TypedDict, total=False):
    lat: Required[float]
    """Latitude"""

    lng: Required[float]
    """Longitude"""

    lang: str
    """Language code for localized names (e.g. en, de, fr)"""

    layer: str
    """Filter by layer: house or poi"""

    limit: int
    """Maximum results (default 1, max 20)"""

    radius: int
    """Search radius in meters (default 200, max 5000)"""
