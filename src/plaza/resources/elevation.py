# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import (
    elevation_batch_params,
    elevation_lookup_params,
    elevation_profile_params,
    elevation_lookup_post_params,
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
from ..types.elevation_batch_result import ElevationBatchResult
from ..types.elevation_lookup_result import ElevationLookupResult
from ..types.elevation_profile_result import ElevationProfileResult

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

    def batch(
        self,
        *,
        coordinates: Iterable[elevation_batch_params.Coordinate],
        format: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ElevationBatchResult:
        """
        Look up elevation for multiple coordinates

        Args:
          coordinates: Coordinates to look up elevations for (max 50)

          format: Response format: json (default), geojson, csv, ndjson

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/elevation/batch",
            body=maybe_transform({"coordinates": coordinates}, elevation_batch_params.ElevationBatchParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, elevation_batch_params.ElevationBatchParams),
            ),
            cast_to=ElevationBatchResult,
        )

    def lookup(
        self,
        *,
        format: str | Omit = omit,
        lat: float | Omit = omit,
        lng: float | Omit = omit,
        locations: str | Omit = omit,
        output_fields: str | Omit = omit,
        output_include: str | Omit = omit,
        output_precision: int | Omit = omit,
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
          format: Response format: json (default), geojson, csv, ndjson

          lat: Latitude (single point)

          lng: Longitude (single point)

          locations: Pipe-separated lng,lat pairs (batch)

          output_fields: Comma-separated property fields to include

          output_include: Extra computed fields: bbox, center

          output_precision: Coordinate decimal precision (1-15, default 7)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/elevation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "format": format,
                        "lat": lat,
                        "lng": lng,
                        "locations": locations,
                        "output_fields": output_fields,
                        "output_include": output_include,
                        "output_precision": output_precision,
                    },
                    elevation_lookup_params.ElevationLookupParams,
                ),
            ),
            cast_to=ElevationLookupResult,
        )

    def lookup_post(
        self,
        *,
        format: str | Omit = omit,
        lat: float | Omit = omit,
        lng: float | Omit = omit,
        locations: str | Omit = omit,
        output_fields: str | Omit = omit,
        output_include: str | Omit = omit,
        output_precision: int | Omit = omit,
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
          format: Response format: json (default), geojson, csv, ndjson

          lat: Latitude (single point)

          lng: Longitude (single point)

          locations: Pipe-separated lng,lat pairs (batch)

          output_fields: Comma-separated property fields to include

          output_include: Extra computed fields: bbox, center

          output_precision: Coordinate decimal precision (1-15, default 7)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/elevation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "format": format,
                        "lat": lat,
                        "lng": lng,
                        "locations": locations,
                        "output_fields": output_fields,
                        "output_include": output_include,
                        "output_precision": output_precision,
                    },
                    elevation_lookup_post_params.ElevationLookupPostParams,
                ),
            ),
            cast_to=ElevationLookupResult,
        )

    def profile(
        self,
        *,
        coordinates: Iterable[elevation_profile_params.Coordinate],
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
          coordinates: Path coordinates in order of travel (min 2, max 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/elevation/profile",
            body=maybe_transform({"coordinates": coordinates}, elevation_profile_params.ElevationProfileParams),
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

    async def batch(
        self,
        *,
        coordinates: Iterable[elevation_batch_params.Coordinate],
        format: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ElevationBatchResult:
        """
        Look up elevation for multiple coordinates

        Args:
          coordinates: Coordinates to look up elevations for (max 50)

          format: Response format: json (default), geojson, csv, ndjson

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/elevation/batch",
            body=await async_maybe_transform({"coordinates": coordinates}, elevation_batch_params.ElevationBatchParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"format": format}, elevation_batch_params.ElevationBatchParams),
            ),
            cast_to=ElevationBatchResult,
        )

    async def lookup(
        self,
        *,
        format: str | Omit = omit,
        lat: float | Omit = omit,
        lng: float | Omit = omit,
        locations: str | Omit = omit,
        output_fields: str | Omit = omit,
        output_include: str | Omit = omit,
        output_precision: int | Omit = omit,
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
          format: Response format: json (default), geojson, csv, ndjson

          lat: Latitude (single point)

          lng: Longitude (single point)

          locations: Pipe-separated lng,lat pairs (batch)

          output_fields: Comma-separated property fields to include

          output_include: Extra computed fields: bbox, center

          output_precision: Coordinate decimal precision (1-15, default 7)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/elevation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "format": format,
                        "lat": lat,
                        "lng": lng,
                        "locations": locations,
                        "output_fields": output_fields,
                        "output_include": output_include,
                        "output_precision": output_precision,
                    },
                    elevation_lookup_params.ElevationLookupParams,
                ),
            ),
            cast_to=ElevationLookupResult,
        )

    async def lookup_post(
        self,
        *,
        format: str | Omit = omit,
        lat: float | Omit = omit,
        lng: float | Omit = omit,
        locations: str | Omit = omit,
        output_fields: str | Omit = omit,
        output_include: str | Omit = omit,
        output_precision: int | Omit = omit,
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
          format: Response format: json (default), geojson, csv, ndjson

          lat: Latitude (single point)

          lng: Longitude (single point)

          locations: Pipe-separated lng,lat pairs (batch)

          output_fields: Comma-separated property fields to include

          output_include: Extra computed fields: bbox, center

          output_precision: Coordinate decimal precision (1-15, default 7)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/elevation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "format": format,
                        "lat": lat,
                        "lng": lng,
                        "locations": locations,
                        "output_fields": output_fields,
                        "output_include": output_include,
                        "output_precision": output_precision,
                    },
                    elevation_lookup_post_params.ElevationLookupPostParams,
                ),
            ),
            cast_to=ElevationLookupResult,
        )

    async def profile(
        self,
        *,
        coordinates: Iterable[elevation_profile_params.Coordinate],
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
          coordinates: Path coordinates in order of travel (min 2, max 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/elevation/profile",
            body=await async_maybe_transform(
                {"coordinates": coordinates}, elevation_profile_params.ElevationProfileParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ElevationProfileResult,
        )


class ElevationResourceWithRawResponse:
    def __init__(self, elevation: ElevationResource) -> None:
        self._elevation = elevation

        self.batch = to_raw_response_wrapper(
            elevation.batch,
        )
        self.lookup = to_raw_response_wrapper(
            elevation.lookup,
        )
        self.lookup_post = to_raw_response_wrapper(
            elevation.lookup_post,
        )
        self.profile = to_raw_response_wrapper(
            elevation.profile,
        )


class AsyncElevationResourceWithRawResponse:
    def __init__(self, elevation: AsyncElevationResource) -> None:
        self._elevation = elevation

        self.batch = async_to_raw_response_wrapper(
            elevation.batch,
        )
        self.lookup = async_to_raw_response_wrapper(
            elevation.lookup,
        )
        self.lookup_post = async_to_raw_response_wrapper(
            elevation.lookup_post,
        )
        self.profile = async_to_raw_response_wrapper(
            elevation.profile,
        )


class ElevationResourceWithStreamingResponse:
    def __init__(self, elevation: ElevationResource) -> None:
        self._elevation = elevation

        self.batch = to_streamed_response_wrapper(
            elevation.batch,
        )
        self.lookup = to_streamed_response_wrapper(
            elevation.lookup,
        )
        self.lookup_post = to_streamed_response_wrapper(
            elevation.lookup_post,
        )
        self.profile = to_streamed_response_wrapper(
            elevation.profile,
        )


class AsyncElevationResourceWithStreamingResponse:
    def __init__(self, elevation: AsyncElevationResource) -> None:
        self._elevation = elevation

        self.batch = async_to_streamed_response_wrapper(
            elevation.batch,
        )
        self.lookup = async_to_streamed_response_wrapper(
            elevation.lookup,
        )
        self.lookup_post = async_to_streamed_response_wrapper(
            elevation.lookup_post,
        )
        self.profile = async_to_streamed_response_wrapper(
            elevation.profile,
        )
