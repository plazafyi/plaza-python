# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["QueryExecuteParams", "Step"]


class QueryExecuteParams(TypedDict, total=False):
    steps: Required[Iterable[Step]]
    """Ordered list of query steps to execute"""


class Step(TypedDict, total=False):
    """A single pipeline step"""

    type: Required[Literal["overpass", "sparql", "filter", "transform"]]
    """Step type: `overpass`, `sparql`, `filter`, or `transform`"""

    query: str
    """Query string for this step (required for overpass/sparql steps)"""
