# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .geometry import Geometry

__all__ = ["MapMatchResult", "Feature", "FeatureProperties"]


class FeatureProperties(BaseModel):
    distance_m: Optional[float] = None
    """Distance from the original GPS point to the snapped point in meters"""

    edge_id: Optional[int] = None
    """Road edge ID the point was snapped to"""

    matchings_index: Optional[int] = None
    """
    Index into the `matchings` array indicating which matching sub-route this point
    belongs to
    """

    name: Optional[str] = None
    """Road name at the snapped point"""

    original: Optional[List[float]] = None
    """Original GPS coordinate as [lng, lat]"""

    waypoint_index: Optional[int] = None
    """Index of this tracepoint in the original `coordinates` array"""


class Feature(BaseModel):
    """GeoJSON Point Feature representing a GPS point snapped to the road network."""

    geometry: Geometry
    """GeoJSON Geometry object per RFC 7946.

    Discriminated union — the `type` field determines the coordinate structure.
    """

    properties: FeatureProperties

    type: Literal["Feature"]


class MapMatchResult(BaseModel):
    """Map matching result as a GeoJSON FeatureCollection.

    Each Feature is a snapped tracepoint. The top-level `matchings` array contains the matched sub-routes connecting consecutive tracepoints.
    """

    features: List[Feature]
    """Snapped tracepoint Features in input order"""

    matchings: List[Dict[str, object]]
    """Matched sub-routes.

    Each matching connects a contiguous sequence of tracepoints that could be
    matched to roads.
    """

    type: Literal["FeatureCollection"]
