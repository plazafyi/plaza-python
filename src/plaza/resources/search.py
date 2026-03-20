# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import search_query_params, search_query_post_params
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
from ..types.feature_collection import FeatureCollection

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plazafyi/plaza-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plazafyi/plaza-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def query(
        self,
        *,
        q: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        output_fields: str | Omit = omit,
        output_include: str | Omit = omit,
        output_precision: int | Omit = omit,
        output_sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """
        Search OSM features by name

        Args:
          q: Search query string

          cursor: Cursor for pagination

          limit: Maximum results (default 25, max 100)

          output_fields: Comma-separated property fields to include

          output_include: Extra computed fields: bbox, distance, center

          output_precision: Coordinate decimal precision (1-15, default 7)

          output_sort: Sort by: distance, name, osm_id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "cursor": cursor,
                        "limit": limit,
                        "output_fields": output_fields,
                        "output_include": output_include,
                        "output_precision": output_precision,
                        "output_sort": output_sort,
                    },
                    search_query_params.SearchQueryParams,
                ),
            ),
            cast_to=FeatureCollection,
        )

    def query_post(
        self,
        *,
        q: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        output_fields: str | Omit = omit,
        output_include: str | Omit = omit,
        output_precision: int | Omit = omit,
        output_sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """
        Search OSM features by name

        Args:
          q: Search query string

          cursor: Cursor for pagination

          limit: Maximum results (default 25, max 100)

          output_fields: Comma-separated property fields to include

          output_include: Extra computed fields: bbox, distance, center

          output_precision: Coordinate decimal precision (1-15, default 7)

          output_sort: Sort by: distance, name, osm_id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "cursor": cursor,
                        "limit": limit,
                        "output_fields": output_fields,
                        "output_include": output_include,
                        "output_precision": output_precision,
                        "output_sort": output_sort,
                    },
                    search_query_post_params.SearchQueryPostParams,
                ),
            ),
            cast_to=FeatureCollection,
        )


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plazafyi/plaza-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plazafyi/plaza-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def query(
        self,
        *,
        q: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        output_fields: str | Omit = omit,
        output_include: str | Omit = omit,
        output_precision: int | Omit = omit,
        output_sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """
        Search OSM features by name

        Args:
          q: Search query string

          cursor: Cursor for pagination

          limit: Maximum results (default 25, max 100)

          output_fields: Comma-separated property fields to include

          output_include: Extra computed fields: bbox, distance, center

          output_precision: Coordinate decimal precision (1-15, default 7)

          output_sort: Sort by: distance, name, osm_id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "cursor": cursor,
                        "limit": limit,
                        "output_fields": output_fields,
                        "output_include": output_include,
                        "output_precision": output_precision,
                        "output_sort": output_sort,
                    },
                    search_query_params.SearchQueryParams,
                ),
            ),
            cast_to=FeatureCollection,
        )

    async def query_post(
        self,
        *,
        q: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        output_fields: str | Omit = omit,
        output_include: str | Omit = omit,
        output_precision: int | Omit = omit,
        output_sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """
        Search OSM features by name

        Args:
          q: Search query string

          cursor: Cursor for pagination

          limit: Maximum results (default 25, max 100)

          output_fields: Comma-separated property fields to include

          output_include: Extra computed fields: bbox, distance, center

          output_precision: Coordinate decimal precision (1-15, default 7)

          output_sort: Sort by: distance, name, osm_id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "cursor": cursor,
                        "limit": limit,
                        "output_fields": output_fields,
                        "output_include": output_include,
                        "output_precision": output_precision,
                        "output_sort": output_sort,
                    },
                    search_query_post_params.SearchQueryPostParams,
                ),
            ),
            cast_to=FeatureCollection,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.query = to_raw_response_wrapper(
            search.query,
        )
        self.query_post = to_raw_response_wrapper(
            search.query_post,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.query = async_to_raw_response_wrapper(
            search.query,
        )
        self.query_post = async_to_raw_response_wrapper(
            search.query_post,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.query = to_streamed_response_wrapper(
            search.query,
        )
        self.query_post = to_streamed_response_wrapper(
            search.query_post,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.query = async_to_streamed_response_wrapper(
            search.query,
        )
        self.query_post = async_to_streamed_response_wrapper(
            search.query_post,
        )
