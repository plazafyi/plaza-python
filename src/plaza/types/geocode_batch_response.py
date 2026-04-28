# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .geocode_result import GeocodeResult

__all__ = ["GeocodeBatchResponse"]


class GeocodeBatchResponse(BaseModel):
    """Batch geocoding result.

    Each entry in `results` is a FeatureCollection corresponding to the input address at the same index. Order is preserved.
    """

    count: int
    """Number of addresses processed (always equals length of results)"""

    results: List[GeocodeResult]
    """Array of FeatureCollections, one per input address.

    Empty FeatureCollections indicate no match.
    """
