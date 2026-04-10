# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import elevation_lookup_params, elevation_profile_params
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
from ..types.elevation_lookup_result import ElevationLookupResult
from ..types.elevation_profile_result import ElevationProfileResult
from ..types.line_string_geometry_param import LineStringGeometryParam

__all__ = ["ElevationResource", "AsyncElevationResource"]


class ElevationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ElevationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plazafyi/plaza-python#accessing-raw-response-data-eg-headers
        """
        return ElevationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ElevationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plazafyi/plaza-python#with_streaming_response
        """
        return ElevationResourceWithStreamingResponse(self)

    def lookup(
        self,
        *,
        geometry: elevation_lookup_params.Geometry,
        format: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ElevationLookupResult:
        """
        Look up elevation at one or more points

        Args:
          geometry: Point or MultiPoint geometry to look up elevations for

          format: Response format: json (default), geojson, csv, ndjson

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/elevation",
            body=maybe_transform({"geometry": geometry}, elevation_lookup_params.ElevationLookupParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, elevation_lookup_params.ElevationLookupParams),
            ),
            cast_to=ElevationLookupResult,
        )

    def profile(
        self,
        *,
        geometry: LineStringGeometryParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ElevationProfileResult:
        """
        Elevation profile along coordinates

        Args:
          geometry: GeoJSON LineString geometry per RFC 7946. An ordered sequence of two or more
              positions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/elevation/profile",
            body=maybe_transform({"geometry": geometry}, elevation_profile_params.ElevationProfileParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ElevationProfileResult,
        )


class AsyncElevationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncElevationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plazafyi/plaza-python#accessing-raw-response-data-eg-headers
        """
        return AsyncElevationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncElevationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plazafyi/plaza-python#with_streaming_response
        """
        return AsyncElevationResourceWithStreamingResponse(self)

    async def lookup(
        self,
        *,
        geometry: elevation_lookup_params.Geometry,
        format: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ElevationLookupResult:
        """
        Look up elevation at one or more points

        Args:
          geometry: Point or MultiPoint geometry to look up elevations for

          format: Response format: json (default), geojson, csv, ndjson

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/elevation",
            body=await async_maybe_transform({"geometry": geometry}, elevation_lookup_params.ElevationLookupParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"format": format}, elevation_lookup_params.ElevationLookupParams),
            ),
            cast_to=ElevationLookupResult,
        )

    async def profile(
        self,
        *,
        geometry: LineStringGeometryParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ElevationProfileResult:
        """
        Elevation profile along coordinates

        Args:
          geometry: GeoJSON LineString geometry per RFC 7946. An ordered sequence of two or more
              positions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/elevation/profile",
            body=await async_maybe_transform({"geometry": geometry}, elevation_profile_params.ElevationProfileParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ElevationProfileResult,
        )


class ElevationResourceWithRawResponse:
    def __init__(self, elevation: ElevationResource) -> None:
        self._elevation = elevation

        self.lookup = to_raw_response_wrapper(
            elevation.lookup,
        )
        self.profile = to_raw_response_wrapper(
            elevation.profile,
        )


class AsyncElevationResourceWithRawResponse:
    def __init__(self, elevation: AsyncElevationResource) -> None:
        self._elevation = elevation

        self.lookup = async_to_raw_response_wrapper(
            elevation.lookup,
        )
        self.profile = async_to_raw_response_wrapper(
            elevation.profile,
        )


class ElevationResourceWithStreamingResponse:
    def __init__(self, elevation: ElevationResource) -> None:
        self._elevation = elevation

        self.lookup = to_streamed_response_wrapper(
            elevation.lookup,
        )
        self.profile = to_streamed_response_wrapper(
            elevation.profile,
        )


class AsyncElevationResourceWithStreamingResponse:
    def __init__(self, elevation: AsyncElevationResource) -> None:
        self._elevation = elevation

        self.lookup = async_to_streamed_response_wrapper(
            elevation.lookup,
        )
        self.profile = async_to_streamed_response_wrapper(
            elevation.profile,
        )
