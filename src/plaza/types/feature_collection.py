# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .geo_json_feature import GeoJsonFeature

__all__ = ["FeatureCollection"]


class FeatureCollection(BaseModel):
    """Bare GeoJSON FeatureCollection.

    Pagination metadata is returned in HTTP headers (X-Limit, X-Has-More, X-Next-Cursor, X-Next-Offset, Link).
    """

    features: List[GeoJsonFeature]

    type: Literal["FeatureCollection"]
