# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["OptimizeJobStatus"]


class OptimizeJobStatus(BaseModel):
    """Status of an async optimization job"""

    status: Literal["completed", "processing", "failed"]
    """Job status"""

    error: Optional[str] = None
    """Error message when failed"""

    result: Optional[object] = None
    """Optimization result when completed"""
