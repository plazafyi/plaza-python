# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .geo_json_geometry import GeoJsonGeometry

__all__ = ["OptimizeCompletedResult", "Feature", "FeatureProperties"]


class FeatureProperties(BaseModel):
    cost_s: float
    """
    Travel time in seconds from the previous waypoint to this one (0 for the first
    waypoint)
    """

    cumulative_cost_s: float
    """Cumulative travel time in seconds from the start to this waypoint"""

    waypoint_index: int
    """Position of this waypoint in the optimized visit order (0-based)"""


class Feature(BaseModel):
    """GeoJSON Point Feature representing an optimized waypoint with cost data."""

    geometry: GeoJsonGeometry
    """GeoJSON Geometry object per RFC 7946.

    Coordinates use [longitude, latitude] order. 3D coordinates [lng, lat,
    elevation] are used for elevation endpoints.
    """

    properties: FeatureProperties

    type: Literal["Feature"]


class OptimizeCompletedResult(BaseModel):
    """Completed optimization result as a GeoJSON FeatureCollection.

    Each Feature is a waypoint in optimized visit order. Top-level fields provide summary statistics.
    """

    features: List[Feature]
    """Waypoints in optimized visit order"""

    optimization: str
    """Optimization method used (e.g. `nearest_neighbor`, `2opt`)"""

    roundtrip: bool
    """Whether the route returns to the starting waypoint"""

    total_cost_s: float
    """Total travel time for the optimized route in seconds"""

    type: Literal["FeatureCollection"]
