# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ElevationLookupParams"]


class ElevationLookupParams(TypedDict, total=False):
    lat: float
    """Latitude (single point)"""

    lng: float
    """Longitude (single point)"""

    locations: str
    """Pipe-separated lng,lat pairs (batch)"""
