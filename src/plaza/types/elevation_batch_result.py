# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .elevation_lookup_result import ElevationLookupResult

__all__ = ["ElevationBatchResult"]


class ElevationBatchResult(BaseModel):
    """GeoJSON FeatureCollection of elevation Point Features with 3D coordinates"""

    features: List[ElevationLookupResult]
    """Elevation Point Features for each queried point"""

    type: Literal["FeatureCollection"]
