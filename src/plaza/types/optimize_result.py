# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .optimize_completed_result import OptimizeCompletedResult
from .optimize_processing_result import OptimizeProcessingResult

__all__ = ["OptimizeResult"]

OptimizeResult: TypeAlias = Union[OptimizeCompletedResult, OptimizeProcessingResult]
