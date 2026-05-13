# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MultiPointGeometry"]


class MultiPointGeometry(BaseModel):
    """GeoJSON MultiPoint geometry per RFC 7946. An array of positions."""

    coordinates: List[List[float]]
    """Array of [lng, lat] or [lng, lat, alt] positions"""

    type: Literal["MultiPoint"]
