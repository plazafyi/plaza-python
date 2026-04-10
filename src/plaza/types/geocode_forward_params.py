# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .point_geometry_param import PointGeometryParam

__all__ = ["GeocodeForwardParams"]


class GeocodeForwardParams(TypedDict, total=False):
    q: Required[str]
    """Address or place name to geocode"""

    format: str
    """Response format: json (default), geojson, csv, ndjson"""

    country_code: Optional[str]
    """ISO 3166-1 alpha-2 country code to restrict results"""

    focus: Optional[PointGeometryParam]
    """GeoJSON Point geometry per RFC 7946.

    Coordinates use [longitude, latitude] order. Optional third element is altitude
    in meters.
    """

    lang: Optional[str]
    """Preferred response language (ISO 639-1)"""

    layer: Optional[str]
    """Filter by result layer (e.g. `address`, `place`, `poi`)"""

    limit: Optional[int]
    """Maximum number of results (default: 5, max: 50)"""
