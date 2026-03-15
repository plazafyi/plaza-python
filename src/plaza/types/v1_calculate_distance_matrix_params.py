# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["V1CalculateDistanceMatrixParams", "Destination", "Origin"]


class V1CalculateDistanceMatrixParams(TypedDict, total=False):
    destinations: Required[Iterable[Destination]]
    """List of destination coordinates"""

    origins: Required[Iterable[Origin]]
    """List of origin coordinates"""

    mode: Literal["auto", "foot", "bicycle"]
    """Travel mode"""


class Destination(TypedDict, total=False):
    lat: Required[float]

    lng: Required[float]


class Origin(TypedDict, total=False):
    lat: Required[float]

    lng: Required[float]
