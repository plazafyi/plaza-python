# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["LineStringGeometryParam"]


class LineStringGeometryParam(TypedDict, total=False):
    """GeoJSON LineString geometry per RFC 7946.

    An ordered sequence of two or more positions.
    """

    coordinates: Required[Iterable[Iterable[float]]]
    """Array of [lng, lat] or [lng, lat, alt] positions"""

    type: Required[Literal["LineString"]]
