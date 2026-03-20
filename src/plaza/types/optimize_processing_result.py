# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["OptimizeProcessingResult"]


class OptimizeProcessingResult(BaseModel):
    """Async optimization in progress.

    Poll `GET /api/v1/optimize/{job_id}` until the status changes to `completed` or `failed`.
    """

    job_id: str
    """Job ID for polling the result"""

    status: Literal["processing"]
    """Always `processing`"""
