# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .geo_json_geometry import GeoJsonGeometry

__all__ = ["OptimizeCompletedResult", "Properties"]


class Properties(BaseModel):
    distance: Optional[float] = None
    """Total distance in meters"""

    duration: Optional[float] = None
    """Estimated duration in seconds"""

    waypoint_order: Optional[List[int]] = None
    """Optimized waypoint ordering"""


class OptimizeCompletedResult(BaseModel):
    """Completed optimization — GeoJSON Feature with optimized route"""

    geometry: GeoJsonGeometry

    properties: Properties

    status: Literal["completed"]
    """Job status"""

    type: Literal["Feature"]
