# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .point_geometry_param import PointGeometryParam

__all__ = ["RoutingMatrixParams"]


class RoutingMatrixParams(TypedDict, total=False):
    destinations: Required[Iterable[PointGeometryParam]]
    """Array of destination coordinates as GeoJSON Points (max 50)"""

    origins: Required[Iterable[PointGeometryParam]]
    """Array of origin coordinates as GeoJSON Points (max 50)"""

    annotations: str
    """
    Comma-separated list of annotations to include: `duration` (always included),
    `distance`. Example: `duration,distance`.
    """

    fallback_speed: Optional[float]
    """Fallback speed in km/h for pairs where no route exists.

    When set, unreachable pairs get estimated values instead of null.
    """

    mode: Literal["auto", "foot", "bicycle"]
    """Travel mode (default: `auto`)"""
