# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .geo_json_geometry import GeoJsonGeometry

__all__ = ["NearestResult", "Properties"]


class Properties(BaseModel):
    distance_m: Optional[float] = None
    """Distance to nearest road in meters"""

    edge_id: Optional[int] = None
    """Road edge ID"""


class NearestResult(BaseModel):
    """GeoJSON Point Feature snapped to the nearest road segment"""

    geometry: GeoJsonGeometry

    properties: Properties

    type: Literal["Feature"]
