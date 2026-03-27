# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["OptimizeProcessingResult"]


class OptimizeProcessingResult(BaseModel):
    """Async optimization in progress — poll with the job_id"""

    job_id: str
    """Job ID for polling"""

    status: Literal["processing"]
    """Job status"""
