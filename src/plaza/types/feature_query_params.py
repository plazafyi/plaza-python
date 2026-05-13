# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .geometry_param import GeometryParam

__all__ = ["FeatureQueryParams"]


class FeatureQueryParams(TypedDict, total=False):
    cursor: str
    """Cursor for pagination"""

    format: str
    """Response format.

    json (default) returns paginated GeoJSON. geojson/csv/ndjson stream via chunked
    transfer encoding.
    """

    h3: str
    """Legacy shorthand. H3 cell index. Use spatial predicates instead."""

    limit: int
    """Maximum results (default 100, max 10000)"""

    type: str
    """Element types (comma-separated: node,way,relation)"""

    around: GeometryParam
    """GeoJSON Geometry object per RFC 7946.

    Discriminated union — the `type` field determines the coordinate structure.
    """

    contains: GeometryParam
    """GeoJSON Geometry object per RFC 7946.

    Discriminated union — the `type` field determines the coordinate structure.
    """

    crosses: GeometryParam
    """GeoJSON Geometry object per RFC 7946.

    Discriminated union — the `type` field determines the coordinate structure.
    """

    intersects: GeometryParam
    """GeoJSON Geometry object per RFC 7946.

    Discriminated union — the `type` field determines the coordinate structure.
    """

    not_contains: GeometryParam
    """GeoJSON Geometry object per RFC 7946.

    Discriminated union — the `type` field determines the coordinate structure.
    """

    not_intersects: GeometryParam
    """GeoJSON Geometry object per RFC 7946.

    Discriminated union — the `type` field determines the coordinate structure.
    """

    not_within: GeometryParam
    """GeoJSON Geometry object per RFC 7946.

    Discriminated union — the `type` field determines the coordinate structure.
    """

    radius: float
    """Search radius in meters.

    Required for `around`, optional buffer for other predicates.
    """

    touches: GeometryParam
    """GeoJSON Geometry object per RFC 7946.

    Discriminated union — the `type` field determines the coordinate structure.
    """

    within: GeometryParam
    """GeoJSON Geometry object per RFC 7946.

    Discriminated union — the `type` field determines the coordinate structure.
    """
