# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DatasetCreateParams"]


class DatasetCreateParams(TypedDict, total=False):
    name: Required[str]
    """Human-readable dataset name"""

    slug: Required[str]
    """URL-friendly identifier (lowercase, hyphens, no spaces)"""

    attribution: Optional[str]
    """Required attribution text"""

    description: Optional[str]
    """Dataset description"""

    license: Optional[str]
    """License identifier (e.g. CC-BY-4.0)"""

    source_url: Optional[str]
    """Source data URL"""

    strict_mode: Optional[bool]
    """Enable strict schema validation (default true)"""
