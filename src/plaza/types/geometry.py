# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .point_geometry import PointGeometry
from .polygon_geometry import PolygonGeometry
from .line_string_geometry import LineStringGeometry
from .multi_point_geometry import MultiPointGeometry
from .multi_polygon_geometry import MultiPolygonGeometry
from .multi_line_string_geometry import MultiLineStringGeometry

__all__ = ["Geometry"]

Geometry: TypeAlias = Annotated[
    Union[
        PointGeometry,
        LineStringGeometry,
        PolygonGeometry,
        MultiPointGeometry,
        MultiLineStringGeometry,
        MultiPolygonGeometry,
    ],
    PropertyInfo(discriminator="type"),
]
