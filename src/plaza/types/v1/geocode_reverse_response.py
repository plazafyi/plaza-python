# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["GeocodeReverseResponse"]


class GeocodeReverseResponse(BaseModel):
    address: str
    """Formatted address"""

    distance: float
    """Distance in meters from query point"""

    lat: float
    """Latitude"""

    lng: float
    """Longitude"""

    osm_id: Optional[int] = None
    """OpenStreetMap ID"""

    osm_type: Optional[str] = None
    """OSM element type"""
