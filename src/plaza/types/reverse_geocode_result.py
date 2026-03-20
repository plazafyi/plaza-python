# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .geocoding_feature import GeocodingFeature

__all__ = ["ReverseGeocodeResult"]


class ReverseGeocodeResult(BaseModel):
    """
    GeoJSON FeatureCollection of reverse geocoding results, ordered by distance from the query point. Content-Type: `application/geo+json`.
    """

    features: List[GeocodingFeature]
    """Reverse geocoding results ordered by distance"""

    type: Literal["FeatureCollection"]
