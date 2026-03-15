# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["GeocodeAutocompleteResponse", "Result"]


class Result(BaseModel):
    display_name: str
    """Suggested address or place name"""

    lat: Optional[float] = None
    """Latitude"""

    lng: Optional[float] = None
    """Longitude"""


class GeocodeAutocompleteResponse(BaseModel):
    results: List[Result]
