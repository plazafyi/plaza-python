# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .v1.geo_json_geometry import GeoJsonGeometry

__all__ = ["V1CalculateRouteResponse", "Properties"]


class Properties(BaseModel):
    distance: Optional[float] = None
    """Total distance in meters"""

    duration: Optional[float] = None
    """Estimated duration in seconds"""

    mode: Optional[str] = None
    """Travel mode used"""


class V1CalculateRouteResponse(BaseModel):
    geometry: GeoJsonGeometry

    properties: Properties

    type: Literal["Feature"]
