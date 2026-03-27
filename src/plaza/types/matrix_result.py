# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["MatrixResult"]


class MatrixResult(BaseModel):
    distances: List[List[Optional[float]]]
    """Distance matrix (meters), origins x destinations"""

    durations: List[List[Optional[float]]]
    """Duration matrix (seconds), origins x destinations"""
