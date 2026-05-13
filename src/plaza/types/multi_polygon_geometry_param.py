# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MultiPolygonGeometryParam"]


class MultiPolygonGeometryParam(TypedDict, total=False):
    """GeoJSON MultiPolygon geometry per RFC 7946.

    An array of Polygon coordinate arrays.
    """

    coordinates: Required[Iterable[Iterable[Iterable[Iterable[float]]]]]
    """Array of Polygon coordinate arrays"""

    type: Required[Literal["MultiPolygon"]]
