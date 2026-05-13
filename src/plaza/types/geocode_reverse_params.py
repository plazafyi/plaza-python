# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .point_geometry_param import PointGeometryParam

__all__ = ["GeocodeReverseParams"]


class GeocodeReverseParams(TypedDict, total=False):
    geometry: Required[PointGeometryParam]
    """GeoJSON Point geometry per RFC 7946.

    Coordinates use [longitude, latitude] order. Optional third element is altitude
    in meters.
    """

    format: str
    """Response format: json (default), geojson, csv, ndjson"""

    lang: Optional[str]
    """Preferred response language (ISO 639-1)"""

    limit: Optional[int]
    """Maximum number of results (default: 1, max: 50)"""

    radius: Optional[float]
    """Search radius in meters (default: 100)"""
