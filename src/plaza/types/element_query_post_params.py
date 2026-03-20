# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ElementQueryPostParams"]


class ElementQueryPostParams(TypedDict, total=False):
    bbox: str
    """Legacy shorthand.

    Bounding box: south,west,north,east. Use spatial predicates (near, within,
    intersects) instead.
    """

    contains: str
    """Geometry that features must contain"""

    crosses: str
    """Geometry that features must cross"""

    cursor: str
    """Cursor for pagination"""

    h3: str
    """Legacy shorthand. H3 cell index. Use spatial predicates instead."""

    intersects: str
    """Geometry that features must intersect"""

    limit: int
    """Maximum results (default 100, max 10000)"""

    near: str
    """Point geometry for proximity search (lat,lng). Requires radius."""

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

    radius: float
    """Search radius in meters (for near) or buffer distance (for other predicates)"""

    touches: str
    """Geometry that features must touch"""

    type: str
    """Element types (comma-separated: node,way,relation)"""

    within: str
    """Geometry that features must be within"""
