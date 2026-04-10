# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MultiPointGeometryParam"]


class MultiPointGeometryParam(TypedDict, total=False):
    """GeoJSON MultiPoint geometry per RFC 7946. An array of positions."""

    coordinates: Required[Iterable[Iterable[float]]]
    """Array of [lng, lat] or [lng, lat, alt] positions"""

    type: Required[Literal["MultiPoint"]]
