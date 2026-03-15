# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .dataset_response import DatasetResponse

__all__ = ["DatasetListResponse"]


class DatasetListResponse(BaseModel):
    datasets: List[DatasetResponse]
