# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .geo_json_feature import GeoJsonFeature

__all__ = ["SparqlResult"]


class SparqlResult(BaseModel):
    """GeoJSON FeatureCollection of SPARQL query results"""

    features: List[GeoJsonFeature]
    """GeoJSON features from SPARQL query"""

    type: Literal["FeatureCollection"]
