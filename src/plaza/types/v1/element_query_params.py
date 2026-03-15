# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ElementQueryParams"]


class ElementQueryParams(TypedDict, total=False):
    bbox: str
    """Bounding box: south,west,north,east. At least one of bbox or h3 is required."""

    cursor: str
    """Cursor for pagination"""

    h3: str
    """H3 cell index. At least one of bbox or h3 is required."""

    limit: int
    """Maximum results (default 100, max 10000)"""

    type: str
    """Element types (comma-separated: node,way,relation)"""
