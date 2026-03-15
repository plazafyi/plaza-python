# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DatasetCreateParams"]


class DatasetCreateParams(TypedDict, total=False):
    name: Required[str]
    """Dataset name"""

    slug: Required[str]
    """URL-friendly slug"""

    attribution: Optional[str]
    """Attribution text"""

    description: Optional[str]
    """Dataset description"""

    license: Optional[str]
    """License identifier"""

    source_url: Optional[str]
    """Source data URL"""
