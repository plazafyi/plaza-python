# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PointGeometry"]


class PointGeometry(BaseModel):
    """GeoJSON Point geometry per RFC 7946.

    Coordinates use [longitude, latitude] order. Optional third element is altitude in meters.
    """

    coordinates: List[float]
    """[longitude, latitude] or [longitude, latitude, altitude]"""

    type: Literal["Point"]
