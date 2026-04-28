# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .point_geometry_param import PointGeometryParam

__all__ = ["RoutingRouteParams", "Ev"]


class RoutingRouteParams(TypedDict, total=False):
    destination: Required[PointGeometryParam]
    """GeoJSON Point geometry per RFC 7946.

    Coordinates use [longitude, latitude] order. Optional third element is altitude
    in meters.
    """

    origin: Required[PointGeometryParam]
    """GeoJSON Point geometry per RFC 7946.

    Coordinates use [longitude, latitude] order. Optional third element is altitude
    in meters.
    """

    format: str
    """Response format for alternatives: json (default), geojson, csv, ndjson"""

    alternatives: int
    """Number of alternative routes to return (0-3, default 0).

    When > 0, response is a FeatureCollection of route Features.
    """

    annotations: bool
    """Include per-edge annotations (speed, duration) on the route (default: false)"""

    depart_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Departure time for traffic-aware routing (ISO 8601)"""

    ev: Optional[Ev]
    """Electric vehicle parameters for EV-aware routing"""

    exclude: Optional[str]
    """Comma-separated road types to exclude (e.g. `toll,motorway,ferry`)"""

    geometries: Literal["geojson", "polyline", "polyline6"]
    """Geometry encoding format. Default: `geojson`."""

    mode: Literal["auto", "foot", "bicycle"]
    """Travel mode (default: `auto`)"""

    overview: Literal["full", "simplified", "false"]
    """
    Level of geometry detail: `full` (all points), `simplified` (Douglas-Peucker),
    `false` (no geometry). Default: `full`.
    """

    steps: bool
    """Include turn-by-turn navigation steps (default: false)"""

    traffic_model: Optional[Literal["best_guess", "optimistic", "pessimistic"]]
    """Traffic prediction model (only used when `depart_at` is set)"""

    waypoints: Optional[Iterable[PointGeometryParam]]
    """Intermediate waypoints to visit in order (maximum 25)"""


class Ev(TypedDict, total=False):
    """Electric vehicle parameters for EV-aware routing"""

    battery_capacity_wh: Required[float]
    """Total battery capacity in watt-hours (required for EV routing)"""

    connector_types: Optional[SequenceNotStr[str]]
    """Acceptable connector types (e.g. `["ccs", "chademo"]`)"""

    initial_charge_pct: float
    """Starting charge as a fraction 0-1 (default: 0.8)"""

    min_charge_pct: float
    """Minimum acceptable charge at destination as a fraction 0-1 (default: 0.10)"""

    min_power_kw: Optional[float]
    """Minimum charger power in kilowatts"""
