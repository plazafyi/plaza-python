# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .geo_json_feature import GeoJsonFeature
from .geo_json_geometry import GeoJsonGeometry

__all__ = ["RoutingIsochroneResponse", "Properties"]


class Properties(BaseModel):
    """Isochrone metadata"""

    area_m2: Optional[float] = None
    """Area of the isochrone polygon in square meters (multi-contour features only)"""

    max_cost_s: Optional[float] = None
    """
    Maximum actual travel cost in seconds to the isochrone boundary (single contour
    only)
    """

    mode: Optional[Literal["auto", "foot", "bicycle"]] = None
    """Travel mode used for the isochrone calculation"""

    time_seconds: Optional[float] = None
    """Travel time budget in seconds"""

    vertices_reached: Optional[int] = None
    """Number of road network vertices within the isochrone"""


class RoutingIsochroneResponse(BaseModel):
    """
    GeoJSON Feature or FeatureCollection representing isochrone polygons — areas reachable within the specified travel time(s). Single time value returns a Feature; comma-separated times return a FeatureCollection with one polygon per contour.
    """

    features: Optional[List[GeoJsonFeature]] = None
    """Array of isochrone polygon Features (multi-contour only)"""

    geometry: Optional[GeoJsonGeometry] = None
    """GeoJSON Geometry object per RFC 7946.

    Coordinates use [longitude, latitude] order. 3D coordinates [lng, lat,
    elevation] are used for elevation endpoints.
    """

    properties: Optional[Properties] = None
    """Isochrone metadata"""

    type: Optional[Literal["Feature", "FeatureCollection"]] = None
    """`Feature` for single contour, `FeatureCollection` for multiple contours"""
