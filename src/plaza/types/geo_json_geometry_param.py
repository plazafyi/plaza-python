# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["GeoJsonGeometryParam"]


class GeoJsonGeometryParam(TypedDict, total=False):
    coordinates: Required[
        Union[
            Iterable[float],
            Iterable[Iterable[float]],
            Iterable[Iterable[Iterable[float]]],
            Iterable[Iterable[Iterable[Iterable[float]]]],
        ]
    ]
    """GeoJSON coordinates array (nesting depth varies by geometry type)"""

    type: Required[Literal["Point", "LineString", "Polygon", "MultiPoint", "MultiLineString", "MultiPolygon"]]
