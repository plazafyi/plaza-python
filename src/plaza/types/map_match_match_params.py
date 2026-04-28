# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .line_string_geometry_param import LineStringGeometryParam

__all__ = ["MapMatchMatchParams"]


class MapMatchMatchParams(TypedDict, total=False):
    geometry: Required[LineStringGeometryParam]
    """GeoJSON LineString geometry per RFC 7946.

    An ordered sequence of two or more positions.
    """

    radiuses: Optional[Iterable[float]]
    """Search radius per coordinate in meters.

    Must have the same length as the geometry coordinates or be omitted entirely.
    Default: 50m per point.
    """
