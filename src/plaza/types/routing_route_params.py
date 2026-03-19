# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .geo_json_geometry_param import GeoJsonGeometryParam

__all__ = ["RoutingRouteParams"]


class RoutingRouteParams(TypedDict, total=False):
    destination: Required[GeoJsonGeometryParam]
    """Destination point (GeoJSON Point geometry)"""

    origin: Required[GeoJsonGeometryParam]
    """Origin point (GeoJSON Point geometry)"""

    mode: Literal["auto", "foot", "bicycle"]
