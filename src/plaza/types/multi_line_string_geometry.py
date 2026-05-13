# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MultiLineStringGeometry"]


class MultiLineStringGeometry(BaseModel):
    """GeoJSON MultiLineString geometry per RFC 7946.

    An array of LineString coordinate arrays.
    """

    coordinates: List[List[List[float]]]
    """Array of LineString coordinate arrays"""

    type: Literal["MultiLineString"]
