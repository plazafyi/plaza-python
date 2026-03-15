# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .v1.geo_json_feature import GeoJsonFeature

__all__ = ["V1ExecuteSparqlResponse"]


class V1ExecuteSparqlResponse(BaseModel):
    results: List[GeoJsonFeature]
    """Array of GeoJSON features from SPARQL query"""
