# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Dataset"]


class Dataset(BaseModel):
    """Metadata for a custom dataset.

    Datasets contain user-uploaded geospatial features separate from the OSM data.
    """

    id: str
    """Dataset UUID"""

    inserted_at: datetime
    """Creation timestamp (UTC)"""

    name: str
    """Human-readable dataset name"""

    scope: Literal["plaza", "user"]
    """Dataset scope: plaza (managed by Plaza) or user (user-owned)"""

    slug: str
    """URL-friendly identifier"""

    status: Literal["pending", "processing", "ready", "error"]
    """Current processing status"""

    updated_at: datetime
    """Last update timestamp (UTC)"""

    address_count: Optional[int] = None
    """Number of addresses in this dataset"""

    attribution: Optional[str] = None
    """Required attribution text"""

    description: Optional[str] = None
    """Dataset description"""

    edge_count: Optional[int] = None
    """Number of routing edges in this dataset"""

    error_message: Optional[str] = None
    """Error message if status is 'error'"""

    feature_count: Optional[int] = None
    """Number of features in this dataset"""

    license: Optional[str] = None
    """License identifier (e.g. CC-BY-4.0)"""

    schema_definition: Optional[object] = None
    """Detected or user-defined property schema"""

    source_format: Optional[str] = None
    """Data format (geojson)"""

    source_url: Optional[str] = None
    """URL of the original data source"""

    storage_bytes: Optional[int] = None
    """Total storage consumed in bytes"""

    strict_mode: Optional[bool] = None
    """Whether strict schema validation is enabled"""
