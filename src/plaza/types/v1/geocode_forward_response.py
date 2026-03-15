# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["GeocodeForwardResponse", "Result"]


class Result(BaseModel):
    display_name: str
    """Formatted address or place name"""

    lat: float
    """Latitude"""

    lng: float
    """Longitude"""

    osm_id: Optional[int] = None
    """OpenStreetMap ID"""

    osm_type: Optional[str] = None
    """OSM element type"""

    score: Optional[float] = None
    """Match confidence score"""


class GeocodeForwardResponse(BaseModel):
    results: List[Result]

    count: Optional[int] = None
    """Number of results"""
