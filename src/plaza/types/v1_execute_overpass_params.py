# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["V1ExecuteOverpassParams"]


class V1ExecuteOverpassParams(TypedDict, total=False):
    data: Required[str]
    """Overpass QL query string"""
