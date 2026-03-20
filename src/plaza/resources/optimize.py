# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Iterable, cast
from typing_extensions import Literal

import httpx

from ..types import optimize_create_params
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
from ..types.optimize_result import OptimizeResult
from ..types.optimize_job_status import OptimizeJobStatus

__all__ = ["OptimizeResource", "AsyncOptimizeResource"]


class OptimizeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OptimizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plazafyi/plaza-python#accessing-raw-response-data-eg-headers
        """
        return OptimizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptimizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plazafyi/plaza-python#with_streaming_response
        """
        return OptimizeResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        waypoints: Iterable[optimize_create_params.Waypoint],
        mode: Literal["auto", "foot", "bicycle"] | Omit = omit,
        roundtrip: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptimizeResult:
        """
        Optimize route through waypoints

        Args:
          waypoints: Waypoints to visit in optimized order (2-50 points)

          mode: Travel mode (default: `auto`)

          roundtrip: Whether the route should return to the starting waypoint (default: true)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            OptimizeResult,
            self._post(
                "/api/v1/optimize",
                body=maybe_transform(
                    {
                        "waypoints": waypoints,
                        "mode": mode,
                        "roundtrip": roundtrip,
                    },
                    optimize_create_params.OptimizeCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, OptimizeResult),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptimizeJobStatus:
        """
        Get async optimization result

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            path_template("/api/v1/optimize/{job_id}", job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OptimizeJobStatus,
        )


class AsyncOptimizeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOptimizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plazafyi/plaza-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptimizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptimizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plazafyi/plaza-python#with_streaming_response
        """
        return AsyncOptimizeResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        waypoints: Iterable[optimize_create_params.Waypoint],
        mode: Literal["auto", "foot", "bicycle"] | Omit = omit,
        roundtrip: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptimizeResult:
        """
        Optimize route through waypoints

        Args:
          waypoints: Waypoints to visit in optimized order (2-50 points)

          mode: Travel mode (default: `auto`)

          roundtrip: Whether the route should return to the starting waypoint (default: true)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            OptimizeResult,
            await self._post(
                "/api/v1/optimize",
                body=await async_maybe_transform(
                    {
                        "waypoints": waypoints,
                        "mode": mode,
                        "roundtrip": roundtrip,
                    },
                    optimize_create_params.OptimizeCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, OptimizeResult),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptimizeJobStatus:
        """
        Get async optimization result

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            path_template("/api/v1/optimize/{job_id}", job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OptimizeJobStatus,
        )


class OptimizeResourceWithRawResponse:
    def __init__(self, optimize: OptimizeResource) -> None:
        self._optimize = optimize

        self.create = to_raw_response_wrapper(
            optimize.create,
        )
        self.retrieve = to_raw_response_wrapper(
            optimize.retrieve,
        )


class AsyncOptimizeResourceWithRawResponse:
    def __init__(self, optimize: AsyncOptimizeResource) -> None:
        self._optimize = optimize

        self.create = async_to_raw_response_wrapper(
            optimize.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            optimize.retrieve,
        )


class OptimizeResourceWithStreamingResponse:
    def __init__(self, optimize: OptimizeResource) -> None:
        self._optimize = optimize

        self.create = to_streamed_response_wrapper(
            optimize.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            optimize.retrieve,
        )


class AsyncOptimizeResourceWithStreamingResponse:
    def __init__(self, optimize: AsyncOptimizeResource) -> None:
        self._optimize = optimize

        self.create = async_to_streamed_response_wrapper(
            optimize.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            optimize.retrieve,
        )
