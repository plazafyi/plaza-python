# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RoutingIsochroneParams"]


class RoutingIsochroneParams(TypedDict, total=False):
    lat: Required[float]
    """Latitude"""

    lng: Required[float]
    """Longitude"""

    time: Required[float]
    """Travel time in seconds (1-7200)"""

    format: str
    """Response format: json (default), geojson, csv, ndjson"""

    mode: str
    """Travel mode (auto, foot, bicycle)"""

    output_fields: Annotated[str, PropertyInfo(alias="output[fields]")]
    """Comma-separated property fields to include"""

    output_geometry: Annotated[bool, PropertyInfo(alias="output[geometry]")]
    """Include geometry (default true)"""

    output_include: Annotated[str, PropertyInfo(alias="output[include]")]
    """Extra computed fields: bbox, center"""

    output_precision: Annotated[int, PropertyInfo(alias="output[precision]")]
    """Coordinate decimal precision (1-15, default 7)"""

    output_simplify: Annotated[float, PropertyInfo(alias="output[simplify]")]
    """Simplify geometry tolerance in meters"""
