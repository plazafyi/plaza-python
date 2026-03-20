# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ElevationBatchParams", "Coordinate"]


class ElevationBatchParams(TypedDict, total=False):
    coordinates: Required[Iterable[Coordinate]]
    """Coordinates to look up elevations for (max 50)"""


class Coordinate(TypedDict, total=False):
    """Geographic coordinate as a JSON object with `lat` and `lng` fields."""

    lat: Required[float]
    """Latitude in decimal degrees (-90 to 90)"""

    lng: Required[float]
    """Longitude in decimal degrees (-180 to 180)"""
