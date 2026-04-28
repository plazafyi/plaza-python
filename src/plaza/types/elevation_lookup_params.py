# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .point_geometry_param import PointGeometryParam
from .multi_point_geometry_param import MultiPointGeometryParam

__all__ = ["ElevationLookupParams", "Geometry"]


class ElevationLookupParams(TypedDict, total=False):
    geometry: Required[Geometry]
    """Point or MultiPoint geometry to look up elevations for"""

    format: str
    """Response format: json (default), geojson, csv, ndjson"""


Geometry: TypeAlias = Union[PointGeometryParam, MultiPointGeometryParam]
