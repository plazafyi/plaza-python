# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ElevationLookupParams"]


class ElevationLookupParams(TypedDict, total=False):
    lat: float
    """Latitude (single point)"""

    lng: float
    """Longitude (single point)"""

    locations: str
    """Pipe-separated lng,lat pairs (batch)"""

    output_fields: Annotated[str, PropertyInfo(alias="output[fields]")]
    """Comma-separated property fields to include"""

    output_include: Annotated[str, PropertyInfo(alias="output[include]")]
    """Extra computed fields: bbox, center"""

    output_precision: Annotated[int, PropertyInfo(alias="output[precision]")]
    """Coordinate decimal precision (1-15, default 7)"""
