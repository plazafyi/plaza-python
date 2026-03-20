# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .geo_json_geometry import GeoJsonGeometry

__all__ = ["SparqlResult", "Result"]


class Result(BaseModel):
    """GeoJSON Feature (may lack @type/@id metadata for untyped results)"""

    geometry: GeoJsonGeometry
    """GeoJSON Geometry object per RFC 7946.

    Coordinates use [longitude, latitude] order. 3D coordinates [lng, lat,
    elevation] are used for elevation endpoints.
    """

    properties: Dict[str, object]
    """OSM tags as key-value pairs, optionally with `@type` and `@id` metadata"""

    type: Literal["Feature"]
    """Always `Feature`"""

    id: Optional[str] = None
    """
    Compound identifier in `type/osm_id` format (present when element type is known)
    """


class SparqlResult(BaseModel):
    """SPARQL query result.

    Contains a `results` array of GeoJSON Feature objects. Unlike REST feature endpoints, SPARQL results may omit `@type`, `@id`, and compound `id` fields depending on the query shape.
    """

    results: List[Result]
    """Array of GeoJSON Features matching the SPARQL query.

    Features include `@type` and `@id` metadata when the source element type is
    known, but may contain only tags as properties for untyped results.
    """
