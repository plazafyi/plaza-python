# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PointGeometryParam"]


class PointGeometryParam(TypedDict, total=False):
    """GeoJSON Point geometry per RFC 7946.

    Coordinates use [longitude, latitude] order. Optional third element is altitude in meters.
    """

    coordinates: Required[Iterable[float]]
    """[longitude, latitude] or [longitude, latitude, altitude]"""

    type: Required[Literal["Point"]]
