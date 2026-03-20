# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RoutingMatrixParams", "Destination", "Origin"]


class RoutingMatrixParams(TypedDict, total=False):
    destinations: Required[Iterable[Destination]]
    """Array of destination coordinates (max 50)"""

    origins: Required[Iterable[Origin]]
    """Array of origin coordinates (max 50)"""

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


class Destination(TypedDict, total=False):
    """Geographic coordinate as a JSON object with `lat` and `lng` fields."""

    lat: Required[float]
    """Latitude in decimal degrees (-90 to 90)"""

    lng: Required[float]
    """Longitude in decimal degrees (-180 to 180)"""


class Origin(TypedDict, total=False):
    """Geographic coordinate as a JSON object with `lat` and `lng` fields."""

    lat: Required[float]
    """Latitude in decimal degrees (-90 to 90)"""

    lng: Required[float]
    """Longitude in decimal degrees (-180 to 180)"""
