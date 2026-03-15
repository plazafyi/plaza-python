# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["V1ExecuteQueryParams"]


class V1ExecuteQueryParams(TypedDict, total=False):
    bbox: str
    """Bounding box filter"""

    type: str
    """Element type filter"""
