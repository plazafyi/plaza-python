# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .geo_json_geometry import GeoJsonGeometry

__all__ = ["NearestResult", "Properties"]


class Properties(BaseModel):
    """Snap result metadata"""

    distance_m: Optional[float] = None
    """Distance from the input coordinate to the snapped point in meters"""

    edge_id: Optional[int] = None
    """ID of the road network edge that was snapped to"""

    edge_length_m: Optional[float] = None
    """Length of the matched road edge in meters"""

    highway: Optional[str] = None
    """OSM highway tag value (e.g. `residential`, `primary`, `motorway`)"""

    osm_way_id: Optional[int] = None
    """OSM way ID of the matched road segment"""

    surface: Optional[str] = None
    """OSM surface tag value (e.g. `asphalt`, `gravel`, `paved`)"""


class NearestResult(BaseModel):
    """
    GeoJSON Point Feature representing the nearest point on the road network to the input coordinate. Used for snapping GPS coordinates to roads.
    """

    geometry: GeoJsonGeometry
    """GeoJSON Geometry object per RFC 7946.

    Coordinates use [longitude, latitude] order. 3D coordinates [lng, lat,
    elevation] are used for elevation endpoints.
    """

    properties: Properties
    """Snap result metadata"""

    type: Literal["Feature"]
