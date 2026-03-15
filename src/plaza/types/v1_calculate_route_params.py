# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["V1CalculateRouteParams", "Destination", "Origin"]


class V1CalculateRouteParams(TypedDict, total=False):
    destination: Required[Destination]

    origin: Required[Origin]

    mode: Literal["auto", "foot", "bicycle"]


class Destination(TypedDict, total=False):
    lat: Required[float]

    lng: Required[float]


class Origin(TypedDict, total=False):
    lat: Required[float]

    lng: Required[float]
