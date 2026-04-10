# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .point_geometry_param import PointGeometryParam

__all__ = ["RoutingIsochroneParams"]


class RoutingIsochroneParams(TypedDict, total=False):
    geometry: Required[PointGeometryParam]
    """GeoJSON Point geometry per RFC 7946.

    Coordinates use [longitude, latitude] order. Optional third element is altitude
    in meters.
    """

    time: Required[Iterable[int]]
    """Travel time budgets in seconds. Each value produces one contour polygon."""

    format: str
    """Response format: json (default), geojson, csv, ndjson"""

    mode: Literal["auto", "foot", "bicycle"]
    """Travel mode (default: `auto`)"""
