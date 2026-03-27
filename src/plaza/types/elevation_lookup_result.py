# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .geo_json_geometry import GeoJsonGeometry

__all__ = ["ElevationLookupResult", "Properties"]


class Properties(BaseModel):
    elevation_m: Optional[float] = None
    """Elevation in meters above mean sea level"""


class ElevationLookupResult(BaseModel):
    """
    GeoJSON Point Feature with 3D coordinate [lng, lat, elevation] (RFC 7946 §3.1.1)
    """

    geometry: GeoJsonGeometry

    properties: Properties

    type: Literal["Feature"]
