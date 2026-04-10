# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .geometry import Geometry

__all__ = ["GeocodingFeature", "Properties"]


class Properties(BaseModel):
    """Geocoding result properties"""

    display_name: str
    """Formatted address or place name"""

    category: Optional[str] = None
    """POI category (e.g. restaurant, cafe, park). Present for place results."""

    city: Optional[str] = None
    """City or town name. Present for address results."""

    confidence: Optional[float] = None
    """Interpolation confidence (0-1). Present only for interpolated results."""

    country: Optional[str] = None
    """Country name. Present for reverse geocode address results."""

    country_code: Optional[str] = None
    """ISO 3166-1 alpha-2 country code"""

    distance_m: Optional[float] = None
    """Distance from the query point in meters (reverse geocode / nearby only)"""

    full_address: Optional[str] = None
    """Complete formatted address from the database.

    Present for reverse geocode address results.
    """

    house_number: Optional[str] = None
    """House or building number. Present for address and interpolated results."""

    interpolated: Optional[bool] = None
    """
    Whether this result was estimated by address interpolation rather than an exact
    database match.
    """

    name: Optional[str] = None
    """Place name (raw). Present for reverse geocode place results."""

    osm_id: Optional[int] = None
    """OpenStreetMap element ID (null for interpolated results)"""

    osm_type: Optional[Literal["node", "way", "relation"]] = None
    """OSM element type (node, way, relation)"""

    postcode: Optional[str] = None
    """Postal code. Present for reverse geocode address results."""

    score: Optional[float] = None
    """Relevance score (higher is better).

    Incorporates text match quality, spatial proximity boost, and popularity
    signals. Not bounded to 0-1.
    """

    source: Optional[Literal["structured", "fuzzy", "address", "place", "interpolation"]] = None
    """
    Result source indicating how the result was found: structured (exact field
    match), fuzzy (trigram similarity), address (reverse geocode address), place
    (reverse geocode POI), interpolation (estimated from neighboring addresses)
    """

    state: Optional[str] = None
    """State or province name. Present for reverse geocode address results."""

    street: Optional[str] = None
    """Street name. Present for address and interpolated results."""

    subcategory: Optional[str] = None
    """POI subcategory. Present for place results."""

    tags: Optional[Dict[str, str]] = None
    """Raw OSM tags. Present for place results."""

    wikipedia: Optional[str] = None
    """Wikipedia article reference (e.g. en:Eiffel Tower). Present for notable places."""


class GeocodingFeature(BaseModel):
    """GeoJSON Feature representing a geocoding result.

    The geometry is always a Point. Properties include the formatted display name, OSM metadata, confidence score, and source type.
    """

    geometry: Geometry
    """GeoJSON Geometry object per RFC 7946.

    Discriminated union — the `type` field determines the coordinate structure.
    """

    properties: Properties
    """Geocoding result properties"""

    type: Literal["Feature"]
