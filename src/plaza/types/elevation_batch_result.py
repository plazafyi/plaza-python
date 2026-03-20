# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .elevation_lookup_result import ElevationLookupResult

__all__ = ["ElevationBatchResult"]


class ElevationBatchResult(BaseModel):
    """GeoJSON FeatureCollection of elevation Point Features with 3D coordinates.

    Order matches the input coordinates array.
    """

    features: List[ElevationLookupResult]
    """Elevation results in the same order as input coordinates"""

    type: Literal["FeatureCollection"]
