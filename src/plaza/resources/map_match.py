# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import map_match_match_params
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
from ..types.map_match_result import MapMatchResult
from ..types.line_string_geometry_param import LineStringGeometryParam

__all__ = ["MapMatchResource", "AsyncMapMatchResource"]


class MapMatchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MapMatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plazafyi/plaza-python#accessing-raw-response-data-eg-headers
        """
        return MapMatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MapMatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plazafyi/plaza-python#with_streaming_response
        """
        return MapMatchResourceWithStreamingResponse(self)

    def match(
        self,
        *,
        geometry: LineStringGeometryParam,
        radiuses: Optional[Iterable[float]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MapMatchResult:
        """
        Match GPS coordinates to the road network

        Args:
          geometry: GeoJSON LineString geometry per RFC 7946. An ordered sequence of two or more
              positions.

          radiuses: Search radius per coordinate in meters. Must have the same length as the
              geometry coordinates or be omitted entirely. Default: 50m per point.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/map-match",
            body=maybe_transform(
                {
                    "geometry": geometry,
                    "radiuses": radiuses,
                },
                map_match_match_params.MapMatchMatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MapMatchResult,
        )


class AsyncMapMatchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMapMatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plazafyi/plaza-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMapMatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMapMatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plazafyi/plaza-python#with_streaming_response
        """
        return AsyncMapMatchResourceWithStreamingResponse(self)

    async def match(
        self,
        *,
        geometry: LineStringGeometryParam,
        radiuses: Optional[Iterable[float]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MapMatchResult:
        """
        Match GPS coordinates to the road network

        Args:
          geometry: GeoJSON LineString geometry per RFC 7946. An ordered sequence of two or more
              positions.

          radiuses: Search radius per coordinate in meters. Must have the same length as the
              geometry coordinates or be omitted entirely. Default: 50m per point.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/map-match",
            body=await async_maybe_transform(
                {
                    "geometry": geometry,
                    "radiuses": radiuses,
                },
                map_match_match_params.MapMatchMatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MapMatchResult,
        )


class MapMatchResourceWithRawResponse:
    def __init__(self, map_match: MapMatchResource) -> None:
        self._map_match = map_match

        self.match = to_raw_response_wrapper(
            map_match.match,
        )


class AsyncMapMatchResourceWithRawResponse:
    def __init__(self, map_match: AsyncMapMatchResource) -> None:
        self._map_match = map_match

        self.match = async_to_raw_response_wrapper(
            map_match.match,
        )


class MapMatchResourceWithStreamingResponse:
    def __init__(self, map_match: MapMatchResource) -> None:
        self._map_match = map_match

        self.match = to_streamed_response_wrapper(
            map_match.match,
        )


class AsyncMapMatchResourceWithStreamingResponse:
    def __init__(self, map_match: AsyncMapMatchResource) -> None:
        self._map_match = map_match

        self.match = async_to_streamed_response_wrapper(
            map_match.match,
        )
