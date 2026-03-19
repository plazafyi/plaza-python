# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .geo_json_geometry import GeoJsonGeometry

__all__ = ["GeocodingFeature", "Properties"]


class Properties(BaseModel):
    country_code: Optional[str] = None
    """ISO 3166-1 alpha-2 country code"""

    display_name: Optional[str] = None
    """Formatted address or place name"""

    distance_m: Optional[float] = None
    """Distance in meters"""

    osm_id: Optional[int] = None
    """OpenStreetMap ID"""

    osm_type: Optional[str] = None
    """OSM element type"""

    score: Optional[float] = None
    """Match confidence score"""

    source: Optional[str] = None
    """Result source (address, place, interpolation)"""


class GeocodingFeature(BaseModel):
    geometry: GeoJsonGeometry

    properties: Properties

    type: Literal["Feature"]
