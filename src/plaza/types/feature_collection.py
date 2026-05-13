# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .geo_json_feature import GeoJsonFeature

__all__ = ["FeatureCollection"]


class FeatureCollection(BaseModel):
    """GeoJSON FeatureCollection (RFC 7946).

    For paginated endpoints, metadata is returned in HTTP response headers rather than the body:

    | Header | Description |
    |---|---|
    | `X-Limit` | Requested result limit |
    | `X-Has-More` | `true` if more results exist |
    | `X-Next-Cursor` | Opaque cursor for next page (cursor pagination) |
    | `X-Next-Offset` | Numeric offset for next page (offset pagination) |
    | `Link` | RFC 8288 `rel="next"` link to the next page |

    Content-Type is `application/geo+json`.
    """

    features: List[GeoJsonFeature]
    """Array of GeoJSON Feature objects"""

    type: Literal["FeatureCollection"]
    """Always `FeatureCollection`"""
