# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .geo_json_geometry import GeoJsonGeometry

__all__ = ["MapMatchResult", "Properties"]


class Properties(BaseModel):
    confidence: Optional[float] = None
    """Match confidence score"""

    distance: Optional[float] = None
    """Total matched distance in meters"""

    duration: Optional[float] = None
    """Estimated duration in seconds"""


class MapMatchResult(BaseModel):
    """Map matching result with snapped geometry"""

    geometry: GeoJsonGeometry

    properties: Properties

    type: Literal["Feature"]

    legs: Optional[List[Dict[str, object]]] = None
    """Matched route legs between consecutive trace points"""
