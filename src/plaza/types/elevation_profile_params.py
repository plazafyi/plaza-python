# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .geo_json_geometry_param import GeoJsonGeometryParam

__all__ = ["ElevationProfileParams"]


class ElevationProfileParams(TypedDict, total=False):
    geometry: Required[GeoJsonGeometryParam]
    """Path to profile (GeoJSON LineString geometry, minimum 2 points)"""
