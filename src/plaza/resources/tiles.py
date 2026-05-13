# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import path_template
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["TilesResource", "AsyncTilesResource"]


class TilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plazafyi/plaza-python#accessing-raw-response-data-eg-headers
        """
        return TilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plazafyi/plaza-python#with_streaming_response
        """
        return TilesResourceWithStreamingResponse(self)

    def get(
        self,
        y: int,
        *,
        z: int,
        x: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Get a Mapbox Vector Tile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.mapbox-vector-tile", **(extra_headers or {})}
        return self._get(
            path_template("/api/v1/tiles/{z}/{x}/{y}", z=z, x=x, y=y),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncTilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plazafyi/plaza-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plazafyi/plaza-python#with_streaming_response
        """
        return AsyncTilesResourceWithStreamingResponse(self)

    async def get(
        self,
        y: int,
        *,
        z: int,
        x: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Get a Mapbox Vector Tile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.mapbox-vector-tile", **(extra_headers or {})}
        return await self._get(
            path_template("/api/v1/tiles/{z}/{x}/{y}", z=z, x=x, y=y),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class TilesResourceWithRawResponse:
    def __init__(self, tiles: TilesResource) -> None:
        self._tiles = tiles

        self.get = to_custom_raw_response_wrapper(
            tiles.get,
            BinaryAPIResponse,
        )


class AsyncTilesResourceWithRawResponse:
    def __init__(self, tiles: AsyncTilesResource) -> None:
        self._tiles = tiles

        self.get = async_to_custom_raw_response_wrapper(
            tiles.get,
            AsyncBinaryAPIResponse,
        )


class TilesResourceWithStreamingResponse:
    def __init__(self, tiles: TilesResource) -> None:
        self._tiles = tiles

        self.get = to_custom_streamed_response_wrapper(
            tiles.get,
            StreamedBinaryAPIResponse,
        )


class AsyncTilesResourceWithStreamingResponse:
    def __init__(self, tiles: AsyncTilesResource) -> None:
        self._tiles = tiles

        self.get = async_to_custom_streamed_response_wrapper(
            tiles.get,
            AsyncStreamedBinaryAPIResponse,
        )
