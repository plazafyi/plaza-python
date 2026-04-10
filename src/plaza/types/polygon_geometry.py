# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PolygonGeometry"]


class PolygonGeometry(BaseModel):
    """GeoJSON Polygon geometry per RFC 7946.

    An array of linear rings where the first ring is the exterior boundary and subsequent rings are holes. Each ring must have at least 4 positions with the first and last being identical.
    """

    coordinates: List[List[List[float]]]
    """Array of linear rings (first = exterior, rest = holes)"""

    type: Literal["Polygon"]
