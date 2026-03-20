# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .geo_json_geometry import GeoJsonGeometry

__all__ = ["ElevationLookupResult", "Properties"]


class Properties(BaseModel):
    elevation_m: float
    """Elevation in meters above mean sea level (WGS84 EGM96 geoid)"""


class ElevationLookupResult(BaseModel):
    """
    GeoJSON Point Feature with a 3D coordinate [lng, lat, elevation] per RFC 7946 §3.1.1. The elevation is also available in `properties.elevation_m` for convenience.
    """

    geometry: GeoJsonGeometry
    """GeoJSON Geometry object per RFC 7946.

    Coordinates use [longitude, latitude] order. 3D coordinates [lng, lat,
    elevation] are used for elevation endpoints.
    """

    properties: Properties

    type: Literal["Feature"]
