# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .geocoding_feature import GeocodingFeature

__all__ = ["GeocodeResult"]


class GeocodeResult(BaseModel):
    """GeoJSON FeatureCollection of geocoding results"""

    features: List[GeocodingFeature]

    type: Literal["FeatureCollection"]
