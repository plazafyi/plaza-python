# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MultiLineStringGeometryParam"]


class MultiLineStringGeometryParam(TypedDict, total=False):
    """GeoJSON MultiLineString geometry per RFC 7946.

    An array of LineString coordinate arrays.
    """

    coordinates: Required[Iterable[Iterable[Iterable[float]]]]
    """Array of LineString coordinate arrays"""

    type: Required[Literal["MultiLineString"]]
