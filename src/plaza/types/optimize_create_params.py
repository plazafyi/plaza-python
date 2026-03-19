# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .geo_json_geometry_param import GeoJsonGeometryParam

__all__ = ["OptimizeCreateParams"]


class OptimizeCreateParams(TypedDict, total=False):
    waypoints: Required[GeoJsonGeometryParam]
    """Waypoints to visit (GeoJSON MultiPoint geometry, minimum 2 points)"""

    mode: Literal["auto", "foot", "bicycle"]
    """Travel mode (default: auto)"""

    roundtrip: bool
    """Whether route returns to start (default: true)"""
