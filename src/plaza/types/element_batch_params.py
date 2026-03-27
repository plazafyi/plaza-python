# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ElementBatchParams", "Element"]


class ElementBatchParams(TypedDict, total=False):
    elements: Required[Iterable[Element]]


class Element(TypedDict, total=False):
    id: Required[int]

    type: Required[Literal["node", "way", "relation"]]
