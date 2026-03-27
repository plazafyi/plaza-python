# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ..types.geo_json_feature import GeoJsonFeature
from ..types.geo_json_geometry_param import GeoJsonGeometryParam

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
        lat: float,
        lng: float,
        time: float,
        mode: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeoJsonFeature:
        """
        Calculate an isochrone from a point

        Args:
          lat: Latitude

          lng: Longitude

          time: Travel time in seconds (1-7200)

          mode: Travel mode (auto, foot, bicycle)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/geo+json", **(extra_headers or {})}
        return self._get(
            "/api/v1/isochrone",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "lat": lat,
                        "lng": lng,
                        "time": time,
                        "mode": mode,
                    },
                    routing_isochrone_params.RoutingIsochroneParams,
                ),
            ),
            cast_to=GeoJsonFeature,
        )

    def matrix(
        self,
        *,
        destinations: GeoJsonGeometryParam,
        origins: GeoJsonGeometryParam,
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
          destinations: Destination points (GeoJSON MultiPoint geometry)

          origins: Origin points (GeoJSON MultiPoint geometry)

          mode: Travel mode

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
        lat: float,
        lng: float,
        radius: int | Omit = omit,
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
          lat: Latitude

          lng: Longitude

          radius: Search radius in meters (default 500, max 5000)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/nearest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "lat": lat,
                        "lng": lng,
                        "radius": radius,
                    },
                    routing_nearest_params.RoutingNearestParams,
                ),
            ),
            cast_to=NearestResult,
        )

    def route(
        self,
        *,
        destination: GeoJsonGeometryParam,
        origin: GeoJsonGeometryParam,
        mode: Literal["auto", "foot", "bicycle"] | Omit = omit,
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
          destination: Destination point (GeoJSON Point geometry)

          origin: Origin point (GeoJSON Point geometry)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/geo+json", **(extra_headers or {})}
        return self._post(
            "/api/v1/route",
            body=maybe_transform(
                {
                    "destination": destination,
                    "origin": origin,
                    "mode": mode,
                },
                routing_route_params.RoutingRouteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        lat: float,
        lng: float,
        time: float,
        mode: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeoJsonFeature:
        """
        Calculate an isochrone from a point

        Args:
          lat: Latitude

          lng: Longitude

          time: Travel time in seconds (1-7200)

          mode: Travel mode (auto, foot, bicycle)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/geo+json", **(extra_headers or {})}
        return await self._get(
            "/api/v1/isochrone",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "lat": lat,
                        "lng": lng,
                        "time": time,
                        "mode": mode,
                    },
                    routing_isochrone_params.RoutingIsochroneParams,
                ),
            ),
            cast_to=GeoJsonFeature,
        )

    async def matrix(
        self,
        *,
        destinations: GeoJsonGeometryParam,
        origins: GeoJsonGeometryParam,
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
          destinations: Destination points (GeoJSON MultiPoint geometry)

          origins: Origin points (GeoJSON MultiPoint geometry)

          mode: Travel mode

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
        lat: float,
        lng: float,
        radius: int | Omit = omit,
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
          lat: Latitude

          lng: Longitude

          radius: Search radius in meters (default 500, max 5000)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/nearest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "lat": lat,
                        "lng": lng,
                        "radius": radius,
                    },
                    routing_nearest_params.RoutingNearestParams,
                ),
            ),
            cast_to=NearestResult,
        )

    async def route(
        self,
        *,
        destination: GeoJsonGeometryParam,
        origin: GeoJsonGeometryParam,
        mode: Literal["auto", "foot", "bicycle"] | Omit = omit,
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
          destination: Destination point (GeoJSON Point geometry)

          origin: Origin point (GeoJSON Point geometry)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/geo+json", **(extra_headers or {})}
        return await self._post(
            "/api/v1/route",
            body=await async_maybe_transform(
                {
                    "destination": destination,
                    "origin": origin,
                    "mode": mode,
                },
                routing_route_params.RoutingRouteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
