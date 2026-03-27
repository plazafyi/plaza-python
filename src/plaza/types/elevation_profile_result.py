# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .geo_json_geometry import GeoJsonGeometry

__all__ = ["ElevationProfileResult", "Properties"]


class Properties(BaseModel):
    avg_elevation_m: Optional[float] = None
    """Average elevation along profile"""

    max_elevation_m: Optional[float] = None
    """Maximum elevation along profile"""

    min_elevation_m: Optional[float] = None
    """Minimum elevation along profile"""

    total_ascent_m: Optional[float] = None
    """Total elevation gain in meters"""

    total_descent_m: Optional[float] = None
    """Total elevation loss in meters"""


class ElevationProfileResult(BaseModel):
    """
    GeoJSON LineString Feature with 3D coordinates representing an elevation profile
    """

    geometry: GeoJsonGeometry

    properties: Properties

    type: Literal["Feature"]
