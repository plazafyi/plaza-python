# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["V1FindNearbyParams"]


class V1FindNearbyParams(TypedDict, total=False):
    lat: Required[float]
    """Latitude"""

    lng: Required[float]
    """Longitude"""

    limit: int
    """Maximum results (default 100, max 1000)"""

    radius: float
    """Search radius in meters (default 500)"""
