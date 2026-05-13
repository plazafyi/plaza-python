# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PolygonGeometryParam"]


class PolygonGeometryParam(TypedDict, total=False):
    """GeoJSON Polygon geometry per RFC 7946.

    An array of linear rings where the first ring is the exterior boundary and subsequent rings are holes. Each ring must have at least 4 positions with the first and last being identical.
    """

    coordinates: Required[Iterable[Iterable[Iterable[float]]]]
    """Array of linear rings (first = exterior, rest = holes)"""

    type: Required[Literal["Polygon"]]
