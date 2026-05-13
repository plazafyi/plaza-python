# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .point_geometry_param import PointGeometryParam
from .polygon_geometry_param import PolygonGeometryParam
from .line_string_geometry_param import LineStringGeometryParam
from .multi_point_geometry_param import MultiPointGeometryParam
from .multi_polygon_geometry_param import MultiPolygonGeometryParam
from .multi_line_string_geometry_param import MultiLineStringGeometryParam

__all__ = ["GeometryParam"]

GeometryParam: TypeAlias = Union[
    PointGeometryParam,
    LineStringGeometryParam,
    PolygonGeometryParam,
    MultiPointGeometryParam,
    MultiLineStringGeometryParam,
    MultiPolygonGeometryParam,
]
