# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .multi_point_geometry_param import MultiPointGeometryParam

__all__ = ["OptimizeCreateParams"]


class OptimizeCreateParams(TypedDict, total=False):
    waypoints: Required[MultiPointGeometryParam]
    """GeoJSON MultiPoint geometry per RFC 7946. An array of positions."""

    format: str
    """Response format: json (default), geojson, csv, ndjson"""

    mode: Literal["auto", "foot", "bicycle"]
    """Travel mode (default: `auto`)"""

    roundtrip: bool
    """Whether the route should return to the starting waypoint (default: true)"""
