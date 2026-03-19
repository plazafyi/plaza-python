# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ElementNearbyParams"]


class ElementNearbyParams(TypedDict, total=False):
    lat: Required[float]
    """Latitude (-90 to 90)"""

    lng: Required[float]
    """Longitude (-180 to 180)"""

    limit: int
    """Maximum results (default 20, max 100)"""

    radius: int
    """Search radius in meters (default 500, max 10000)"""
