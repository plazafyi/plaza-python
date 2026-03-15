# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["V1CalculateIsochroneParams"]


class V1CalculateIsochroneParams(TypedDict, total=False):
    lat: Required[float]
    """Latitude"""

    lng: Required[float]
    """Longitude"""

    time: Required[float]
    """Travel time in seconds (1-7200)"""

    mode: str
    """Travel mode (auto, foot, bicycle)"""
