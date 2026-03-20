# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GeocodeAutocompletePostParams"]


class GeocodeAutocompletePostParams(TypedDict, total=False):
    q: Required[str]
    """Partial address query"""

    country_code: str
    """ISO 3166-1 alpha-2 country code filter"""

    format: str
    """Response format: json (default), geojson, csv, ndjson"""

    lang: str
    """Language code for localized names (e.g. en, de, fr)"""

    lat: float
    """Focus latitude"""

    layer: str
    """Filter by layer: address, poi, or admin"""

    limit: int
    """Maximum results (default 10, max 20)"""

    lng: float
    """Focus longitude"""
