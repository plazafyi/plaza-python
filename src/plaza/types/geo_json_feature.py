# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .geometry import Geometry

__all__ = ["GeoJsonFeature"]


class GeoJsonFeature(BaseModel):
    """GeoJSON Feature representing an OSM element.

    Tags from the original OSM element are flattened directly into `properties` (not nested under a `tags` key). Metadata fields `@type` and `@id` identify the OSM element type and ID within properties.
    """

    geometry: Geometry
    """GeoJSON Geometry object per RFC 7946.

    Discriminated union — the `type` field determines the coordinate structure.
    """

    properties: Dict[str, object]
    """
    OSM tags flattened as key-value pairs, plus `@type` (node/way/relation) and
    `@id` (OSM ID) metadata fields. May include `distance_m` for proximity queries.
    """

    type: Literal["Feature"]
    """Always `Feature`"""

    id: Optional[str] = None
    """Compound identifier in `type/osm_id` format"""
