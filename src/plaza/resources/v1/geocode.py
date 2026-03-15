# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import geocode_forward_params, geocode_reverse_params, geocode_autocomplete_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.geocode_forward_response import GeocodeForwardResponse
from ...types.v1.geocode_reverse_response import GeocodeReverseResponse
from ...types.v1.geocode_autocomplete_response import GeocodeAutocompleteResponse

__all__ = ["GeocodeResource", "AsyncGeocodeResource"]


class GeocodeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GeocodeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/plaza-python#accessing-raw-response-data-eg-headers
        """
        return GeocodeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GeocodeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/plaza-python#with_streaming_response
        """
        return GeocodeResourceWithStreamingResponse(self)

    def autocomplete(
        self,
        *,
        q: str,
        lat: float | Omit = omit,
        limit: int | Omit = omit,
        lng: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeocodeAutocompleteResponse:
        """
        Autocomplete a partial address

        Args:
          q: Partial address query

          lat: Focus latitude

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
                        "lat": lat,
                        "limit": limit,
                        "lng": lng,
                    },
                    geocode_autocomplete_params.GeocodeAutocompleteParams,
                ),
            ),
            cast_to=GeocodeAutocompleteResponse,
        )

    def forward(
        self,
        *,
        q: str,
        lat: float | Omit = omit,
        limit: int | Omit = omit,
        lng: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeocodeForwardResponse:
        """
        Forward geocode an address

        Args:
          q: Address or place name

          lat: Focus latitude

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
                        "lat": lat,
                        "limit": limit,
                        "lng": lng,
                    },
                    geocode_forward_params.GeocodeForwardParams,
                ),
            ),
            cast_to=GeocodeForwardResponse,
        )

    def reverse(
        self,
        *,
        lat: float,
        lng: float,
        radius: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeocodeReverseResponse:
        """
        Reverse geocode a coordinate

        Args:
          lat: Latitude

          lng: Longitude

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
                        "lat": lat,
                        "lng": lng,
                        "radius": radius,
                    },
                    geocode_reverse_params.GeocodeReverseParams,
                ),
            ),
            cast_to=GeocodeReverseResponse,
        )


class AsyncGeocodeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGeocodeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/plaza-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGeocodeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGeocodeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/plaza-python#with_streaming_response
        """
        return AsyncGeocodeResourceWithStreamingResponse(self)

    async def autocomplete(
        self,
        *,
        q: str,
        lat: float | Omit = omit,
        limit: int | Omit = omit,
        lng: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeocodeAutocompleteResponse:
        """
        Autocomplete a partial address

        Args:
          q: Partial address query

          lat: Focus latitude

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
                        "lat": lat,
                        "limit": limit,
                        "lng": lng,
                    },
                    geocode_autocomplete_params.GeocodeAutocompleteParams,
                ),
            ),
            cast_to=GeocodeAutocompleteResponse,
        )

    async def forward(
        self,
        *,
        q: str,
        lat: float | Omit = omit,
        limit: int | Omit = omit,
        lng: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeocodeForwardResponse:
        """
        Forward geocode an address

        Args:
          q: Address or place name

          lat: Focus latitude

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
                        "lat": lat,
                        "limit": limit,
                        "lng": lng,
                    },
                    geocode_forward_params.GeocodeForwardParams,
                ),
            ),
            cast_to=GeocodeForwardResponse,
        )

    async def reverse(
        self,
        *,
        lat: float,
        lng: float,
        radius: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeocodeReverseResponse:
        """
        Reverse geocode a coordinate

        Args:
          lat: Latitude

          lng: Longitude

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
                        "lat": lat,
                        "lng": lng,
                        "radius": radius,
                    },
                    geocode_reverse_params.GeocodeReverseParams,
                ),
            ),
            cast_to=GeocodeReverseResponse,
        )


class GeocodeResourceWithRawResponse:
    def __init__(self, geocode: GeocodeResource) -> None:
        self._geocode = geocode

        self.autocomplete = to_raw_response_wrapper(
            geocode.autocomplete,
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
        self.forward = async_to_streamed_response_wrapper(
            geocode.forward,
        )
        self.reverse = async_to_streamed_response_wrapper(
            geocode.reverse,
        )
