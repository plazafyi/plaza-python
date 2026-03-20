# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RoutingNearestPostParams"]


class RoutingNearestPostParams(TypedDict, total=False):
    lat: Required[float]
    """Latitude"""

    lng: Required[float]
    """Longitude"""

    output_fields: Annotated[str, PropertyInfo(alias="output[fields]")]
    """Comma-separated property fields to include"""

    output_include: Annotated[str, PropertyInfo(alias="output[include]")]
    """Extra computed fields: bbox, distance, center"""

    output_precision: Annotated[int, PropertyInfo(alias="output[precision]")]
    """Coordinate decimal precision (1-15, default 7)"""

    radius: int
    """Search radius in meters (default 500, max 5000)"""
