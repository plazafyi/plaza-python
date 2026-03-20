# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .geo_json_geometry import GeoJsonGeometry

__all__ = ["RouteResult", "Properties"]


class Properties(BaseModel):
    """Route metadata"""

    distance_m: float
    """Total route distance in meters"""

    duration_s: float
    """Estimated travel duration in seconds"""

    annotations: Optional[Dict[str, object]] = None
    """Per-edge annotations (present when `annotations: true` in request)"""

    charge_profile: Optional[List[List[float]]] = None
    """
    Battery charge level at route waypoints as [distance_fraction, charge_pct] pairs
    (EV routes only)
    """

    charging_stops: Optional[List[Dict[str, object]]] = None
    """Recommended charging stops along the route (EV routes only)"""

    edges: Optional[List[Dict[str, object]]] = None
    """Edge-level route details (present when `annotations: true`)"""

    energy_used_wh: Optional[float] = None
    """Total energy consumed in watt-hours (EV routes only)"""


class RouteResult(BaseModel):
    """GeoJSON Feature representing a calculated route.

    The geometry is a LineString or MultiLineString of the route path. When `alternatives > 0`, the response is a FeatureCollection containing multiple route Features.
    """

    geometry: GeoJsonGeometry
    """GeoJSON Geometry object per RFC 7946.

    Coordinates use [longitude, latitude] order. 3D coordinates [lng, lat,
    elevation] are used for elevation endpoints.
    """

    properties: Properties
    """Route metadata"""

    type: Literal["Feature"]
