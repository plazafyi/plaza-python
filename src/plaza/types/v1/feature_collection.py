# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .geo_json_feature import GeoJsonFeature

__all__ = ["FeatureCollection", "Pagination"]


class Pagination(BaseModel):
    has_more: Optional[bool] = None
    """Whether more results exist"""

    limit: Optional[int] = None
    """Requested result limit"""

    next_cursor: Optional[str] = None
    """Cursor for next page"""

    next_offset: Optional[int] = None
    """Offset for next page"""


class FeatureCollection(BaseModel):
    features: List[GeoJsonFeature]

    type: Literal["FeatureCollection"]

    pagination: Optional[Pagination] = None
