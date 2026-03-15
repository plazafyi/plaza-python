# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ...types import (
    v1_find_nearby_params,
    v1_execute_query_params,
    v1_execute_sparql_params,
    v1_calculate_route_params,
    v1_reverse_geocode_params,
    v1_search_features_params,
    v1_snap_to_nearest_params,
    v1_execute_overpass_params,
    v1_calculate_isochrone_params,
    v1_calculate_distance_matrix_params,
)
from .geocode import (
    GeocodeResource,
    AsyncGeocodeResource,
    GeocodeResourceWithRawResponse,
    AsyncGeocodeResourceWithRawResponse,
    GeocodeResourceWithStreamingResponse,
    AsyncGeocodeResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .datasets import (
    DatasetsResource,
    AsyncDatasetsResource,
    DatasetsResourceWithRawResponse,
    AsyncDatasetsResourceWithRawResponse,
    DatasetsResourceWithStreamingResponse,
    AsyncDatasetsResourceWithStreamingResponse,
)
from .elements import (
    ElementsResource,
    AsyncElementsResource,
    ElementsResourceWithRawResponse,
    AsyncElementsResourceWithRawResponse,
    ElementsResourceWithStreamingResponse,
    AsyncElementsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.geo_json_feature import GeoJsonFeature
from ...types.v1.feature_collection import FeatureCollection
from ...types.v1_execute_sparql_response import V1ExecuteSparqlResponse
from ...types.v1_calculate_route_response import V1CalculateRouteResponse
from ...types.v1_snap_to_nearest_response import V1SnapToNearestResponse
from ...types.v1_calculate_distance_matrix_response import V1CalculateDistanceMatrixResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def datasets(self) -> DatasetsResource:
        return DatasetsResource(self._client)

    @cached_property
    def elements(self) -> ElementsResource:
        return ElementsResource(self._client)

    @cached_property
    def geocode(self) -> GeocodeResource:
        return GeocodeResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/plaza-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/plaza-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def calculate_distance_matrix(
        self,
        *,
        destinations: Iterable[v1_calculate_distance_matrix_params.Destination],
        origins: Iterable[v1_calculate_distance_matrix_params.Origin],
        mode: Literal["auto", "foot", "bicycle"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1CalculateDistanceMatrixResponse:
        """
        Calculate a distance matrix between points

        Args:
          destinations: List of destination coordinates

          origins: List of origin coordinates

          mode: Travel mode

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/matrix",
            body=maybe_transform(
                {
                    "destinations": destinations,
                    "origins": origins,
                    "mode": mode,
                },
                v1_calculate_distance_matrix_params.V1CalculateDistanceMatrixParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1CalculateDistanceMatrixResponse,
        )

    def calculate_isochrone(
        self,
        *,
        lat: float,
        lng: float,
        time: float,
        mode: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeoJsonFeature:
        """
        Calculate an isochrone from a point

        Args:
          lat: Latitude

          lng: Longitude

          time: Travel time in seconds (1-7200)

          mode: Travel mode (auto, foot, bicycle)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/isochrone",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "lat": lat,
                        "lng": lng,
                        "time": time,
                        "mode": mode,
                    },
                    v1_calculate_isochrone_params.V1CalculateIsochroneParams,
                ),
            ),
            cast_to=GeoJsonFeature,
        )

    def calculate_route(
        self,
        *,
        destination: v1_calculate_route_params.Destination,
        origin: v1_calculate_route_params.Origin,
        mode: Literal["auto", "foot", "bicycle"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1CalculateRouteResponse:
        """
        Calculate a route between two points

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/route",
            body=maybe_transform(
                {
                    "destination": destination,
                    "origin": origin,
                    "mode": mode,
                },
                v1_calculate_route_params.V1CalculateRouteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1CalculateRouteResponse,
        )

    def execute_overpass(
        self,
        *,
        data: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """
        Execute an Overpass QL query

        Args:
          data: Overpass QL query string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/overpass",
            body=maybe_transform({"data": data}, v1_execute_overpass_params.V1ExecuteOverpassParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeatureCollection,
        )

    def execute_query(
        self,
        *,
        bbox: str | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """
        Execute a query via REST parameters

        Args:
          bbox: Bounding box filter

          type: Element type filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/query",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bbox": bbox,
                        "type": type,
                    },
                    v1_execute_query_params.V1ExecuteQueryParams,
                ),
            ),
            cast_to=FeatureCollection,
        )

    def execute_sparql(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1ExecuteSparqlResponse:
        """
        Execute a SPARQL query

        Args:
          query: SPARQL query string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/sparql",
            body=maybe_transform({"query": query}, v1_execute_sparql_params.V1ExecuteSparqlParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ExecuteSparqlResponse,
        )

    def find_nearby(
        self,
        *,
        lat: float,
        lng: float,
        limit: int | Omit = omit,
        radius: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """
        Find elements near a point

        Args:
          lat: Latitude

          lng: Longitude

          limit: Maximum results (default 100, max 1000)

          radius: Search radius in meters (default 500)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/nearby",
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
                    v1_find_nearby_params.V1FindNearbyParams,
                ),
            ),
            cast_to=FeatureCollection,
        )

    def get_tile(
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
            f"/api/v1/tiles/{z}/{x}/{y}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def reverse_geocode(
        self,
        *,
        lat: float,
        lng: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeoJsonFeature:
        """
        Reverse geocode a coordinate to the nearest named feature

        Args:
          lat: Latitude

          lng: Longitude

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/reverse-geocode",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "lat": lat,
                        "lng": lng,
                    },
                    v1_reverse_geocode_params.V1ReverseGeocodeParams,
                ),
            ),
            cast_to=GeoJsonFeature,
        )

    def search_features(
        self,
        *,
        q: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
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
                    },
                    v1_search_features_params.V1SearchFeaturesParams,
                ),
            ),
            cast_to=FeatureCollection,
        )

    def snap_to_nearest(
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
    ) -> V1SnapToNearestResponse:
        """
        Snap a coordinate to the nearest road

        Args:
          lat: Latitude

          lng: Longitude

          radius: Search radius in meters (default 500, max 5000)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/nearest",
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
                    v1_snap_to_nearest_params.V1SnapToNearestParams,
                ),
            ),
            cast_to=V1SnapToNearestResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def datasets(self) -> AsyncDatasetsResource:
        return AsyncDatasetsResource(self._client)

    @cached_property
    def elements(self) -> AsyncElementsResource:
        return AsyncElementsResource(self._client)

    @cached_property
    def geocode(self) -> AsyncGeocodeResource:
        return AsyncGeocodeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/plaza-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/plaza-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def calculate_distance_matrix(
        self,
        *,
        destinations: Iterable[v1_calculate_distance_matrix_params.Destination],
        origins: Iterable[v1_calculate_distance_matrix_params.Origin],
        mode: Literal["auto", "foot", "bicycle"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1CalculateDistanceMatrixResponse:
        """
        Calculate a distance matrix between points

        Args:
          destinations: List of destination coordinates

          origins: List of origin coordinates

          mode: Travel mode

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/matrix",
            body=await async_maybe_transform(
                {
                    "destinations": destinations,
                    "origins": origins,
                    "mode": mode,
                },
                v1_calculate_distance_matrix_params.V1CalculateDistanceMatrixParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1CalculateDistanceMatrixResponse,
        )

    async def calculate_isochrone(
        self,
        *,
        lat: float,
        lng: float,
        time: float,
        mode: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeoJsonFeature:
        """
        Calculate an isochrone from a point

        Args:
          lat: Latitude

          lng: Longitude

          time: Travel time in seconds (1-7200)

          mode: Travel mode (auto, foot, bicycle)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/isochrone",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "lat": lat,
                        "lng": lng,
                        "time": time,
                        "mode": mode,
                    },
                    v1_calculate_isochrone_params.V1CalculateIsochroneParams,
                ),
            ),
            cast_to=GeoJsonFeature,
        )

    async def calculate_route(
        self,
        *,
        destination: v1_calculate_route_params.Destination,
        origin: v1_calculate_route_params.Origin,
        mode: Literal["auto", "foot", "bicycle"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1CalculateRouteResponse:
        """
        Calculate a route between two points

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/route",
            body=await async_maybe_transform(
                {
                    "destination": destination,
                    "origin": origin,
                    "mode": mode,
                },
                v1_calculate_route_params.V1CalculateRouteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1CalculateRouteResponse,
        )

    async def execute_overpass(
        self,
        *,
        data: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """
        Execute an Overpass QL query

        Args:
          data: Overpass QL query string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/overpass",
            body=await async_maybe_transform({"data": data}, v1_execute_overpass_params.V1ExecuteOverpassParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeatureCollection,
        )

    async def execute_query(
        self,
        *,
        bbox: str | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """
        Execute a query via REST parameters

        Args:
          bbox: Bounding box filter

          type: Element type filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/query",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "bbox": bbox,
                        "type": type,
                    },
                    v1_execute_query_params.V1ExecuteQueryParams,
                ),
            ),
            cast_to=FeatureCollection,
        )

    async def execute_sparql(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1ExecuteSparqlResponse:
        """
        Execute a SPARQL query

        Args:
          query: SPARQL query string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/sparql",
            body=await async_maybe_transform({"query": query}, v1_execute_sparql_params.V1ExecuteSparqlParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ExecuteSparqlResponse,
        )

    async def find_nearby(
        self,
        *,
        lat: float,
        lng: float,
        limit: int | Omit = omit,
        radius: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """
        Find elements near a point

        Args:
          lat: Latitude

          lng: Longitude

          limit: Maximum results (default 100, max 1000)

          radius: Search radius in meters (default 500)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/nearby",
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
                    v1_find_nearby_params.V1FindNearbyParams,
                ),
            ),
            cast_to=FeatureCollection,
        )

    async def get_tile(
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
            f"/api/v1/tiles/{z}/{x}/{y}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def reverse_geocode(
        self,
        *,
        lat: float,
        lng: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeoJsonFeature:
        """
        Reverse geocode a coordinate to the nearest named feature

        Args:
          lat: Latitude

          lng: Longitude

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/reverse-geocode",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "lat": lat,
                        "lng": lng,
                    },
                    v1_reverse_geocode_params.V1ReverseGeocodeParams,
                ),
            ),
            cast_to=GeoJsonFeature,
        )

    async def search_features(
        self,
        *,
        q: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
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
                    },
                    v1_search_features_params.V1SearchFeaturesParams,
                ),
            ),
            cast_to=FeatureCollection,
        )

    async def snap_to_nearest(
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
    ) -> V1SnapToNearestResponse:
        """
        Snap a coordinate to the nearest road

        Args:
          lat: Latitude

          lng: Longitude

          radius: Search radius in meters (default 500, max 5000)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/nearest",
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
                    v1_snap_to_nearest_params.V1SnapToNearestParams,
                ),
            ),
            cast_to=V1SnapToNearestResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.calculate_distance_matrix = to_raw_response_wrapper(
            v1.calculate_distance_matrix,
        )
        self.calculate_isochrone = to_raw_response_wrapper(
            v1.calculate_isochrone,
        )
        self.calculate_route = to_raw_response_wrapper(
            v1.calculate_route,
        )
        self.execute_overpass = to_raw_response_wrapper(
            v1.execute_overpass,
        )
        self.execute_query = to_raw_response_wrapper(
            v1.execute_query,
        )
        self.execute_sparql = to_raw_response_wrapper(
            v1.execute_sparql,
        )
        self.find_nearby = to_raw_response_wrapper(
            v1.find_nearby,
        )
        self.get_tile = to_custom_raw_response_wrapper(
            v1.get_tile,
            BinaryAPIResponse,
        )
        self.reverse_geocode = to_raw_response_wrapper(
            v1.reverse_geocode,
        )
        self.search_features = to_raw_response_wrapper(
            v1.search_features,
        )
        self.snap_to_nearest = to_raw_response_wrapper(
            v1.snap_to_nearest,
        )

    @cached_property
    def datasets(self) -> DatasetsResourceWithRawResponse:
        return DatasetsResourceWithRawResponse(self._v1.datasets)

    @cached_property
    def elements(self) -> ElementsResourceWithRawResponse:
        return ElementsResourceWithRawResponse(self._v1.elements)

    @cached_property
    def geocode(self) -> GeocodeResourceWithRawResponse:
        return GeocodeResourceWithRawResponse(self._v1.geocode)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.calculate_distance_matrix = async_to_raw_response_wrapper(
            v1.calculate_distance_matrix,
        )
        self.calculate_isochrone = async_to_raw_response_wrapper(
            v1.calculate_isochrone,
        )
        self.calculate_route = async_to_raw_response_wrapper(
            v1.calculate_route,
        )
        self.execute_overpass = async_to_raw_response_wrapper(
            v1.execute_overpass,
        )
        self.execute_query = async_to_raw_response_wrapper(
            v1.execute_query,
        )
        self.execute_sparql = async_to_raw_response_wrapper(
            v1.execute_sparql,
        )
        self.find_nearby = async_to_raw_response_wrapper(
            v1.find_nearby,
        )
        self.get_tile = async_to_custom_raw_response_wrapper(
            v1.get_tile,
            AsyncBinaryAPIResponse,
        )
        self.reverse_geocode = async_to_raw_response_wrapper(
            v1.reverse_geocode,
        )
        self.search_features = async_to_raw_response_wrapper(
            v1.search_features,
        )
        self.snap_to_nearest = async_to_raw_response_wrapper(
            v1.snap_to_nearest,
        )

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithRawResponse:
        return AsyncDatasetsResourceWithRawResponse(self._v1.datasets)

    @cached_property
    def elements(self) -> AsyncElementsResourceWithRawResponse:
        return AsyncElementsResourceWithRawResponse(self._v1.elements)

    @cached_property
    def geocode(self) -> AsyncGeocodeResourceWithRawResponse:
        return AsyncGeocodeResourceWithRawResponse(self._v1.geocode)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.calculate_distance_matrix = to_streamed_response_wrapper(
            v1.calculate_distance_matrix,
        )
        self.calculate_isochrone = to_streamed_response_wrapper(
            v1.calculate_isochrone,
        )
        self.calculate_route = to_streamed_response_wrapper(
            v1.calculate_route,
        )
        self.execute_overpass = to_streamed_response_wrapper(
            v1.execute_overpass,
        )
        self.execute_query = to_streamed_response_wrapper(
            v1.execute_query,
        )
        self.execute_sparql = to_streamed_response_wrapper(
            v1.execute_sparql,
        )
        self.find_nearby = to_streamed_response_wrapper(
            v1.find_nearby,
        )
        self.get_tile = to_custom_streamed_response_wrapper(
            v1.get_tile,
            StreamedBinaryAPIResponse,
        )
        self.reverse_geocode = to_streamed_response_wrapper(
            v1.reverse_geocode,
        )
        self.search_features = to_streamed_response_wrapper(
            v1.search_features,
        )
        self.snap_to_nearest = to_streamed_response_wrapper(
            v1.snap_to_nearest,
        )

    @cached_property
    def datasets(self) -> DatasetsResourceWithStreamingResponse:
        return DatasetsResourceWithStreamingResponse(self._v1.datasets)

    @cached_property
    def elements(self) -> ElementsResourceWithStreamingResponse:
        return ElementsResourceWithStreamingResponse(self._v1.elements)

    @cached_property
    def geocode(self) -> GeocodeResourceWithStreamingResponse:
        return GeocodeResourceWithStreamingResponse(self._v1.geocode)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.calculate_distance_matrix = async_to_streamed_response_wrapper(
            v1.calculate_distance_matrix,
        )
        self.calculate_isochrone = async_to_streamed_response_wrapper(
            v1.calculate_isochrone,
        )
        self.calculate_route = async_to_streamed_response_wrapper(
            v1.calculate_route,
        )
        self.execute_overpass = async_to_streamed_response_wrapper(
            v1.execute_overpass,
        )
        self.execute_query = async_to_streamed_response_wrapper(
            v1.execute_query,
        )
        self.execute_sparql = async_to_streamed_response_wrapper(
            v1.execute_sparql,
        )
        self.find_nearby = async_to_streamed_response_wrapper(
            v1.find_nearby,
        )
        self.get_tile = async_to_custom_streamed_response_wrapper(
            v1.get_tile,
            AsyncStreamedBinaryAPIResponse,
        )
        self.reverse_geocode = async_to_streamed_response_wrapper(
            v1.reverse_geocode,
        )
        self.search_features = async_to_streamed_response_wrapper(
            v1.search_features,
        )
        self.snap_to_nearest = async_to_streamed_response_wrapper(
            v1.snap_to_nearest,
        )

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithStreamingResponse:
        return AsyncDatasetsResourceWithStreamingResponse(self._v1.datasets)

    @cached_property
    def elements(self) -> AsyncElementsResourceWithStreamingResponse:
        return AsyncElementsResourceWithStreamingResponse(self._v1.elements)

    @cached_property
    def geocode(self) -> AsyncGeocodeResourceWithStreamingResponse:
        return AsyncGeocodeResourceWithStreamingResponse(self._v1.geocode)
