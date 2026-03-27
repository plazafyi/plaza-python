# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .geo_json_geometry_param import GeoJsonGeometryParam

__all__ = ["MapMatchMatchParams"]


class MapMatchMatchParams(TypedDict, total=False):
    trace: Required[GeoJsonGeometryParam]
    """GPS trace (GeoJSON LineString geometry)"""

    radiuses: Optional[Iterable[float]]
    """Search radius per coordinate in meters (optional, default 50)"""
