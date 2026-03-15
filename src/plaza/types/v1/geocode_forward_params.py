# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GeocodeForwardParams"]


class GeocodeForwardParams(TypedDict, total=False):
    q: Required[str]
    """Address or place name"""

    lat: float
    """Focus latitude"""

    limit: int
    """Maximum results (default 20, max 100)"""

    lng: float
    """Focus longitude"""
