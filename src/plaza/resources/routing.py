# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    routing_route_params,
    routing_matrix_params,
    routing_nearest_params,
    routing_isochrone_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.route_result import RouteResult
from ..types.matrix_result import MatrixResult
from ..types.nearest_result import NearestResult
from ..types.point_geometry_param import PointGeometryParam
from ..types.routing_isochrone_response import RoutingIsochroneResponse

__all__ = ["RoutingResource", "AsyncRoutingResource"]


class RoutingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoutingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plazafyi/plaza-python#accessing-raw-response-data-eg-headers
        """
        return RoutingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plazafyi/plaza-python#with_streaming_response
        """
        return RoutingResourceWithStreamingResponse(self)

    def isochrone(
        self,
        *,
        geometry: PointGeometryParam,
        time: Iterable[int],
        format: str | Omit = omit,
        mode: Literal["auto", "foot", "bicycle"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingIsochroneResponse:
        """
        Calculate an isochrone from a point

        Args:
          geometry: GeoJSON Point geometry per RFC 7946. Coordinates use [longitude, latitude]
              order. Optional third element is altitude in meters.

          time: Travel time budgets in seconds. Each value produces one contour polygon.

          format: Response format: json (default), geojson, csv, ndjson

          mode: Travel mode (default: `auto`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/isochrone",
            body=maybe_transform(
                {
                    "geometry": geometry,
                    "time": time,
                    "mode": mode,
                },
                routing_isochrone_params.RoutingIsochroneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, routing_isochrone_params.RoutingIsochroneParams),
            ),
            cast_to=RoutingIsochroneResponse,
        )

    def matrix(
        self,
        *,
        destinations: Iterable[PointGeometryParam],
        origins: Iterable[PointGeometryParam],
        annotations: str | Omit = omit,
        fallback_speed: Optional[float] | Omit = omit,
        mode: Literal["auto", "foot", "bicycle"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MatrixResult:
        """
        Calculate a distance matrix between points

        Args:
          destinations: Array of destination coordinates as GeoJSON Points (max 50)

          origins: Array of origin coordinates as GeoJSON Points (max 50)

          annotations: Comma-separated list of annotations to include: `duration` (always included),
              `distance`. Example: `duration,distance`.

          fallback_speed: Fallback speed in km/h for pairs where no route exists. When set, unreachable
              pairs get estimated values instead of null.

          mode: Travel mode (default: `auto`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/matrix",
            body=maybe_transform(
                {
                    "destinations": destinations,
                    "origins": origins,
                    "annotations": annotations,
                    "fallback_speed": fallback_speed,
                    "mode": mode,
                },
                routing_matrix_params.RoutingMatrixParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MatrixResult,
        )

    def nearest(
        self,
        *,
        geometry: PointGeometryParam,
        radius: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NearestResult:
        """
        Snap a coordinate to the nearest road

        Args:
          geometry: GeoJSON Point geometry per RFC 7946. Coordinates use [longitude, latitude]
              order. Optional third element is altitude in meters.

          radius: Maximum search radius in meters (default: 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/nearest",
            body=maybe_transform(
                {
                    "geometry": geometry,
                    "radius": radius,
                },
                routing_nearest_params.RoutingNearestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NearestResult,
        )

    def route(
        self,
        *,
        destination: PointGeometryParam,
        origin: PointGeometryParam,
        format: str | Omit = omit,
        alternatives: int | Omit = omit,
        annotations: bool | Omit = omit,
        depart_at: Union[str, datetime, None] | Omit = omit,
        ev: Optional[routing_route_params.Ev] | Omit = omit,
        exclude: Optional[str] | Omit = omit,
        geometries: Literal["geojson", "polyline", "polyline6"] | Omit = omit,
        mode: Literal["auto", "foot", "bicycle"] | Omit = omit,
        overview: Literal["full", "simplified", "false"] | Omit = omit,
        steps: bool | Omit = omit,
        traffic_model: Optional[Literal["best_guess", "optimistic", "pessimistic"]] | Omit = omit,
        waypoints: Optional[Iterable[PointGeometryParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RouteResult:
        """
        Calculate a route between two points

        Args:
          destination: GeoJSON Point geometry per RFC 7946. Coordinates use [longitude, latitude]
              order. Optional third element is altitude in meters.

          origin: GeoJSON Point geometry per RFC 7946. Coordinates use [longitude, latitude]
              order. Optional third element is altitude in meters.

          format: Response format for alternatives: json (default), geojson, csv, ndjson

          alternatives: Number of alternative routes to return (0-3, default 0). When > 0, response is a
              FeatureCollection of route Features.

          annotations: Include per-edge annotations (speed, duration) on the route (default: false)

          depart_at: Departure time for traffic-aware routing (ISO 8601)

          ev: Electric vehicle parameters for EV-aware routing

          exclude: Comma-separated road types to exclude (e.g. `toll,motorway,ferry`)

          geometries: Geometry encoding format. Default: `geojson`.

          mode: Travel mode (default: `auto`)

          overview: Level of geometry detail: `full` (all points), `simplified` (Douglas-Peucker),
              `false` (no geometry). Default: `full`.

          steps: Include turn-by-turn navigation steps (default: false)

          traffic_model: Traffic prediction model (only used when `depart_at` is set)

          waypoints: Intermediate waypoints to visit in order (maximum 25)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/route",
            body=maybe_transform(
                {
                    "destination": destination,
                    "origin": origin,
                    "alternatives": alternatives,
                    "annotations": annotations,
                    "depart_at": depart_at,
                    "ev": ev,
                    "exclude": exclude,
                    "geometries": geometries,
                    "mode": mode,
                    "overview": overview,
                    "steps": steps,
                    "traffic_model": traffic_model,
                    "waypoints": waypoints,
                },
                routing_route_params.RoutingRouteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, routing_route_params.RoutingRouteParams),
            ),
            cast_to=RouteResult,
        )


class AsyncRoutingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoutingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plazafyi/plaza-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoutingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plazafyi/plaza-python#with_streaming_response
        """
        return AsyncRoutingResourceWithStreamingResponse(self)

    async def isochrone(
        self,
        *,
        geometry: PointGeometryParam,
        time: Iterable[int],
        format: str | Omit = omit,
        mode: Literal["auto", "foot", "bicycle"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingIsochroneResponse:
        """
        Calculate an isochrone from a point

        Args:
          geometry: GeoJSON Point geometry per RFC 7946. Coordinates use [longitude, latitude]
              order. Optional third element is altitude in meters.

          time: Travel time budgets in seconds. Each value produces one contour polygon.

          format: Response format: json (default), geojson, csv, ndjson

          mode: Travel mode (default: `auto`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/isochrone",
            body=await async_maybe_transform(
                {
                    "geometry": geometry,
                    "time": time,
                    "mode": mode,
                },
                routing_isochrone_params.RoutingIsochroneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"format": format}, routing_isochrone_params.RoutingIsochroneParams),
            ),
            cast_to=RoutingIsochroneResponse,
        )

    async def matrix(
        self,
        *,
        destinations: Iterable[PointGeometryParam],
        origins: Iterable[PointGeometryParam],
        annotations: str | Omit = omit,
        fallback_speed: Optional[float] | Omit = omit,
        mode: Literal["auto", "foot", "bicycle"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MatrixResult:
        """
        Calculate a distance matrix between points

        Args:
          destinations: Array of destination coordinates as GeoJSON Points (max 50)

          origins: Array of origin coordinates as GeoJSON Points (max 50)

          annotations: Comma-separated list of annotations to include: `duration` (always included),
              `distance`. Example: `duration,distance`.

          fallback_speed: Fallback speed in km/h for pairs where no route exists. When set, unreachable
              pairs get estimated values instead of null.

          mode: Travel mode (default: `auto`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/matrix",
            body=await async_maybe_transform(
                {
                    "destinations": destinations,
                    "origins": origins,
                    "annotations": annotations,
                    "fallback_speed": fallback_speed,
                    "mode": mode,
                },
                routing_matrix_params.RoutingMatrixParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MatrixResult,
        )

    async def nearest(
        self,
        *,
        geometry: PointGeometryParam,
        radius: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NearestResult:
        """
        Snap a coordinate to the nearest road

        Args:
          geometry: GeoJSON Point geometry per RFC 7946. Coordinates use [longitude, latitude]
              order. Optional third element is altitude in meters.

          radius: Maximum search radius in meters (default: 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/nearest",
            body=await async_maybe_transform(
                {
                    "geometry": geometry,
                    "radius": radius,
                },
                routing_nearest_params.RoutingNearestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NearestResult,
        )

    async def route(
        self,
        *,
        destination: PointGeometryParam,
        origin: PointGeometryParam,
        format: str | Omit = omit,
        alternatives: int | Omit = omit,
        annotations: bool | Omit = omit,
        depart_at: Union[str, datetime, None] | Omit = omit,
        ev: Optional[routing_route_params.Ev] | Omit = omit,
        exclude: Optional[str] | Omit = omit,
        geometries: Literal["geojson", "polyline", "polyline6"] | Omit = omit,
        mode: Literal["auto", "foot", "bicycle"] | Omit = omit,
        overview: Literal["full", "simplified", "false"] | Omit = omit,
        steps: bool | Omit = omit,
        traffic_model: Optional[Literal["best_guess", "optimistic", "pessimistic"]] | Omit = omit,
        waypoints: Optional[Iterable[PointGeometryParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RouteResult:
        """
        Calculate a route between two points

        Args:
          destination: GeoJSON Point geometry per RFC 7946. Coordinates use [longitude, latitude]
              order. Optional third element is altitude in meters.

          origin: GeoJSON Point geometry per RFC 7946. Coordinates use [longitude, latitude]
              order. Optional third element is altitude in meters.

          format: Response format for alternatives: json (default), geojson, csv, ndjson

          alternatives: Number of alternative routes to return (0-3, default 0). When > 0, response is a
              FeatureCollection of route Features.

          annotations: Include per-edge annotations (speed, duration) on the route (default: false)

          depart_at: Departure time for traffic-aware routing (ISO 8601)

          ev: Electric vehicle parameters for EV-aware routing

          exclude: Comma-separated road types to exclude (e.g. `toll,motorway,ferry`)

          geometries: Geometry encoding format. Default: `geojson`.

          mode: Travel mode (default: `auto`)

          overview: Level of geometry detail: `full` (all points), `simplified` (Douglas-Peucker),
              `false` (no geometry). Default: `full`.

          steps: Include turn-by-turn navigation steps (default: false)

          traffic_model: Traffic prediction model (only used when `depart_at` is set)

          waypoints: Intermediate waypoints to visit in order (maximum 25)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/route",
            body=await async_maybe_transform(
                {
                    "destination": destination,
                    "origin": origin,
                    "alternatives": alternatives,
                    "annotations": annotations,
                    "depart_at": depart_at,
                    "ev": ev,
                    "exclude": exclude,
                    "geometries": geometries,
                    "mode": mode,
                    "overview": overview,
                    "steps": steps,
                    "traffic_model": traffic_model,
                    "waypoints": waypoints,
                },
                routing_route_params.RoutingRouteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"format": format}, routing_route_params.RoutingRouteParams),
            ),
            cast_to=RouteResult,
        )


class RoutingResourceWithRawResponse:
    def __init__(self, routing: RoutingResource) -> None:
        self._routing = routing

        self.isochrone = to_raw_response_wrapper(
            routing.isochrone,
        )
        self.matrix = to_raw_response_wrapper(
            routing.matrix,
        )
        self.nearest = to_raw_response_wrapper(
            routing.nearest,
        )
        self.route = to_raw_response_wrapper(
            routing.route,
        )


class AsyncRoutingResourceWithRawResponse:
    def __init__(self, routing: AsyncRoutingResource) -> None:
        self._routing = routing

        self.isochrone = async_to_raw_response_wrapper(
            routing.isochrone,
        )
        self.matrix = async_to_raw_response_wrapper(
            routing.matrix,
        )
        self.nearest = async_to_raw_response_wrapper(
            routing.nearest,
        )
        self.route = async_to_raw_response_wrapper(
            routing.route,
        )


class RoutingResourceWithStreamingResponse:
    def __init__(self, routing: RoutingResource) -> None:
        self._routing = routing

        self.isochrone = to_streamed_response_wrapper(
            routing.isochrone,
        )
        self.matrix = to_streamed_response_wrapper(
            routing.matrix,
        )
        self.nearest = to_streamed_response_wrapper(
            routing.nearest,
        )
        self.route = to_streamed_response_wrapper(
            routing.route,
        )


class AsyncRoutingResourceWithStreamingResponse:
    def __init__(self, routing: AsyncRoutingResource) -> None:
        self._routing = routing

        self.isochrone = async_to_streamed_response_wrapper(
            routing.isochrone,
        )
        self.matrix = async_to_streamed_response_wrapper(
            routing.matrix,
        )
        self.nearest = async_to_streamed_response_wrapper(
            routing.nearest,
        )
        self.route = async_to_streamed_response_wrapper(
            routing.route,
        )
