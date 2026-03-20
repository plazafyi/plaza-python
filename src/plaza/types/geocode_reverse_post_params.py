# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GeocodeReversePostParams"]


class GeocodeReversePostParams(TypedDict, total=False):
    lang: str
    """Language code for localized names (e.g. en, de, fr)"""

    lat: float
    """Legacy shorthand. Latitude. Use near param instead."""

    layer: str
    """Filter by layer: house or poi"""

    limit: int
    """Maximum results (default 1, max 20)"""

    lng: float
    """Legacy shorthand. Longitude. Use near param instead."""

    near: str
    """Point geometry for reverse geocode (lat,lng or GeoJSON).

    Alternative to lat/lng params.
    """

    radius: int
    """Search radius in meters (default 200, max 5000)"""
