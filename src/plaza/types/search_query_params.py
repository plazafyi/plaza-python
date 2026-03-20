# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SearchQueryParams"]


class SearchQueryParams(TypedDict, total=False):
    q: Required[str]
    """Search query string"""

    cursor: str
    """Cursor for pagination"""

    format: str
    """Response format: json (default), geojson, csv, ndjson"""

    limit: int
    """Maximum results (default 25, max 100)"""

    output_fields: Annotated[str, PropertyInfo(alias="output[fields]")]
    """Comma-separated property fields to include"""

    output_include: Annotated[str, PropertyInfo(alias="output[include]")]
    """Extra computed fields: bbox, distance, center"""

    output_precision: Annotated[int, PropertyInfo(alias="output[precision]")]
    """Coordinate decimal precision (1-15, default 7)"""

    output_sort: Annotated[str, PropertyInfo(alias="output[sort]")]
    """Sort by: distance, name, osm_id"""
