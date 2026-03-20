# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import (
    element_batch_params,
    element_query_params,
    element_nearby_params,
    element_query_post_params,
    element_nearby_post_params,
)
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
          elements: Array of element references to fetch

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/features/batch",
            body=maybe_transform({"elements": elements}, element_batch_params.ElementBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeatureCollection,
        )

    def lookup(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeoJsonFeature:
        """Get feature by type and ID"""
        return self._post(
            "/api/v1/features/lookup",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GeoJsonFeature,
        )

    def nearby(
        self,
        *,
        lat: float | Omit = omit,
        limit: int | Omit = omit,
        lng: float | Omit = omit,
        near: str | Omit = omit,
        output_buffer: float | Omit = omit,
        output_centroid: bool | Omit = omit,
        output_fields: str | Omit = omit,
        output_geometry: bool | Omit = omit,
        output_include: str | Omit = omit,
        output_precision: int | Omit = omit,
        output_simplify: float | Omit = omit,
        output_sort: str | Omit = omit,
        radius: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """Find features near a geographic point

        Args:
          lat: Legacy shorthand.

        Latitude (-90 to 90). Use near param instead.

          limit: Maximum results (default 20, max 100)

          lng: Legacy shorthand. Longitude (-180 to 180). Use near param instead.

          near: Point geometry for proximity search (lat,lng or GeoJSON). Alternative to lat/lng
              params.

          output_buffer: Buffer geometry by meters

          output_centroid: Replace geometry with centroid

          output_fields: Comma-separated property fields to include

          output_geometry: Include geometry (default true)

          output_include: Extra computed fields: bbox, distance, center

          output_precision: Coordinate decimal precision (1-15, default 7)

          output_simplify: Simplify geometry tolerance in meters

          output_sort: Sort by: distance, name, osm_id

          radius: Search radius in meters (default 500, max 10000)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
                        "limit": limit,
                        "lng": lng,
                        "near": near,
                        "output_buffer": output_buffer,
                        "output_centroid": output_centroid,
                        "output_fields": output_fields,
                        "output_geometry": output_geometry,
                        "output_include": output_include,
                        "output_precision": output_precision,
                        "output_simplify": output_simplify,
                        "output_sort": output_sort,
                        "radius": radius,
                    },
                    element_nearby_params.ElementNearbyParams,
                ),
            ),
            cast_to=FeatureCollection,
        )

    def nearby_post(
        self,
        *,
        lat: float | Omit = omit,
        limit: int | Omit = omit,
        lng: float | Omit = omit,
        near: str | Omit = omit,
        output_buffer: float | Omit = omit,
        output_centroid: bool | Omit = omit,
        output_fields: str | Omit = omit,
        output_geometry: bool | Omit = omit,
        output_include: str | Omit = omit,
        output_precision: int | Omit = omit,
        output_simplify: float | Omit = omit,
        output_sort: str | Omit = omit,
        radius: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """Find features near a geographic point

        Args:
          lat: Legacy shorthand.

        Latitude (-90 to 90). Use near param instead.

          limit: Maximum results (default 20, max 100)

          lng: Legacy shorthand. Longitude (-180 to 180). Use near param instead.

          near: Point geometry for proximity search (lat,lng or GeoJSON). Alternative to lat/lng
              params.

          output_buffer: Buffer geometry by meters

          output_centroid: Replace geometry with centroid

          output_fields: Comma-separated property fields to include

          output_geometry: Include geometry (default true)

          output_include: Extra computed fields: bbox, distance, center

          output_precision: Coordinate decimal precision (1-15, default 7)

          output_simplify: Simplify geometry tolerance in meters

          output_sort: Sort by: distance, name, osm_id

          radius: Search radius in meters (default 500, max 10000)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/features/nearby",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "lat": lat,
                        "limit": limit,
                        "lng": lng,
                        "near": near,
                        "output_buffer": output_buffer,
                        "output_centroid": output_centroid,
                        "output_fields": output_fields,
                        "output_geometry": output_geometry,
                        "output_include": output_include,
                        "output_precision": output_precision,
                        "output_simplify": output_simplify,
                        "output_sort": output_sort,
                        "radius": radius,
                    },
                    element_nearby_post_params.ElementNearbyPostParams,
                ),
            ),
            cast_to=FeatureCollection,
        )

    def query(
        self,
        *,
        bbox: str | Omit = omit,
        contains: str | Omit = omit,
        crosses: str | Omit = omit,
        cursor: str | Omit = omit,
        h3: str | Omit = omit,
        intersects: str | Omit = omit,
        limit: int | Omit = omit,
        near: str | Omit = omit,
        output_buffer: float | Omit = omit,
        output_centroid: bool | Omit = omit,
        output_fields: str | Omit = omit,
        output_geometry: bool | Omit = omit,
        output_include: str | Omit = omit,
        output_precision: int | Omit = omit,
        output_simplify: float | Omit = omit,
        output_sort: str | Omit = omit,
        radius: float | Omit = omit,
        touches: str | Omit = omit,
        type: str | Omit = omit,
        within: str | Omit = omit,
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
          bbox: Legacy shorthand. Bounding box: south,west,north,east. Use spatial predicates
              (near, within, intersects) instead.

          contains: Geometry that features must contain

          crosses: Geometry that features must cross

          cursor: Cursor for pagination

          h3: Legacy shorthand. H3 cell index. Use spatial predicates instead.

          intersects: Geometry that features must intersect

          limit: Maximum results (default 100, max 10000)

          near: Point geometry for proximity search (lat,lng). Requires radius.

          output_buffer: Buffer geometry by meters

          output_centroid: Replace geometry with centroid

          output_fields: Comma-separated property fields to include

          output_geometry: Include geometry (default true)

          output_include: Extra computed fields: bbox, distance, center

          output_precision: Coordinate decimal precision (1-15, default 7)

          output_simplify: Simplify geometry tolerance in meters

          output_sort: Sort by: distance, name, osm_id

          radius: Search radius in meters (for near) or buffer distance (for other predicates)

          touches: Geometry that features must touch

          type: Element types (comma-separated: node,way,relation)

          within: Geometry that features must be within

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
                        "contains": contains,
                        "crosses": crosses,
                        "cursor": cursor,
                        "h3": h3,
                        "intersects": intersects,
                        "limit": limit,
                        "near": near,
                        "output_buffer": output_buffer,
                        "output_centroid": output_centroid,
                        "output_fields": output_fields,
                        "output_geometry": output_geometry,
                        "output_include": output_include,
                        "output_precision": output_precision,
                        "output_simplify": output_simplify,
                        "output_sort": output_sort,
                        "radius": radius,
                        "touches": touches,
                        "type": type,
                        "within": within,
                    },
                    element_query_params.ElementQueryParams,
                ),
            ),
            cast_to=FeatureCollection,
        )

    def query_post(
        self,
        *,
        bbox: str | Omit = omit,
        contains: str | Omit = omit,
        crosses: str | Omit = omit,
        cursor: str | Omit = omit,
        h3: str | Omit = omit,
        intersects: str | Omit = omit,
        limit: int | Omit = omit,
        near: str | Omit = omit,
        output_buffer: float | Omit = omit,
        output_centroid: bool | Omit = omit,
        output_fields: str | Omit = omit,
        output_geometry: bool | Omit = omit,
        output_include: str | Omit = omit,
        output_precision: int | Omit = omit,
        output_simplify: float | Omit = omit,
        output_sort: str | Omit = omit,
        radius: float | Omit = omit,
        touches: str | Omit = omit,
        type: str | Omit = omit,
        within: str | Omit = omit,
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
          bbox: Legacy shorthand. Bounding box: south,west,north,east. Use spatial predicates
              (near, within, intersects) instead.

          contains: Geometry that features must contain

          crosses: Geometry that features must cross

          cursor: Cursor for pagination

          h3: Legacy shorthand. H3 cell index. Use spatial predicates instead.

          intersects: Geometry that features must intersect

          limit: Maximum results (default 100, max 10000)

          near: Point geometry for proximity search (lat,lng). Requires radius.

          output_buffer: Buffer geometry by meters

          output_centroid: Replace geometry with centroid

          output_fields: Comma-separated property fields to include

          output_geometry: Include geometry (default true)

          output_include: Extra computed fields: bbox, distance, center

          output_precision: Coordinate decimal precision (1-15, default 7)

          output_simplify: Simplify geometry tolerance in meters

          output_sort: Sort by: distance, name, osm_id

          radius: Search radius in meters (for near) or buffer distance (for other predicates)

          touches: Geometry that features must touch

          type: Element types (comma-separated: node,way,relation)

          within: Geometry that features must be within

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/features",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bbox": bbox,
                        "contains": contains,
                        "crosses": crosses,
                        "cursor": cursor,
                        "h3": h3,
                        "intersects": intersects,
                        "limit": limit,
                        "near": near,
                        "output_buffer": output_buffer,
                        "output_centroid": output_centroid,
                        "output_fields": output_fields,
                        "output_geometry": output_geometry,
                        "output_include": output_include,
                        "output_precision": output_precision,
                        "output_simplify": output_simplify,
                        "output_sort": output_sort,
                        "radius": radius,
                        "touches": touches,
                        "type": type,
                        "within": within,
                    },
                    element_query_post_params.ElementQueryPostParams,
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
          elements: Array of element references to fetch

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/features/batch",
            body=await async_maybe_transform({"elements": elements}, element_batch_params.ElementBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeatureCollection,
        )

    async def lookup(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeoJsonFeature:
        """Get feature by type and ID"""
        return await self._post(
            "/api/v1/features/lookup",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GeoJsonFeature,
        )

    async def nearby(
        self,
        *,
        lat: float | Omit = omit,
        limit: int | Omit = omit,
        lng: float | Omit = omit,
        near: str | Omit = omit,
        output_buffer: float | Omit = omit,
        output_centroid: bool | Omit = omit,
        output_fields: str | Omit = omit,
        output_geometry: bool | Omit = omit,
        output_include: str | Omit = omit,
        output_precision: int | Omit = omit,
        output_simplify: float | Omit = omit,
        output_sort: str | Omit = omit,
        radius: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """Find features near a geographic point

        Args:
          lat: Legacy shorthand.

        Latitude (-90 to 90). Use near param instead.

          limit: Maximum results (default 20, max 100)

          lng: Legacy shorthand. Longitude (-180 to 180). Use near param instead.

          near: Point geometry for proximity search (lat,lng or GeoJSON). Alternative to lat/lng
              params.

          output_buffer: Buffer geometry by meters

          output_centroid: Replace geometry with centroid

          output_fields: Comma-separated property fields to include

          output_geometry: Include geometry (default true)

          output_include: Extra computed fields: bbox, distance, center

          output_precision: Coordinate decimal precision (1-15, default 7)

          output_simplify: Simplify geometry tolerance in meters

          output_sort: Sort by: distance, name, osm_id

          radius: Search radius in meters (default 500, max 10000)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
                        "limit": limit,
                        "lng": lng,
                        "near": near,
                        "output_buffer": output_buffer,
                        "output_centroid": output_centroid,
                        "output_fields": output_fields,
                        "output_geometry": output_geometry,
                        "output_include": output_include,
                        "output_precision": output_precision,
                        "output_simplify": output_simplify,
                        "output_sort": output_sort,
                        "radius": radius,
                    },
                    element_nearby_params.ElementNearbyParams,
                ),
            ),
            cast_to=FeatureCollection,
        )

    async def nearby_post(
        self,
        *,
        lat: float | Omit = omit,
        limit: int | Omit = omit,
        lng: float | Omit = omit,
        near: str | Omit = omit,
        output_buffer: float | Omit = omit,
        output_centroid: bool | Omit = omit,
        output_fields: str | Omit = omit,
        output_geometry: bool | Omit = omit,
        output_include: str | Omit = omit,
        output_precision: int | Omit = omit,
        output_simplify: float | Omit = omit,
        output_sort: str | Omit = omit,
        radius: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """Find features near a geographic point

        Args:
          lat: Legacy shorthand.

        Latitude (-90 to 90). Use near param instead.

          limit: Maximum results (default 20, max 100)

          lng: Legacy shorthand. Longitude (-180 to 180). Use near param instead.

          near: Point geometry for proximity search (lat,lng or GeoJSON). Alternative to lat/lng
              params.

          output_buffer: Buffer geometry by meters

          output_centroid: Replace geometry with centroid

          output_fields: Comma-separated property fields to include

          output_geometry: Include geometry (default true)

          output_include: Extra computed fields: bbox, distance, center

          output_precision: Coordinate decimal precision (1-15, default 7)

          output_simplify: Simplify geometry tolerance in meters

          output_sort: Sort by: distance, name, osm_id

          radius: Search radius in meters (default 500, max 10000)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/features/nearby",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "lat": lat,
                        "limit": limit,
                        "lng": lng,
                        "near": near,
                        "output_buffer": output_buffer,
                        "output_centroid": output_centroid,
                        "output_fields": output_fields,
                        "output_geometry": output_geometry,
                        "output_include": output_include,
                        "output_precision": output_precision,
                        "output_simplify": output_simplify,
                        "output_sort": output_sort,
                        "radius": radius,
                    },
                    element_nearby_post_params.ElementNearbyPostParams,
                ),
            ),
            cast_to=FeatureCollection,
        )

    async def query(
        self,
        *,
        bbox: str | Omit = omit,
        contains: str | Omit = omit,
        crosses: str | Omit = omit,
        cursor: str | Omit = omit,
        h3: str | Omit = omit,
        intersects: str | Omit = omit,
        limit: int | Omit = omit,
        near: str | Omit = omit,
        output_buffer: float | Omit = omit,
        output_centroid: bool | Omit = omit,
        output_fields: str | Omit = omit,
        output_geometry: bool | Omit = omit,
        output_include: str | Omit = omit,
        output_precision: int | Omit = omit,
        output_simplify: float | Omit = omit,
        output_sort: str | Omit = omit,
        radius: float | Omit = omit,
        touches: str | Omit = omit,
        type: str | Omit = omit,
        within: str | Omit = omit,
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
          bbox: Legacy shorthand. Bounding box: south,west,north,east. Use spatial predicates
              (near, within, intersects) instead.

          contains: Geometry that features must contain

          crosses: Geometry that features must cross

          cursor: Cursor for pagination

          h3: Legacy shorthand. H3 cell index. Use spatial predicates instead.

          intersects: Geometry that features must intersect

          limit: Maximum results (default 100, max 10000)

          near: Point geometry for proximity search (lat,lng). Requires radius.

          output_buffer: Buffer geometry by meters

          output_centroid: Replace geometry with centroid

          output_fields: Comma-separated property fields to include

          output_geometry: Include geometry (default true)

          output_include: Extra computed fields: bbox, distance, center

          output_precision: Coordinate decimal precision (1-15, default 7)

          output_simplify: Simplify geometry tolerance in meters

          output_sort: Sort by: distance, name, osm_id

          radius: Search radius in meters (for near) or buffer distance (for other predicates)

          touches: Geometry that features must touch

          type: Element types (comma-separated: node,way,relation)

          within: Geometry that features must be within

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
                        "contains": contains,
                        "crosses": crosses,
                        "cursor": cursor,
                        "h3": h3,
                        "intersects": intersects,
                        "limit": limit,
                        "near": near,
                        "output_buffer": output_buffer,
                        "output_centroid": output_centroid,
                        "output_fields": output_fields,
                        "output_geometry": output_geometry,
                        "output_include": output_include,
                        "output_precision": output_precision,
                        "output_simplify": output_simplify,
                        "output_sort": output_sort,
                        "radius": radius,
                        "touches": touches,
                        "type": type,
                        "within": within,
                    },
                    element_query_params.ElementQueryParams,
                ),
            ),
            cast_to=FeatureCollection,
        )

    async def query_post(
        self,
        *,
        bbox: str | Omit = omit,
        contains: str | Omit = omit,
        crosses: str | Omit = omit,
        cursor: str | Omit = omit,
        h3: str | Omit = omit,
        intersects: str | Omit = omit,
        limit: int | Omit = omit,
        near: str | Omit = omit,
        output_buffer: float | Omit = omit,
        output_centroid: bool | Omit = omit,
        output_fields: str | Omit = omit,
        output_geometry: bool | Omit = omit,
        output_include: str | Omit = omit,
        output_precision: int | Omit = omit,
        output_simplify: float | Omit = omit,
        output_sort: str | Omit = omit,
        radius: float | Omit = omit,
        touches: str | Omit = omit,
        type: str | Omit = omit,
        within: str | Omit = omit,
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
          bbox: Legacy shorthand. Bounding box: south,west,north,east. Use spatial predicates
              (near, within, intersects) instead.

          contains: Geometry that features must contain

          crosses: Geometry that features must cross

          cursor: Cursor for pagination

          h3: Legacy shorthand. H3 cell index. Use spatial predicates instead.

          intersects: Geometry that features must intersect

          limit: Maximum results (default 100, max 10000)

          near: Point geometry for proximity search (lat,lng). Requires radius.

          output_buffer: Buffer geometry by meters

          output_centroid: Replace geometry with centroid

          output_fields: Comma-separated property fields to include

          output_geometry: Include geometry (default true)

          output_include: Extra computed fields: bbox, distance, center

          output_precision: Coordinate decimal precision (1-15, default 7)

          output_simplify: Simplify geometry tolerance in meters

          output_sort: Sort by: distance, name, osm_id

          radius: Search radius in meters (for near) or buffer distance (for other predicates)

          touches: Geometry that features must touch

          type: Element types (comma-separated: node,way,relation)

          within: Geometry that features must be within

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/features",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "bbox": bbox,
                        "contains": contains,
                        "crosses": crosses,
                        "cursor": cursor,
                        "h3": h3,
                        "intersects": intersects,
                        "limit": limit,
                        "near": near,
                        "output_buffer": output_buffer,
                        "output_centroid": output_centroid,
                        "output_fields": output_fields,
                        "output_geometry": output_geometry,
                        "output_include": output_include,
                        "output_precision": output_precision,
                        "output_simplify": output_simplify,
                        "output_sort": output_sort,
                        "radius": radius,
                        "touches": touches,
                        "type": type,
                        "within": within,
                    },
                    element_query_post_params.ElementQueryPostParams,
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
        self.lookup = to_raw_response_wrapper(
            elements.lookup,
        )
        self.nearby = to_raw_response_wrapper(
            elements.nearby,
        )
        self.nearby_post = to_raw_response_wrapper(
            elements.nearby_post,
        )
        self.query = to_raw_response_wrapper(
            elements.query,
        )
        self.query_post = to_raw_response_wrapper(
            elements.query_post,
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
        self.lookup = async_to_raw_response_wrapper(
            elements.lookup,
        )
        self.nearby = async_to_raw_response_wrapper(
            elements.nearby,
        )
        self.nearby_post = async_to_raw_response_wrapper(
            elements.nearby_post,
        )
        self.query = async_to_raw_response_wrapper(
            elements.query,
        )
        self.query_post = async_to_raw_response_wrapper(
            elements.query_post,
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
        self.lookup = to_streamed_response_wrapper(
            elements.lookup,
        )
        self.nearby = to_streamed_response_wrapper(
            elements.nearby,
        )
        self.nearby_post = to_streamed_response_wrapper(
            elements.nearby_post,
        )
        self.query = to_streamed_response_wrapper(
            elements.query,
        )
        self.query_post = to_streamed_response_wrapper(
            elements.query_post,
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
        self.lookup = async_to_streamed_response_wrapper(
            elements.lookup,
        )
        self.nearby = async_to_streamed_response_wrapper(
            elements.nearby,
        )
        self.nearby_post = async_to_streamed_response_wrapper(
            elements.nearby_post,
        )
        self.query = async_to_streamed_response_wrapper(
            elements.query,
        )
        self.query_post = async_to_streamed_response_wrapper(
            elements.query_post,
        )
