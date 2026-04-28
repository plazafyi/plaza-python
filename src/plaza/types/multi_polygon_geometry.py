# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MultiPolygonGeometry"]


class MultiPolygonGeometry(BaseModel):
    """GeoJSON MultiPolygon geometry per RFC 7946.

    An array of Polygon coordinate arrays.
    """

    coordinates: List[List[List[List[float]]]]
    """Array of Polygon coordinate arrays"""

    type: Literal["MultiPolygon"]
