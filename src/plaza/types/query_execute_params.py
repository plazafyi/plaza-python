# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["QueryExecuteParams"]


class QueryExecuteParams(TypedDict, total=False):
    data: Required[str]
    """PlazaQL query string"""

    format: str
    """Response format: json (default), geojson, csv, ndjson"""
