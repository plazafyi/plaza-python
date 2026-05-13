# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    geocode_batch_params,
    geocode_forward_params,
    geocode_reverse_params,
    geocode_autocomplete_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.geocode_result import GeocodeResult
from ..types.autocomplete_result import AutocompleteResult
from ..types.point_geometry_param import PointGeometryParam
from ..types.geocode_batch_response import GeocodeBatchResponse
from ..types.reverse_geocode_result import ReverseGeocodeResult

__all__ = ["GeocodeResource", "AsyncGeocodeResource"]


class GeocodeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GeocodeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plazafyi/plaza-python#accessing-raw-response-data-eg-headers
        """
        return GeocodeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GeocodeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plazafyi/plaza-python#with_streaming_response
        """
        return GeocodeResourceWithStreamingResponse(self)

    def autocomplete(
        self,
        *,
        q: str,
        format: str | Omit = omit,
        country_code: Optional[str] | Omit = omit,
        focus: Optional[PointGeometryParam] | Omit = omit,
        lang: Optional[str] | Omit = omit,
        layer: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteResult:
        """
        Autocomplete a partial address

        Args:
          q: Partial address or place name input

          format: Response format: json (default), geojson, csv, ndjson

          country_code: ISO 3166-1 alpha-2 country code to restrict results

          focus: GeoJSON Point geometry per RFC 7946. Coordinates use [longitude, latitude]
              order. Optional third element is altitude in meters.

          lang: Preferred response language (ISO 639-1)

          layer: Filter by result layer (e.g. `address`, `place`, `poi`)

          limit: Maximum number of suggestions (default: 5, max: 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/geocode/autocomplete",
            body=maybe_transform(
                {
                    "q": q,
                    "country_code": country_code,
                    "focus": focus,
                    "lang": lang,
                    "layer": layer,
                    "limit": limit,
                },
                geocode_autocomplete_params.GeocodeAutocompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, geocode_autocomplete_params.GeocodeAutocompleteParams),
            ),
            cast_to=AutocompleteResult,
        )

    def batch(
        self,
        *,
        addresses: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeocodeBatchResponse:
        """
        Batch geocode multiple addresses

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/geocode/batch",
            body=maybe_transform({"addresses": addresses}, geocode_batch_params.GeocodeBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GeocodeBatchResponse,
        )

    def forward(
        self,
        *,
        q: str,
        format: str | Omit = omit,
        country_code: Optional[str] | Omit = omit,
        focus: Optional[PointGeometryParam] | Omit = omit,
        lang: Optional[str] | Omit = omit,
        layer: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeocodeResult:
        """
        Forward geocode an address

        Args:
          q: Address or place name to geocode

          format: Response format: json (default), geojson, csv, ndjson

          country_code: ISO 3166-1 alpha-2 country code to restrict results

          focus: GeoJSON Point geometry per RFC 7946. Coordinates use [longitude, latitude]
              order. Optional third element is altitude in meters.

          lang: Preferred response language (ISO 639-1)

          layer: Filter by result layer (e.g. `address`, `place`, `poi`)

          limit: Maximum number of results (default: 5, max: 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/geocode",
            body=maybe_transform(
                {
                    "q": q,
                    "country_code": country_code,
                    "focus": focus,
                    "lang": lang,
                    "layer": layer,
                    "limit": limit,
                },
                geocode_forward_params.GeocodeForwardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, geocode_forward_params.GeocodeForwardParams),
            ),
            cast_to=GeocodeResult,
        )

    def reverse(
        self,
        *,
        geometry: PointGeometryParam,
        format: str | Omit = omit,
        lang: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        radius: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReverseGeocodeResult:
        """
        Reverse geocode a coordinate

        Args:
          geometry: GeoJSON Point geometry per RFC 7946. Coordinates use [longitude, latitude]
              order. Optional third element is altitude in meters.

          format: Response format: json (default), geojson, csv, ndjson

          lang: Preferred response language (ISO 639-1)

          limit: Maximum number of results (default: 1, max: 50)

          radius: Search radius in meters (default: 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/geocode/reverse",
            body=maybe_transform(
                {
                    "geometry": geometry,
                    "lang": lang,
                    "limit": limit,
                    "radius": radius,
                },
                geocode_reverse_params.GeocodeReverseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, geocode_reverse_params.GeocodeReverseParams),
            ),
            cast_to=ReverseGeocodeResult,
        )


class AsyncGeocodeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGeocodeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plazafyi/plaza-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGeocodeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGeocodeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plazafyi/plaza-python#with_streaming_response
        """
        return AsyncGeocodeResourceWithStreamingResponse(self)

    async def autocomplete(
        self,
        *,
        q: str,
        format: str | Omit = omit,
        country_code: Optional[str] | Omit = omit,
        focus: Optional[PointGeometryParam] | Omit = omit,
        lang: Optional[str] | Omit = omit,
        layer: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteResult:
        """
        Autocomplete a partial address

        Args:
          q: Partial address or place name input

          format: Response format: json (default), geojson, csv, ndjson

          country_code: ISO 3166-1 alpha-2 country code to restrict results

          focus: GeoJSON Point geometry per RFC 7946. Coordinates use [longitude, latitude]
              order. Optional third element is altitude in meters.

          lang: Preferred response language (ISO 639-1)

          layer: Filter by result layer (e.g. `address`, `place`, `poi`)

          limit: Maximum number of suggestions (default: 5, max: 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/geocode/autocomplete",
            body=await async_maybe_transform(
                {
                    "q": q,
                    "country_code": country_code,
                    "focus": focus,
                    "lang": lang,
                    "layer": layer,
                    "limit": limit,
                },
                geocode_autocomplete_params.GeocodeAutocompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"format": format}, geocode_autocomplete_params.GeocodeAutocompleteParams
                ),
            ),
            cast_to=AutocompleteResult,
        )

    async def batch(
        self,
        *,
        addresses: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeocodeBatchResponse:
        """
        Batch geocode multiple addresses

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/geocode/batch",
            body=await async_maybe_transform({"addresses": addresses}, geocode_batch_params.GeocodeBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GeocodeBatchResponse,
        )

    async def forward(
        self,
        *,
        q: str,
        format: str | Omit = omit,
        country_code: Optional[str] | Omit = omit,
        focus: Optional[PointGeometryParam] | Omit = omit,
        lang: Optional[str] | Omit = omit,
        layer: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeocodeResult:
        """
        Forward geocode an address

        Args:
          q: Address or place name to geocode

          format: Response format: json (default), geojson, csv, ndjson

          country_code: ISO 3166-1 alpha-2 country code to restrict results

          focus: GeoJSON Point geometry per RFC 7946. Coordinates use [longitude, latitude]
              order. Optional third element is altitude in meters.

          lang: Preferred response language (ISO 639-1)

          layer: Filter by result layer (e.g. `address`, `place`, `poi`)

          limit: Maximum number of results (default: 5, max: 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/geocode",
            body=await async_maybe_transform(
                {
                    "q": q,
                    "country_code": country_code,
                    "focus": focus,
                    "lang": lang,
                    "layer": layer,
                    "limit": limit,
                },
                geocode_forward_params.GeocodeForwardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"format": format}, geocode_forward_params.GeocodeForwardParams),
            ),
            cast_to=GeocodeResult,
        )

    async def reverse(
        self,
        *,
        geometry: PointGeometryParam,
        format: str | Omit = omit,
        lang: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        radius: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReverseGeocodeResult:
        """
        Reverse geocode a coordinate

        Args:
          geometry: GeoJSON Point geometry per RFC 7946. Coordinates use [longitude, latitude]
              order. Optional third element is altitude in meters.

          format: Response format: json (default), geojson, csv, ndjson

          lang: Preferred response language (ISO 639-1)

          limit: Maximum number of results (default: 1, max: 50)

          radius: Search radius in meters (default: 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/geocode/reverse",
            body=await async_maybe_transform(
                {
                    "geometry": geometry,
                    "lang": lang,
                    "limit": limit,
                    "radius": radius,
                },
                geocode_reverse_params.GeocodeReverseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"format": format}, geocode_reverse_params.GeocodeReverseParams),
            ),
            cast_to=ReverseGeocodeResult,
        )


class GeocodeResourceWithRawResponse:
    def __init__(self, geocode: GeocodeResource) -> None:
        self._geocode = geocode

        self.autocomplete = to_raw_response_wrapper(
            geocode.autocomplete,
        )
        self.batch = to_raw_response_wrapper(
            geocode.batch,
        )
        self.forward = to_raw_response_wrapper(
            geocode.forward,
        )
        self.reverse = to_raw_response_wrapper(
            geocode.reverse,
        )


class AsyncGeocodeResourceWithRawResponse:
    def __init__(self, geocode: AsyncGeocodeResource) -> None:
        self._geocode = geocode

        self.autocomplete = async_to_raw_response_wrapper(
            geocode.autocomplete,
        )
        self.batch = async_to_raw_response_wrapper(
            geocode.batch,
        )
        self.forward = async_to_raw_response_wrapper(
            geocode.forward,
        )
        self.reverse = async_to_raw_response_wrapper(
            geocode.reverse,
        )


class GeocodeResourceWithStreamingResponse:
    def __init__(self, geocode: GeocodeResource) -> None:
        self._geocode = geocode

        self.autocomplete = to_streamed_response_wrapper(
            geocode.autocomplete,
        )
        self.batch = to_streamed_response_wrapper(
            geocode.batch,
        )
        self.forward = to_streamed_response_wrapper(
            geocode.forward,
        )
        self.reverse = to_streamed_response_wrapper(
            geocode.reverse,
        )


class AsyncGeocodeResourceWithStreamingResponse:
    def __init__(self, geocode: AsyncGeocodeResource) -> None:
        self._geocode = geocode

        self.autocomplete = async_to_streamed_response_wrapper(
            geocode.autocomplete,
        )
        self.batch = async_to_streamed_response_wrapper(
            geocode.batch,
        )
        self.forward = async_to_streamed_response_wrapper(
            geocode.forward,
        )
        self.reverse = async_to_streamed_response_wrapper(
            geocode.reverse,
        )
