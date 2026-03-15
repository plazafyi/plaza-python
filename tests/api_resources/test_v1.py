# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from plaza import Plaza, AsyncPlaza
from plaza.types import (
    V1ExecuteSparqlResponse,
    V1SnapToNearestResponse,
    V1CalculateRouteResponse,
    V1CalculateDistanceMatrixResponse,
)
from tests.utils import assert_matches_type
from plaza.types.v1 import GeoJsonFeature, FeatureCollection
from plaza._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_calculate_distance_matrix(self, client: Plaza) -> None:
        v1 = client.v1.calculate_distance_matrix(
            destinations=[
                {
                    "lat": 0,
                    "lng": 0,
                }
            ],
            origins=[
                {
                    "lat": 0,
                    "lng": 0,
                }
            ],
        )
        assert_matches_type(V1CalculateDistanceMatrixResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_calculate_distance_matrix_with_all_params(self, client: Plaza) -> None:
        v1 = client.v1.calculate_distance_matrix(
            destinations=[
                {
                    "lat": 0,
                    "lng": 0,
                }
            ],
            origins=[
                {
                    "lat": 0,
                    "lng": 0,
                }
            ],
            mode="auto",
        )
        assert_matches_type(V1CalculateDistanceMatrixResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_calculate_distance_matrix(self, client: Plaza) -> None:
        response = client.v1.with_raw_response.calculate_distance_matrix(
            destinations=[
                {
                    "lat": 0,
                    "lng": 0,
                }
            ],
            origins=[
                {
                    "lat": 0,
                    "lng": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1CalculateDistanceMatrixResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_calculate_distance_matrix(self, client: Plaza) -> None:
        with client.v1.with_streaming_response.calculate_distance_matrix(
            destinations=[
                {
                    "lat": 0,
                    "lng": 0,
                }
            ],
            origins=[
                {
                    "lat": 0,
                    "lng": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1CalculateDistanceMatrixResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_calculate_isochrone(self, client: Plaza) -> None:
        v1 = client.v1.calculate_isochrone(
            lat=0,
            lng=0,
            time=0,
        )
        assert_matches_type(GeoJsonFeature, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_calculate_isochrone_with_all_params(self, client: Plaza) -> None:
        v1 = client.v1.calculate_isochrone(
            lat=0,
            lng=0,
            time=0,
            mode="mode",
        )
        assert_matches_type(GeoJsonFeature, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_calculate_isochrone(self, client: Plaza) -> None:
        response = client.v1.with_raw_response.calculate_isochrone(
            lat=0,
            lng=0,
            time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(GeoJsonFeature, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_calculate_isochrone(self, client: Plaza) -> None:
        with client.v1.with_streaming_response.calculate_isochrone(
            lat=0,
            lng=0,
            time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(GeoJsonFeature, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_calculate_route(self, client: Plaza) -> None:
        v1 = client.v1.calculate_route(
            destination={
                "lat": 0,
                "lng": 0,
            },
            origin={
                "lat": 0,
                "lng": 0,
            },
        )
        assert_matches_type(V1CalculateRouteResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_calculate_route_with_all_params(self, client: Plaza) -> None:
        v1 = client.v1.calculate_route(
            destination={
                "lat": 0,
                "lng": 0,
            },
            origin={
                "lat": 0,
                "lng": 0,
            },
            mode="auto",
        )
        assert_matches_type(V1CalculateRouteResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_calculate_route(self, client: Plaza) -> None:
        response = client.v1.with_raw_response.calculate_route(
            destination={
                "lat": 0,
                "lng": 0,
            },
            origin={
                "lat": 0,
                "lng": 0,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1CalculateRouteResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_calculate_route(self, client: Plaza) -> None:
        with client.v1.with_streaming_response.calculate_route(
            destination={
                "lat": 0,
                "lng": 0,
            },
            origin={
                "lat": 0,
                "lng": 0,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1CalculateRouteResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_overpass(self, client: Plaza) -> None:
        v1 = client.v1.execute_overpass(
            data="data",
        )
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_execute_overpass(self, client: Plaza) -> None:
        response = client.v1.with_raw_response.execute_overpass(
            data="data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_execute_overpass(self, client: Plaza) -> None:
        with client.v1.with_streaming_response.execute_overpass(
            data="data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(FeatureCollection, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_query(self, client: Plaza) -> None:
        v1 = client.v1.execute_query()
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_query_with_all_params(self, client: Plaza) -> None:
        v1 = client.v1.execute_query(
            bbox="bbox",
            type="type",
        )
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_execute_query(self, client: Plaza) -> None:
        response = client.v1.with_raw_response.execute_query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_execute_query(self, client: Plaza) -> None:
        with client.v1.with_streaming_response.execute_query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(FeatureCollection, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_sparql(self, client: Plaza) -> None:
        v1 = client.v1.execute_sparql(
            query="query",
        )
        assert_matches_type(V1ExecuteSparqlResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_execute_sparql(self, client: Plaza) -> None:
        response = client.v1.with_raw_response.execute_sparql(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ExecuteSparqlResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_execute_sparql(self, client: Plaza) -> None:
        with client.v1.with_streaming_response.execute_sparql(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ExecuteSparqlResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_nearby(self, client: Plaza) -> None:
        v1 = client.v1.find_nearby(
            lat=0,
            lng=0,
        )
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_nearby_with_all_params(self, client: Plaza) -> None:
        v1 = client.v1.find_nearby(
            lat=0,
            lng=0,
            limit=0,
            radius=0,
        )
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_find_nearby(self, client: Plaza) -> None:
        response = client.v1.with_raw_response.find_nearby(
            lat=0,
            lng=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_find_nearby(self, client: Plaza) -> None:
        with client.v1.with_streaming_response.find_nearby(
            lat=0,
            lng=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(FeatureCollection, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_tile(self, client: Plaza, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/tiles/0/0/0").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        v1 = client.v1.get_tile(
            y=0,
            z=0,
            x=0,
        )
        assert v1.is_closed
        assert v1.json() == {"foo": "bar"}
        assert cast(Any, v1.is_closed) is True
        assert isinstance(v1, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_tile(self, client: Plaza, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/tiles/0/0/0").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        v1 = client.v1.with_raw_response.get_tile(
            y=0,
            z=0,
            x=0,
        )

        assert v1.is_closed is True
        assert v1.http_request.headers.get("X-Stainless-Lang") == "python"
        assert v1.json() == {"foo": "bar"}
        assert isinstance(v1, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_tile(self, client: Plaza, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/tiles/0/0/0").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.v1.with_streaming_response.get_tile(
            y=0,
            z=0,
            x=0,
        ) as v1:
            assert not v1.is_closed
            assert v1.http_request.headers.get("X-Stainless-Lang") == "python"

            assert v1.json() == {"foo": "bar"}
            assert cast(Any, v1.is_closed) is True
            assert isinstance(v1, StreamedBinaryAPIResponse)

        assert cast(Any, v1.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reverse_geocode(self, client: Plaza) -> None:
        v1 = client.v1.reverse_geocode(
            lat=0,
            lng=0,
        )
        assert_matches_type(GeoJsonFeature, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reverse_geocode(self, client: Plaza) -> None:
        response = client.v1.with_raw_response.reverse_geocode(
            lat=0,
            lng=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(GeoJsonFeature, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reverse_geocode(self, client: Plaza) -> None:
        with client.v1.with_streaming_response.reverse_geocode(
            lat=0,
            lng=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(GeoJsonFeature, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_features(self, client: Plaza) -> None:
        v1 = client.v1.search_features(
            q="q",
        )
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_features_with_all_params(self, client: Plaza) -> None:
        v1 = client.v1.search_features(
            q="q",
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search_features(self, client: Plaza) -> None:
        response = client.v1.with_raw_response.search_features(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search_features(self, client: Plaza) -> None:
        with client.v1.with_streaming_response.search_features(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(FeatureCollection, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_snap_to_nearest(self, client: Plaza) -> None:
        v1 = client.v1.snap_to_nearest(
            lat=0,
            lng=0,
        )
        assert_matches_type(V1SnapToNearestResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_snap_to_nearest_with_all_params(self, client: Plaza) -> None:
        v1 = client.v1.snap_to_nearest(
            lat=0,
            lng=0,
            radius=0,
        )
        assert_matches_type(V1SnapToNearestResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_snap_to_nearest(self, client: Plaza) -> None:
        response = client.v1.with_raw_response.snap_to_nearest(
            lat=0,
            lng=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1SnapToNearestResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_snap_to_nearest(self, client: Plaza) -> None:
        with client.v1.with_streaming_response.snap_to_nearest(
            lat=0,
            lng=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1SnapToNearestResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_calculate_distance_matrix(self, async_client: AsyncPlaza) -> None:
        v1 = await async_client.v1.calculate_distance_matrix(
            destinations=[
                {
                    "lat": 0,
                    "lng": 0,
                }
            ],
            origins=[
                {
                    "lat": 0,
                    "lng": 0,
                }
            ],
        )
        assert_matches_type(V1CalculateDistanceMatrixResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_calculate_distance_matrix_with_all_params(self, async_client: AsyncPlaza) -> None:
        v1 = await async_client.v1.calculate_distance_matrix(
            destinations=[
                {
                    "lat": 0,
                    "lng": 0,
                }
            ],
            origins=[
                {
                    "lat": 0,
                    "lng": 0,
                }
            ],
            mode="auto",
        )
        assert_matches_type(V1CalculateDistanceMatrixResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_calculate_distance_matrix(self, async_client: AsyncPlaza) -> None:
        response = await async_client.v1.with_raw_response.calculate_distance_matrix(
            destinations=[
                {
                    "lat": 0,
                    "lng": 0,
                }
            ],
            origins=[
                {
                    "lat": 0,
                    "lng": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1CalculateDistanceMatrixResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_calculate_distance_matrix(self, async_client: AsyncPlaza) -> None:
        async with async_client.v1.with_streaming_response.calculate_distance_matrix(
            destinations=[
                {
                    "lat": 0,
                    "lng": 0,
                }
            ],
            origins=[
                {
                    "lat": 0,
                    "lng": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1CalculateDistanceMatrixResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_calculate_isochrone(self, async_client: AsyncPlaza) -> None:
        v1 = await async_client.v1.calculate_isochrone(
            lat=0,
            lng=0,
            time=0,
        )
        assert_matches_type(GeoJsonFeature, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_calculate_isochrone_with_all_params(self, async_client: AsyncPlaza) -> None:
        v1 = await async_client.v1.calculate_isochrone(
            lat=0,
            lng=0,
            time=0,
            mode="mode",
        )
        assert_matches_type(GeoJsonFeature, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_calculate_isochrone(self, async_client: AsyncPlaza) -> None:
        response = await async_client.v1.with_raw_response.calculate_isochrone(
            lat=0,
            lng=0,
            time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(GeoJsonFeature, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_calculate_isochrone(self, async_client: AsyncPlaza) -> None:
        async with async_client.v1.with_streaming_response.calculate_isochrone(
            lat=0,
            lng=0,
            time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(GeoJsonFeature, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_calculate_route(self, async_client: AsyncPlaza) -> None:
        v1 = await async_client.v1.calculate_route(
            destination={
                "lat": 0,
                "lng": 0,
            },
            origin={
                "lat": 0,
                "lng": 0,
            },
        )
        assert_matches_type(V1CalculateRouteResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_calculate_route_with_all_params(self, async_client: AsyncPlaza) -> None:
        v1 = await async_client.v1.calculate_route(
            destination={
                "lat": 0,
                "lng": 0,
            },
            origin={
                "lat": 0,
                "lng": 0,
            },
            mode="auto",
        )
        assert_matches_type(V1CalculateRouteResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_calculate_route(self, async_client: AsyncPlaza) -> None:
        response = await async_client.v1.with_raw_response.calculate_route(
            destination={
                "lat": 0,
                "lng": 0,
            },
            origin={
                "lat": 0,
                "lng": 0,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1CalculateRouteResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_calculate_route(self, async_client: AsyncPlaza) -> None:
        async with async_client.v1.with_streaming_response.calculate_route(
            destination={
                "lat": 0,
                "lng": 0,
            },
            origin={
                "lat": 0,
                "lng": 0,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1CalculateRouteResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_overpass(self, async_client: AsyncPlaza) -> None:
        v1 = await async_client.v1.execute_overpass(
            data="data",
        )
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_execute_overpass(self, async_client: AsyncPlaza) -> None:
        response = await async_client.v1.with_raw_response.execute_overpass(
            data="data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_execute_overpass(self, async_client: AsyncPlaza) -> None:
        async with async_client.v1.with_streaming_response.execute_overpass(
            data="data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(FeatureCollection, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_query(self, async_client: AsyncPlaza) -> None:
        v1 = await async_client.v1.execute_query()
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_query_with_all_params(self, async_client: AsyncPlaza) -> None:
        v1 = await async_client.v1.execute_query(
            bbox="bbox",
            type="type",
        )
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_execute_query(self, async_client: AsyncPlaza) -> None:
        response = await async_client.v1.with_raw_response.execute_query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_execute_query(self, async_client: AsyncPlaza) -> None:
        async with async_client.v1.with_streaming_response.execute_query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(FeatureCollection, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_sparql(self, async_client: AsyncPlaza) -> None:
        v1 = await async_client.v1.execute_sparql(
            query="query",
        )
        assert_matches_type(V1ExecuteSparqlResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_execute_sparql(self, async_client: AsyncPlaza) -> None:
        response = await async_client.v1.with_raw_response.execute_sparql(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ExecuteSparqlResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_execute_sparql(self, async_client: AsyncPlaza) -> None:
        async with async_client.v1.with_streaming_response.execute_sparql(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ExecuteSparqlResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_nearby(self, async_client: AsyncPlaza) -> None:
        v1 = await async_client.v1.find_nearby(
            lat=0,
            lng=0,
        )
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_nearby_with_all_params(self, async_client: AsyncPlaza) -> None:
        v1 = await async_client.v1.find_nearby(
            lat=0,
            lng=0,
            limit=0,
            radius=0,
        )
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_find_nearby(self, async_client: AsyncPlaza) -> None:
        response = await async_client.v1.with_raw_response.find_nearby(
            lat=0,
            lng=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_find_nearby(self, async_client: AsyncPlaza) -> None:
        async with async_client.v1.with_streaming_response.find_nearby(
            lat=0,
            lng=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(FeatureCollection, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_tile(self, async_client: AsyncPlaza, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/tiles/0/0/0").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        v1 = await async_client.v1.get_tile(
            y=0,
            z=0,
            x=0,
        )
        assert v1.is_closed
        assert await v1.json() == {"foo": "bar"}
        assert cast(Any, v1.is_closed) is True
        assert isinstance(v1, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_tile(self, async_client: AsyncPlaza, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/tiles/0/0/0").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        v1 = await async_client.v1.with_raw_response.get_tile(
            y=0,
            z=0,
            x=0,
        )

        assert v1.is_closed is True
        assert v1.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await v1.json() == {"foo": "bar"}
        assert isinstance(v1, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_tile(self, async_client: AsyncPlaza, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/tiles/0/0/0").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.v1.with_streaming_response.get_tile(
            y=0,
            z=0,
            x=0,
        ) as v1:
            assert not v1.is_closed
            assert v1.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await v1.json() == {"foo": "bar"}
            assert cast(Any, v1.is_closed) is True
            assert isinstance(v1, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, v1.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reverse_geocode(self, async_client: AsyncPlaza) -> None:
        v1 = await async_client.v1.reverse_geocode(
            lat=0,
            lng=0,
        )
        assert_matches_type(GeoJsonFeature, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reverse_geocode(self, async_client: AsyncPlaza) -> None:
        response = await async_client.v1.with_raw_response.reverse_geocode(
            lat=0,
            lng=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(GeoJsonFeature, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reverse_geocode(self, async_client: AsyncPlaza) -> None:
        async with async_client.v1.with_streaming_response.reverse_geocode(
            lat=0,
            lng=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(GeoJsonFeature, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_features(self, async_client: AsyncPlaza) -> None:
        v1 = await async_client.v1.search_features(
            q="q",
        )
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_features_with_all_params(self, async_client: AsyncPlaza) -> None:
        v1 = await async_client.v1.search_features(
            q="q",
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search_features(self, async_client: AsyncPlaza) -> None:
        response = await async_client.v1.with_raw_response.search_features(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(FeatureCollection, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search_features(self, async_client: AsyncPlaza) -> None:
        async with async_client.v1.with_streaming_response.search_features(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(FeatureCollection, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_snap_to_nearest(self, async_client: AsyncPlaza) -> None:
        v1 = await async_client.v1.snap_to_nearest(
            lat=0,
            lng=0,
        )
        assert_matches_type(V1SnapToNearestResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_snap_to_nearest_with_all_params(self, async_client: AsyncPlaza) -> None:
        v1 = await async_client.v1.snap_to_nearest(
            lat=0,
            lng=0,
            radius=0,
        )
        assert_matches_type(V1SnapToNearestResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_snap_to_nearest(self, async_client: AsyncPlaza) -> None:
        response = await async_client.v1.with_raw_response.snap_to_nearest(
            lat=0,
            lng=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1SnapToNearestResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_snap_to_nearest(self, async_client: AsyncPlaza) -> None:
        async with async_client.v1.with_streaming_response.snap_to_nearest(
            lat=0,
            lng=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1SnapToNearestResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True
