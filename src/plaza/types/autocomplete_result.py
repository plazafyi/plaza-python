# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .geocoding_feature import GeocodingFeature

__all__ = ["AutocompleteResult"]


class AutocompleteResult(BaseModel):
    """GeoJSON FeatureCollection of autocomplete suggestions"""

    features: List[GeocodingFeature]

    type: Literal["FeatureCollection"]
