# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    geocode_batch_params,
    geocode_forward_params,
    geocode_reverse_params,
    geocode_autocomplete_params,
    geocode_forward_post_params,
    geocode_reverse_post_params,
    geocode_autocomplete_post_params,
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
        country_code: str | Omit = omit,
        lang: str | Omit = omit,
        lat: float | Omit = omit,
        layer: str | Omit = omit,
        limit: int | Omit = omit,
        lng: float | Omit = omit,
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
          q: Partial address query

          country_code: ISO 3166-1 alpha-2 country code filter

          lang: Language code for localized names (e.g. en, de, fr)

          lat: Focus latitude

          layer: Filter by layer: address, poi, or admin

          limit: Maximum results (default 10, max 20)

          lng: Focus longitude

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/geocode/autocomplete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "country_code": country_code,
                        "lang": lang,
                        "lat": lat,
                        "layer": layer,
                        "limit": limit,
                        "lng": lng,
                    },
                    geocode_autocomplete_params.GeocodeAutocompleteParams,
                ),
            ),
            cast_to=AutocompleteResult,
        )

    def autocomplete_post(
        self,
        *,
        q: str,
        country_code: str | Omit = omit,
        lang: str | Omit = omit,
        lat: float | Omit = omit,
        layer: str | Omit = omit,
        limit: int | Omit = omit,
        lng: float | Omit = omit,
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
          q: Partial address query

          country_code: ISO 3166-1 alpha-2 country code filter

          lang: Language code for localized names (e.g. en, de, fr)

          lat: Focus latitude

          layer: Filter by layer: address, poi, or admin

          limit: Maximum results (default 10, max 20)

          lng: Focus longitude

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/geocode/autocomplete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "country_code": country_code,
                        "lang": lang,
                        "lat": lat,
                        "layer": layer,
                        "limit": limit,
                        "lng": lng,
                    },
                    geocode_autocomplete_post_params.GeocodeAutocompletePostParams,
                ),
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
        bbox: str | Omit = omit,
        country_code: str | Omit = omit,
        lang: str | Omit = omit,
        lat: float | Omit = omit,
        layer: str | Omit = omit,
        limit: int | Omit = omit,
        lng: float | Omit = omit,
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
          q: Address or place name

          bbox: Bounding box filter: south,west,north,east

          country_code: ISO 3166-1 alpha-2 country code filter

          lang: Language code for localized names (e.g. en, de, fr)

          lat: Focus latitude

          layer: Filter by layer: address, poi, or admin

          limit: Maximum results (default 20, max 100)

          lng: Focus longitude

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/geocode",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "bbox": bbox,
                        "country_code": country_code,
                        "lang": lang,
                        "lat": lat,
                        "layer": layer,
                        "limit": limit,
                        "lng": lng,
                    },
                    geocode_forward_params.GeocodeForwardParams,
                ),
            ),
            cast_to=GeocodeResult,
        )

    def forward_post(
        self,
        *,
        q: str,
        bbox: str | Omit = omit,
        country_code: str | Omit = omit,
        lang: str | Omit = omit,
        lat: float | Omit = omit,
        layer: str | Omit = omit,
        limit: int | Omit = omit,
        lng: float | Omit = omit,
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
          q: Address or place name

          bbox: Bounding box filter: south,west,north,east

          country_code: ISO 3166-1 alpha-2 country code filter

          lang: Language code for localized names (e.g. en, de, fr)

          lat: Focus latitude

          layer: Filter by layer: address, poi, or admin

          limit: Maximum results (default 20, max 100)

          lng: Focus longitude

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/geocode",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "bbox": bbox,
                        "country_code": country_code,
                        "lang": lang,
                        "lat": lat,
                        "layer": layer,
                        "limit": limit,
                        "lng": lng,
                    },
                    geocode_forward_post_params.GeocodeForwardPostParams,
                ),
            ),
            cast_to=GeocodeResult,
        )

    def reverse(
        self,
        *,
        lang: str | Omit = omit,
        lat: float | Omit = omit,
        layer: str | Omit = omit,
        limit: int | Omit = omit,
        lng: float | Omit = omit,
        near: str | Omit = omit,
        radius: int | Omit = omit,
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
          lang: Language code for localized names (e.g. en, de, fr)

          lat: Legacy shorthand. Latitude. Use near param instead.

          layer: Filter by layer: house or poi

          limit: Maximum results (default 1, max 20)

          lng: Legacy shorthand. Longitude. Use near param instead.

          near: Point geometry for reverse geocode (lat,lng or GeoJSON). Alternative to lat/lng
              params.

          radius: Search radius in meters (default 200, max 5000)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/geocode/reverse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "lang": lang,
                        "lat": lat,
                        "layer": layer,
                        "limit": limit,
                        "lng": lng,
                        "near": near,
                        "radius": radius,
                    },
                    geocode_reverse_params.GeocodeReverseParams,
                ),
            ),
            cast_to=ReverseGeocodeResult,
        )

    def reverse_post(
        self,
        *,
        lang: str | Omit = omit,
        lat: float | Omit = omit,
        layer: str | Omit = omit,
        limit: int | Omit = omit,
        lng: float | Omit = omit,
        near: str | Omit = omit,
        radius: int | Omit = omit,
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
          lang: Language code for localized names (e.g. en, de, fr)

          lat: Legacy shorthand. Latitude. Use near param instead.

          layer: Filter by layer: house or poi

          limit: Maximum results (default 1, max 20)

          lng: Legacy shorthand. Longitude. Use near param instead.

          near: Point geometry for reverse geocode (lat,lng or GeoJSON). Alternative to lat/lng
              params.

          radius: Search radius in meters (default 200, max 5000)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/geocode/reverse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "lang": lang,
                        "lat": lat,
                        "layer": layer,
                        "limit": limit,
                        "lng": lng,
                        "near": near,
                        "radius": radius,
                    },
                    geocode_reverse_post_params.GeocodeReversePostParams,
                ),
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
        country_code: str | Omit = omit,
        lang: str | Omit = omit,
        lat: float | Omit = omit,
        layer: str | Omit = omit,
        limit: int | Omit = omit,
        lng: float | Omit = omit,
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
          q: Partial address query

          country_code: ISO 3166-1 alpha-2 country code filter

          lang: Language code for localized names (e.g. en, de, fr)

          lat: Focus latitude

          layer: Filter by layer: address, poi, or admin

          limit: Maximum results (default 10, max 20)

          lng: Focus longitude

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/geocode/autocomplete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "country_code": country_code,
                        "lang": lang,
                        "lat": lat,
                        "layer": layer,
                        "limit": limit,
                        "lng": lng,
                    },
                    geocode_autocomplete_params.GeocodeAutocompleteParams,
                ),
            ),
            cast_to=AutocompleteResult,
        )

    async def autocomplete_post(
        self,
        *,
        q: str,
        country_code: str | Omit = omit,
        lang: str | Omit = omit,
        lat: float | Omit = omit,
        layer: str | Omit = omit,
        limit: int | Omit = omit,
        lng: float | Omit = omit,
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
          q: Partial address query

          country_code: ISO 3166-1 alpha-2 country code filter

          lang: Language code for localized names (e.g. en, de, fr)

          lat: Focus latitude

          layer: Filter by layer: address, poi, or admin

          limit: Maximum results (default 10, max 20)

          lng: Focus longitude

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/geocode/autocomplete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "country_code": country_code,
                        "lang": lang,
                        "lat": lat,
                        "layer": layer,
                        "limit": limit,
                        "lng": lng,
                    },
                    geocode_autocomplete_post_params.GeocodeAutocompletePostParams,
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
        bbox: str | Omit = omit,
        country_code: str | Omit = omit,
        lang: str | Omit = omit,
        lat: float | Omit = omit,
        layer: str | Omit = omit,
        limit: int | Omit = omit,
        lng: float | Omit = omit,
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
          q: Address or place name

          bbox: Bounding box filter: south,west,north,east

          country_code: ISO 3166-1 alpha-2 country code filter

          lang: Language code for localized names (e.g. en, de, fr)

          lat: Focus latitude

          layer: Filter by layer: address, poi, or admin

          limit: Maximum results (default 20, max 100)

          lng: Focus longitude

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/geocode",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "bbox": bbox,
                        "country_code": country_code,
                        "lang": lang,
                        "lat": lat,
                        "layer": layer,
                        "limit": limit,
                        "lng": lng,
                    },
                    geocode_forward_params.GeocodeForwardParams,
                ),
            ),
            cast_to=GeocodeResult,
        )

    async def forward_post(
        self,
        *,
        q: str,
        bbox: str | Omit = omit,
        country_code: str | Omit = omit,
        lang: str | Omit = omit,
        lat: float | Omit = omit,
        layer: str | Omit = omit,
        limit: int | Omit = omit,
        lng: float | Omit = omit,
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
          q: Address or place name

          bbox: Bounding box filter: south,west,north,east

          country_code: ISO 3166-1 alpha-2 country code filter

          lang: Language code for localized names (e.g. en, de, fr)

          lat: Focus latitude

          layer: Filter by layer: address, poi, or admin

          limit: Maximum results (default 20, max 100)

          lng: Focus longitude

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/geocode",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "bbox": bbox,
                        "country_code": country_code,
                        "lang": lang,
                        "lat": lat,
                        "layer": layer,
                        "limit": limit,
                        "lng": lng,
                    },
                    geocode_forward_post_params.GeocodeForwardPostParams,
                ),
            ),
            cast_to=GeocodeResult,
        )

    async def reverse(
        self,
        *,
        lang: str | Omit = omit,
        lat: float | Omit = omit,
        layer: str | Omit = omit,
        limit: int | Omit = omit,
        lng: float | Omit = omit,
        near: str | Omit = omit,
        radius: int | Omit = omit,
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
          lang: Language code for localized names (e.g. en, de, fr)

          lat: Legacy shorthand. Latitude. Use near param instead.

          layer: Filter by layer: house or poi

          limit: Maximum results (default 1, max 20)

          lng: Legacy shorthand. Longitude. Use near param instead.

          near: Point geometry for reverse geocode (lat,lng or GeoJSON). Alternative to lat/lng
              params.

          radius: Search radius in meters (default 200, max 5000)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/geocode/reverse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "lang": lang,
                        "lat": lat,
                        "layer": layer,
                        "limit": limit,
                        "lng": lng,
                        "near": near,
                        "radius": radius,
                    },
                    geocode_reverse_params.GeocodeReverseParams,
                ),
            ),
            cast_to=ReverseGeocodeResult,
        )

    async def reverse_post(
        self,
        *,
        lang: str | Omit = omit,
        lat: float | Omit = omit,
        layer: str | Omit = omit,
        limit: int | Omit = omit,
        lng: float | Omit = omit,
        near: str | Omit = omit,
        radius: int | Omit = omit,
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
          lang: Language code for localized names (e.g. en, de, fr)

          lat: Legacy shorthand. Latitude. Use near param instead.

          layer: Filter by layer: house or poi

          limit: Maximum results (default 1, max 20)

          lng: Legacy shorthand. Longitude. Use near param instead.

          near: Point geometry for reverse geocode (lat,lng or GeoJSON). Alternative to lat/lng
              params.

          radius: Search radius in meters (default 200, max 5000)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/geocode/reverse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "lang": lang,
                        "lat": lat,
                        "layer": layer,
                        "limit": limit,
                        "lng": lng,
                        "near": near,
                        "radius": radius,
                    },
                    geocode_reverse_post_params.GeocodeReversePostParams,
                ),
            ),
            cast_to=ReverseGeocodeResult,
        )


class GeocodeResourceWithRawResponse:
    def __init__(self, geocode: GeocodeResource) -> None:
        self._geocode = geocode

        self.autocomplete = to_raw_response_wrapper(
            geocode.autocomplete,
        )
        self.autocomplete_post = to_raw_response_wrapper(
            geocode.autocomplete_post,
        )
        self.batch = to_raw_response_wrapper(
            geocode.batch,
        )
        self.forward = to_raw_response_wrapper(
            geocode.forward,
        )
        self.forward_post = to_raw_response_wrapper(
            geocode.forward_post,
        )
        self.reverse = to_raw_response_wrapper(
            geocode.reverse,
        )
        self.reverse_post = to_raw_response_wrapper(
            geocode.reverse_post,
        )


class AsyncGeocodeResourceWithRawResponse:
    def __init__(self, geocode: AsyncGeocodeResource) -> None:
        self._geocode = geocode

        self.autocomplete = async_to_raw_response_wrapper(
            geocode.autocomplete,
        )
        self.autocomplete_post = async_to_raw_response_wrapper(
            geocode.autocomplete_post,
        )
        self.batch = async_to_raw_response_wrapper(
            geocode.batch,
        )
        self.forward = async_to_raw_response_wrapper(
            geocode.forward,
        )
        self.forward_post = async_to_raw_response_wrapper(
            geocode.forward_post,
        )
        self.reverse = async_to_raw_response_wrapper(
            geocode.reverse,
        )
        self.reverse_post = async_to_raw_response_wrapper(
            geocode.reverse_post,
        )


class GeocodeResourceWithStreamingResponse:
    def __init__(self, geocode: GeocodeResource) -> None:
        self._geocode = geocode

        self.autocomplete = to_streamed_response_wrapper(
            geocode.autocomplete,
        )
        self.autocomplete_post = to_streamed_response_wrapper(
            geocode.autocomplete_post,
        )
        self.batch = to_streamed_response_wrapper(
            geocode.batch,
        )
        self.forward = to_streamed_response_wrapper(
            geocode.forward,
        )
        self.forward_post = to_streamed_response_wrapper(
            geocode.forward_post,
        )
        self.reverse = to_streamed_response_wrapper(
            geocode.reverse,
        )
        self.reverse_post = to_streamed_response_wrapper(
            geocode.reverse_post,
        )


class AsyncGeocodeResourceWithStreamingResponse:
    def __init__(self, geocode: AsyncGeocodeResource) -> None:
        self._geocode = geocode

        self.autocomplete = async_to_streamed_response_wrapper(
            geocode.autocomplete,
        )
        self.autocomplete_post = async_to_streamed_response_wrapper(
            geocode.autocomplete_post,
        )
        self.batch = async_to_streamed_response_wrapper(
            geocode.batch,
        )
        self.forward = async_to_streamed_response_wrapper(
            geocode.forward,
        )
        self.forward_post = async_to_streamed_response_wrapper(
            geocode.forward_post,
        )
        self.reverse = async_to_streamed_response_wrapper(
            geocode.reverse,
        )
        self.reverse_post = async_to_streamed_response_wrapper(
            geocode.reverse_post,
        )
