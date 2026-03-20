# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

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

    slug: str
    """URL-friendly identifier"""

    updated_at: datetime
    """Last update timestamp (UTC)"""

    attribution: Optional[str] = None
    """Required attribution text"""

    description: Optional[str] = None
    """Dataset description"""

    license: Optional[str] = None
    """License identifier (e.g. CC-BY-4.0)"""

    source_url: Optional[str] = None
    """URL of the original data source"""
