# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .geo_json_feature import GeoJsonFeature

__all__ = ["RoutingIsochroneResponse"]


class RoutingIsochroneResponse(BaseModel):
    """
    GeoJSON FeatureCollection of isochrone polygons — areas reachable within the specified travel time(s). Each Feature is a Polygon contour with travel time and area metadata in properties.
    """

    features: List[GeoJsonFeature]
    """Array of isochrone polygon Features, one per contour"""

    type: Literal["FeatureCollection"]
    """Always `FeatureCollection`"""
