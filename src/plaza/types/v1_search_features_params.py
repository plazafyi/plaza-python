# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["V1SearchFeaturesParams"]


class V1SearchFeaturesParams(TypedDict, total=False):
    q: Required[str]
    """Search query string"""

    cursor: str
    """Cursor for pagination"""

    limit: int
    """Maximum results (default 25, max 100)"""
