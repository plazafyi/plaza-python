# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LineStringGeometry"]


class LineStringGeometry(BaseModel):
    """GeoJSON LineString geometry per RFC 7946.

    An ordered sequence of two or more positions.
    """

    coordinates: List[List[float]]
    """Array of [lng, lat] or [lng, lat, alt] positions"""

    type: Literal["LineString"]
