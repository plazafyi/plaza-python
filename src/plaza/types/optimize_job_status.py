# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .optimize_completed_result import OptimizeCompletedResult

__all__ = ["OptimizeJobStatus"]


class OptimizeJobStatus(BaseModel):
    """Status of an async optimization job.

    When `completed`, the `result` field contains the full OptimizeCompletedResult. When `processing`, the job is still running — poll again. Failed jobs return a standard Error response (HTTP 422), not this schema.
    """

    status: Literal["completed", "processing"]
    """Current job state"""

    result: Optional[OptimizeCompletedResult] = None
    """Completed optimization result as a GeoJSON FeatureCollection.

    Each Feature is a waypoint in optimized visit order. Top-level fields provide
    summary statistics.
    """
