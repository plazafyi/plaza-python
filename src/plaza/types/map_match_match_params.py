# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["MapMatchMatchParams", "Coordinate"]


class MapMatchMatchParams(TypedDict, total=False):
    coordinates: Required[Iterable[Coordinate]]
    """GPS coordinates to match, in order of travel (max 50 points)"""

    radiuses: Optional[Iterable[float]]
    """Search radius per coordinate in meters.

    Must have the same length as `coordinates` or be omitted entirely. Default: 50m
    per point.
    """


class Coordinate(TypedDict, total=False):
    """Geographic coordinate as a JSON object with `lat` and `lng` fields."""

    lat: Required[float]
    """Latitude in decimal degrees (-90 to 90)"""

    lng: Required[float]
    """Longitude in decimal degrees (-180 to 180)"""
