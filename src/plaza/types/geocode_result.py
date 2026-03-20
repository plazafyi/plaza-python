# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .geocoding_feature import GeocodingFeature

__all__ = ["GeocodeResult"]


class GeocodeResult(BaseModel):
    """GeoJSON FeatureCollection of forward geocoding results, ordered by relevance.

    Content-Type: `application/geo+json`.
    """

    features: List[GeocodingFeature]
    """Geocoding results ordered by relevance score"""

    type: Literal["FeatureCollection"]
