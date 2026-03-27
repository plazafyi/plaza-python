# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .geo_json_geometry_param import GeoJsonGeometryParam

__all__ = ["RoutingMatrixParams"]


class RoutingMatrixParams(TypedDict, total=False):
    destinations: Required[GeoJsonGeometryParam]
    """Destination points (GeoJSON MultiPoint geometry)"""

    origins: Required[GeoJsonGeometryParam]
    """Origin points (GeoJSON MultiPoint geometry)"""

    mode: Literal["auto", "foot", "bicycle"]
    """Travel mode"""
