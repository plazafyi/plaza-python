# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import feature_batch_params, feature_query_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.geometry_param import GeometryParam
from ..types.geo_json_feature import GeoJsonFeature
from ..types.feature_collection import FeatureCollection

__all__ = ["FeaturesResource", "AsyncFeaturesResource"]


class FeaturesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FeaturesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plazafyi/plaza-python#accessing-raw-response-data-eg-headers
        """
        return FeaturesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeaturesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plazafyi/plaza-python#with_streaming_response
        """
        return FeaturesResourceWithStreamingResponse(self)

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
        return self._get(
            path_template("/api/v1/features/{type}/{id}", type=type, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GeoJsonFeature,
        )

    def batch(
        self,
        *,
        elements: Iterable[feature_batch_params.Element],
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
          elements: Array of element references to fetch

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/features/batch",
            body=maybe_transform({"elements": elements}, feature_batch_params.FeatureBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeatureCollection,
        )

    def query(
        self,
        *,
        cursor: str | Omit = omit,
        format: str | Omit = omit,
        h3: str | Omit = omit,
        limit: int | Omit = omit,
        type: str | Omit = omit,
        around: GeometryParam | Omit = omit,
        contains: GeometryParam | Omit = omit,
        crosses: GeometryParam | Omit = omit,
        intersects: GeometryParam | Omit = omit,
        not_contains: GeometryParam | Omit = omit,
        not_intersects: GeometryParam | Omit = omit,
        not_within: GeometryParam | Omit = omit,
        radius: float | Omit = omit,
        touches: GeometryParam | Omit = omit,
        within: GeometryParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """
        Query features by spatial predicate, bounding box, or H3 cell

        Args:
          cursor: Cursor for pagination

          format: Response format. json (default) returns paginated GeoJSON. geojson/csv/ndjson
              stream via chunked transfer encoding.

          h3: Legacy shorthand. H3 cell index. Use spatial predicates instead.

          limit: Maximum results (default 100, max 10000)

          type: Element types (comma-separated: node,way,relation)

          around: GeoJSON Geometry object per RFC 7946. Discriminated union — the `type` field
              determines the coordinate structure.

          contains: GeoJSON Geometry object per RFC 7946. Discriminated union — the `type` field
              determines the coordinate structure.

          crosses: GeoJSON Geometry object per RFC 7946. Discriminated union — the `type` field
              determines the coordinate structure.

          intersects: GeoJSON Geometry object per RFC 7946. Discriminated union — the `type` field
              determines the coordinate structure.

          not_contains: GeoJSON Geometry object per RFC 7946. Discriminated union — the `type` field
              determines the coordinate structure.

          not_intersects: GeoJSON Geometry object per RFC 7946. Discriminated union — the `type` field
              determines the coordinate structure.

          not_within: GeoJSON Geometry object per RFC 7946. Discriminated union — the `type` field
              determines the coordinate structure.

          radius: Search radius in meters. Required for `around`, optional buffer for other
              predicates.

          touches: GeoJSON Geometry object per RFC 7946. Discriminated union — the `type` field
              determines the coordinate structure.

          within: GeoJSON Geometry object per RFC 7946. Discriminated union — the `type` field
              determines the coordinate structure.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/features",
            body=maybe_transform(
                {
                    "around": around,
                    "contains": contains,
                    "crosses": crosses,
                    "intersects": intersects,
                    "not_contains": not_contains,
                    "not_intersects": not_intersects,
                    "not_within": not_within,
                    "radius": radius,
                    "touches": touches,
                    "within": within,
                },
                feature_query_params.FeatureQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "format": format,
                        "h3": h3,
                        "limit": limit,
                        "type": type,
                    },
                    feature_query_params.FeatureQueryParams,
                ),
            ),
            cast_to=FeatureCollection,
        )


class AsyncFeaturesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFeaturesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plazafyi/plaza-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFeaturesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeaturesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plazafyi/plaza-python#with_streaming_response
        """
        return AsyncFeaturesResourceWithStreamingResponse(self)

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
        return await self._get(
            path_template("/api/v1/features/{type}/{id}", type=type, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GeoJsonFeature,
        )

    async def batch(
        self,
        *,
        elements: Iterable[feature_batch_params.Element],
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
          elements: Array of element references to fetch

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/features/batch",
            body=await async_maybe_transform({"elements": elements}, feature_batch_params.FeatureBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeatureCollection,
        )

    async def query(
        self,
        *,
        cursor: str | Omit = omit,
        format: str | Omit = omit,
        h3: str | Omit = omit,
        limit: int | Omit = omit,
        type: str | Omit = omit,
        around: GeometryParam | Omit = omit,
        contains: GeometryParam | Omit = omit,
        crosses: GeometryParam | Omit = omit,
        intersects: GeometryParam | Omit = omit,
        not_contains: GeometryParam | Omit = omit,
        not_intersects: GeometryParam | Omit = omit,
        not_within: GeometryParam | Omit = omit,
        radius: float | Omit = omit,
        touches: GeometryParam | Omit = omit,
        within: GeometryParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """
        Query features by spatial predicate, bounding box, or H3 cell

        Args:
          cursor: Cursor for pagination

          format: Response format. json (default) returns paginated GeoJSON. geojson/csv/ndjson
              stream via chunked transfer encoding.

          h3: Legacy shorthand. H3 cell index. Use spatial predicates instead.

          limit: Maximum results (default 100, max 10000)

          type: Element types (comma-separated: node,way,relation)

          around: GeoJSON Geometry object per RFC 7946. Discriminated union — the `type` field
              determines the coordinate structure.

          contains: GeoJSON Geometry object per RFC 7946. Discriminated union — the `type` field
              determines the coordinate structure.

          crosses: GeoJSON Geometry object per RFC 7946. Discriminated union — the `type` field
              determines the coordinate structure.

          intersects: GeoJSON Geometry object per RFC 7946. Discriminated union — the `type` field
              determines the coordinate structure.

          not_contains: GeoJSON Geometry object per RFC 7946. Discriminated union — the `type` field
              determines the coordinate structure.

          not_intersects: GeoJSON Geometry object per RFC 7946. Discriminated union — the `type` field
              determines the coordinate structure.

          not_within: GeoJSON Geometry object per RFC 7946. Discriminated union — the `type` field
              determines the coordinate structure.

          radius: Search radius in meters. Required for `around`, optional buffer for other
              predicates.

          touches: GeoJSON Geometry object per RFC 7946. Discriminated union — the `type` field
              determines the coordinate structure.

          within: GeoJSON Geometry object per RFC 7946. Discriminated union — the `type` field
              determines the coordinate structure.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/features",
            body=await async_maybe_transform(
                {
                    "around": around,
                    "contains": contains,
                    "crosses": crosses,
                    "intersects": intersects,
                    "not_contains": not_contains,
                    "not_intersects": not_intersects,
                    "not_within": not_within,
                    "radius": radius,
                    "touches": touches,
                    "within": within,
                },
                feature_query_params.FeatureQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "format": format,
                        "h3": h3,
                        "limit": limit,
                        "type": type,
                    },
                    feature_query_params.FeatureQueryParams,
                ),
            ),
            cast_to=FeatureCollection,
        )


class FeaturesResourceWithRawResponse:
    def __init__(self, features: FeaturesResource) -> None:
        self._features = features

        self.retrieve = to_raw_response_wrapper(
            features.retrieve,
        )
        self.batch = to_raw_response_wrapper(
            features.batch,
        )
        self.query = to_raw_response_wrapper(
            features.query,
        )


class AsyncFeaturesResourceWithRawResponse:
    def __init__(self, features: AsyncFeaturesResource) -> None:
        self._features = features

        self.retrieve = async_to_raw_response_wrapper(
            features.retrieve,
        )
        self.batch = async_to_raw_response_wrapper(
            features.batch,
        )
        self.query = async_to_raw_response_wrapper(
            features.query,
        )


class FeaturesResourceWithStreamingResponse:
    def __init__(self, features: FeaturesResource) -> None:
        self._features = features

        self.retrieve = to_streamed_response_wrapper(
            features.retrieve,
        )
        self.batch = to_streamed_response_wrapper(
            features.batch,
        )
        self.query = to_streamed_response_wrapper(
            features.query,
        )


class AsyncFeaturesResourceWithStreamingResponse:
    def __init__(self, features: AsyncFeaturesResource) -> None:
        self._features = features

        self.retrieve = async_to_streamed_response_wrapper(
            features.retrieve,
        )
        self.batch = async_to_streamed_response_wrapper(
            features.batch,
        )
        self.query = async_to_streamed_response_wrapper(
            features.query,
        )
