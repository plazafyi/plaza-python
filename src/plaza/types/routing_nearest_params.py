# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .point_geometry_param import PointGeometryParam

__all__ = ["RoutingNearestParams"]


class RoutingNearestParams(TypedDict, total=False):
    geometry: Required[PointGeometryParam]
    """GeoJSON Point geometry per RFC 7946.

    Coordinates use [longitude, latitude] order. Optional third element is altitude
    in meters.
    """

    radius: Optional[float]
    """Maximum search radius in meters (default: 100)"""
