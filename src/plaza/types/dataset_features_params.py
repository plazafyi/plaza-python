# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DatasetFeaturesParams"]


class DatasetFeaturesParams(TypedDict, total=False):
    cursor: str
    """Cursor for pagination"""

    format: str
    """Response format: json (default), geojson, csv, ndjson"""

    limit: int
    """Maximum results"""

    output_buffer: Annotated[float, PropertyInfo(alias="output[buffer]")]
    """Buffer geometry by meters"""

    output_centroid: Annotated[bool, PropertyInfo(alias="output[centroid]")]
    """Replace geometry with centroid"""

    output_fields: Annotated[str, PropertyInfo(alias="output[fields]")]
    """Comma-separated property fields to include"""

    output_geometry: Annotated[bool, PropertyInfo(alias="output[geometry]")]
    """Include geometry (default true)"""

    output_include: Annotated[str, PropertyInfo(alias="output[include]")]
    """Extra computed fields: bbox, distance, center"""

    output_precision: Annotated[int, PropertyInfo(alias="output[precision]")]
    """Coordinate decimal precision (1-15, default 7)"""

    output_simplify: Annotated[float, PropertyInfo(alias="output[simplify]")]
    """Simplify geometry tolerance in meters"""

    output_sort: Annotated[str, PropertyInfo(alias="output[sort]")]
    """Sort by: distance, name, osm_id"""
