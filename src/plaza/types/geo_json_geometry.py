# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GeoJsonGeometry"]


class GeoJsonGeometry(BaseModel):
    """GeoJSON Geometry object per RFC 7946.

    Coordinates use [longitude, latitude] order. 3D coordinates [lng, lat, elevation] are used for elevation endpoints.
    """

    coordinates: Union[List[float], List[List[float]], List[List[List[float]]], List[List[List[List[float]]]]]
    """Coordinates array.

    Nesting depth varies by geometry type: Point = [lng, lat], LineString = [[lng,
    lat], ...], Polygon = [[[lng, lat], ...], ...], etc.
    """

    type: Literal["Point", "LineString", "Polygon", "MultiPoint", "MultiLineString", "MultiPolygon"]
    """Geometry type"""
