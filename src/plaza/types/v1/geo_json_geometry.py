# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["GeoJsonGeometry"]


class GeoJsonGeometry(BaseModel):
    coordinates: Union[List[float], List[List[float]], List[List[List[float]]], List[List[List[List[float]]]]]
    """GeoJSON coordinates array (nesting depth varies by geometry type)"""

    type: Literal["Point", "LineString", "Polygon", "MultiPoint", "MultiLineString", "MultiPolygon"]
