# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .geocoding_feature import GeocodingFeature

__all__ = ["AutocompleteResult"]


class AutocompleteResult(BaseModel):
    """GeoJSON FeatureCollection of autocomplete suggestions for partial address input.

    Optimized for low-latency type-ahead UIs. Content-Type: `application/geo+json`.
    """

    features: List[GeocodingFeature]
    """Autocomplete suggestions ordered by relevance"""

    type: Literal["FeatureCollection"]
