# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .dataset import Dataset
from .._models import BaseModel

__all__ = ["DatasetList"]


class DatasetList(BaseModel):
    """List of datasets visible to the authenticated user."""

    datasets: List[Dataset]
    """Array of dataset metadata objects"""
