# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["DatasetResponse"]


class DatasetResponse(BaseModel):
    id: str
    """Dataset ID"""

    inserted_at: datetime
    """Creation timestamp"""

    name: str
    """Dataset name"""

    slug: str
    """URL-friendly slug"""

    updated_at: datetime
    """Last update timestamp"""

    attribution: Optional[str] = None
    """Attribution text"""

    description: Optional[str] = None
    """Dataset description"""

    license: Optional[str] = None
    """License identifier"""

    source_url: Optional[str] = None
    """Source data URL"""
