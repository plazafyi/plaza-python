# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["V1SnapToNearestResponse"]


class V1SnapToNearestResponse(BaseModel):
    distance: float
    """Distance to nearest road in meters"""

    lat: float
    """Snapped latitude"""

    lng: float
    """Snapped longitude"""

    edge_id: Optional[int] = None
    """Road edge ID"""
