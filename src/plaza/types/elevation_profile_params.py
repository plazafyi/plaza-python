# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .line_string_geometry_param import LineStringGeometryParam

__all__ = ["ElevationProfileParams"]


class ElevationProfileParams(TypedDict, total=False):
    geometry: Required[LineStringGeometryParam]
    """GeoJSON LineString geometry per RFC 7946.

    An ordered sequence of two or more positions.
    """
