# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .geometry import Geometry

__all__ = ["ElevationProfileResult", "Properties"]


class Properties(BaseModel):
    """Elevation profile summary statistics"""

    avg_elevation_m: float
    """Average elevation along the profile in meters"""

    max_elevation_m: float
    """Maximum elevation along the profile in meters"""

    min_elevation_m: float
    """Minimum elevation along the profile in meters"""

    total_ascent_m: float
    """Total cumulative elevation gain in meters"""

    total_descent_m: float
    """Total cumulative elevation loss in meters"""


class ElevationProfileResult(BaseModel):
    """
    GeoJSON LineString Feature with 3D coordinates [lng, lat, elevation] representing the elevation profile along the input path. Summary statistics are in properties.
    """

    geometry: Geometry
    """GeoJSON Geometry object per RFC 7946.

    Discriminated union — the `type` field determines the coordinate structure.
    """

    properties: Properties
    """Elevation profile summary statistics"""

    type: Literal["Feature"]
