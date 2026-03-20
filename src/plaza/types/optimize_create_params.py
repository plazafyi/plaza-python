# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["OptimizeCreateParams", "Waypoint"]


class OptimizeCreateParams(TypedDict, total=False):
    waypoints: Required[Iterable[Waypoint]]
    """Waypoints to visit in optimized order (2-50 points)"""

    format: str
    """Response format: json (default), geojson, csv, ndjson"""

    mode: Literal["auto", "foot", "bicycle"]
    """Travel mode (default: `auto`)"""

    roundtrip: bool
    """Whether the route should return to the starting waypoint (default: true)"""


class Waypoint(TypedDict, total=False):
    """Geographic coordinate as a JSON object with `lat` and `lng` fields."""

    lat: Required[float]
    """Latitude in decimal degrees (-90 to 90)"""

    lng: Required[float]
    """Longitude in decimal degrees (-180 to 180)"""
