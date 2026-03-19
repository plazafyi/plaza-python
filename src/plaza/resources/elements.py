# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import element_batch_params, element_query_params, element_nearby_params
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
from ..types.geo_json_feature import GeoJsonFeature
from ..types.feature_collection import FeatureCollection

__all__ = ["ElementsResource", "AsyncElementsResource"]


class ElementsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ElementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plazafyi/plaza-python#accessing-raw-response-data-eg-headers
        """
        return ElementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ElementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plazafyi/plaza-python#with_streaming_response
        """
        return ElementsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: int,
        *,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeoJsonFeature:
        """
        Get feature by type and ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        extra_headers = {"Accept": "application/geo+json", **(extra_headers or {})}
        return self._get(
            f"/api/v1/features/{type}/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GeoJsonFeature,
        )

    def batch(
        self,
        *,
        elements: Iterable[element_batch_params.Element],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """
        Fetch multiple features by type and ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/geo+json", **(extra_headers or {})}
        return self._post(
            "/api/v1/features/batch",
            body=maybe_transform({"elements": elements}, element_batch_params.ElementBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeatureCollection,
        )

    def nearby(
        self,
        *,
        lat: float,
        lng: float,
        limit: int | Omit = omit,
        radius: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """
        Find features near a geographic point

        Args:
          lat: Latitude (-90 to 90)

          lng: Longitude (-180 to 180)

          limit: Maximum results (default 20, max 100)

          radius: Search radius in meters (default 500, max 10000)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/geo+json", **(extra_headers or {})}
        return self._get(
            "/api/v1/features/nearby",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "lat": lat,
                        "lng": lng,
                        "limit": limit,
                        "radius": radius,
                    },
                    element_nearby_params.ElementNearbyParams,
                ),
            ),
            cast_to=FeatureCollection,
        )

    def query(
        self,
        *,
        bbox: str | Omit = omit,
        cursor: str | Omit = omit,
        h3: str | Omit = omit,
        limit: int | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """
        Query features by bounding box or H3 cell

        Args:
          bbox: Bounding box: south,west,north,east. At least one of bbox or h3 is required.

          cursor: Cursor for pagination

          h3: H3 cell index. At least one of bbox or h3 is required.

          limit: Maximum results (default 100, max 10000)

          type: Element types (comma-separated: node,way,relation)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/geo+json", **(extra_headers or {})}
        return self._get(
            "/api/v1/features",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bbox": bbox,
                        "cursor": cursor,
                        "h3": h3,
                        "limit": limit,
                        "type": type,
                    },
                    element_query_params.ElementQueryParams,
                ),
            ),
            cast_to=FeatureCollection,
        )


class AsyncElementsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncElementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plazafyi/plaza-python#accessing-raw-response-data-eg-headers
        """
        return AsyncElementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncElementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plazafyi/plaza-python#with_streaming_response
        """
        return AsyncElementsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: int,
        *,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeoJsonFeature:
        """
        Get feature by type and ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        extra_headers = {"Accept": "application/geo+json", **(extra_headers or {})}
        return await self._get(
            f"/api/v1/features/{type}/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GeoJsonFeature,
        )

    async def batch(
        self,
        *,
        elements: Iterable[element_batch_params.Element],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """
        Fetch multiple features by type and ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/geo+json", **(extra_headers or {})}
        return await self._post(
            "/api/v1/features/batch",
            body=await async_maybe_transform({"elements": elements}, element_batch_params.ElementBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeatureCollection,
        )

    async def nearby(
        self,
        *,
        lat: float,
        lng: float,
        limit: int | Omit = omit,
        radius: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """
        Find features near a geographic point

        Args:
          lat: Latitude (-90 to 90)

          lng: Longitude (-180 to 180)

          limit: Maximum results (default 20, max 100)

          radius: Search radius in meters (default 500, max 10000)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/geo+json", **(extra_headers or {})}
        return await self._get(
            "/api/v1/features/nearby",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "lat": lat,
                        "lng": lng,
                        "limit": limit,
                        "radius": radius,
                    },
                    element_nearby_params.ElementNearbyParams,
                ),
            ),
            cast_to=FeatureCollection,
        )

    async def query(
        self,
        *,
        bbox: str | Omit = omit,
        cursor: str | Omit = omit,
        h3: str | Omit = omit,
        limit: int | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """
        Query features by bounding box or H3 cell

        Args:
          bbox: Bounding box: south,west,north,east. At least one of bbox or h3 is required.

          cursor: Cursor for pagination

          h3: H3 cell index. At least one of bbox or h3 is required.

          limit: Maximum results (default 100, max 10000)

          type: Element types (comma-separated: node,way,relation)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/geo+json", **(extra_headers or {})}
        return await self._get(
            "/api/v1/features",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "bbox": bbox,
                        "cursor": cursor,
                        "h3": h3,
                        "limit": limit,
                        "type": type,
                    },
                    element_query_params.ElementQueryParams,
                ),
            ),
            cast_to=FeatureCollection,
        )


class ElementsResourceWithRawResponse:
    def __init__(self, elements: ElementsResource) -> None:
        self._elements = elements

        self.retrieve = to_raw_response_wrapper(
            elements.retrieve,
        )
        self.batch = to_raw_response_wrapper(
            elements.batch,
        )
        self.nearby = to_raw_response_wrapper(
            elements.nearby,
        )
        self.query = to_raw_response_wrapper(
            elements.query,
        )


class AsyncElementsResourceWithRawResponse:
    def __init__(self, elements: AsyncElementsResource) -> None:
        self._elements = elements

        self.retrieve = async_to_raw_response_wrapper(
            elements.retrieve,
        )
        self.batch = async_to_raw_response_wrapper(
            elements.batch,
        )
        self.nearby = async_to_raw_response_wrapper(
            elements.nearby,
        )
        self.query = async_to_raw_response_wrapper(
            elements.query,
        )


class ElementsResourceWithStreamingResponse:
    def __init__(self, elements: ElementsResource) -> None:
        self._elements = elements

        self.retrieve = to_streamed_response_wrapper(
            elements.retrieve,
        )
        self.batch = to_streamed_response_wrapper(
            elements.batch,
        )
        self.nearby = to_streamed_response_wrapper(
            elements.nearby,
        )
        self.query = to_streamed_response_wrapper(
            elements.query,
        )


class AsyncElementsResourceWithStreamingResponse:
    def __init__(self, elements: AsyncElementsResource) -> None:
        self._elements = elements

        self.retrieve = async_to_streamed_response_wrapper(
            elements.retrieve,
        )
        self.batch = async_to_streamed_response_wrapper(
            elements.batch,
        )
        self.nearby = async_to_streamed_response_wrapper(
            elements.nearby,
        )
        self.query = async_to_streamed_response_wrapper(
            elements.query,
        )
