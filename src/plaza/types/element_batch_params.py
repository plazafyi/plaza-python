# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ElementBatchParams", "Element"]


class ElementBatchParams(TypedDict, total=False):
    elements: Required[Iterable[Element]]
    """Array of element references to fetch"""


class Element(TypedDict, total=False):
    """Reference to a single OSM element"""

    id: Required[int]
    """OSM element ID"""

    type: Required[Literal["node", "way", "relation"]]
    """OSM element type"""
