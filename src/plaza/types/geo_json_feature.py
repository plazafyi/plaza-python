# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .geo_json_geometry import GeoJsonGeometry

__all__ = ["GeoJsonFeature"]


class GeoJsonFeature(BaseModel):
    geometry: GeoJsonGeometry

    properties: Dict[str, object]

    type: Literal["Feature"]

    id: Optional[str] = None
    """Feature identifier (type/osm_id)"""

    osm_id: Optional[int] = None
    """OpenStreetMap ID"""
