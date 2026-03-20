# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel

__all__ = ["QueryExecuteResponse"]


class QueryExecuteResponse(BaseModel):
    """Pipeline execution result containing the output of each step."""

    steps: List[Dict[str, object]]
    """Results from each pipeline step in execution order"""
