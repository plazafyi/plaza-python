# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from plaza import Plaza, AsyncPlaza
from plaza.types import (
    RouteResult,
    MatrixResult,
    NearestResult,
    GeoJsonFeature,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRouting:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_isochrone(self, client: Plaza) -> None:
        routing = client.routing.isochrone(
            lat=0,
            lng=0,
            time=0,
        )
        assert_matches_type(GeoJsonFeature, routing, path=["response"])

    @parametrize
    def test_method_isochrone_with_all_params(self, client: Plaza) -> None:
        routing = client.routing.isochrone(
            lat=0,
            lng=0,
            time=0,
            mode="mode",
        )
        assert_matches_type(GeoJsonFeature, routing, path=["response"])

    @parametrize
    def test_raw_response_isochrone(self, client: Plaza) -> None:
        response = client.routing.with_raw_response.isochrone(
            lat=0,
            lng=0,
            time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = response.parse()
        assert_matches_type(GeoJsonFeature, routing, path=["response"])

    @parametrize
    def test_streaming_response_isochrone(self, client: Plaza) -> None:
        with client.routing.with_streaming_response.isochrone(
            lat=0,
            lng=0,
            time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = response.parse()
            assert_matches_type(GeoJsonFeature, routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_matrix(self, client: Plaza) -> None:
        routing = client.routing.matrix(
            destinations={
                "coordinates": [0],
                "type": "Point",
            },
            origins={
                "coordinates": [0],
                "type": "Point",
            },
        )
        assert_matches_type(MatrixResult, routing, path=["response"])

    @parametrize
    def test_method_matrix_with_all_params(self, client: Plaza) -> None:
        routing = client.routing.matrix(
            destinations={
                "coordinates": [0],
                "type": "Point",
            },
            origins={
                "coordinates": [0],
                "type": "Point",
            },
            mode="auto",
        )
        assert_matches_type(MatrixResult, routing, path=["response"])

    @parametrize
    def test_raw_response_matrix(self, client: Plaza) -> None:
        response = client.routing.with_raw_response.matrix(
            destinations={
                "coordinates": [0],
                "type": "Point",
            },
            origins={
                "coordinates": [0],
                "type": "Point",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = response.parse()
        assert_matches_type(MatrixResult, routing, path=["response"])

    @parametrize
    def test_streaming_response_matrix(self, client: Plaza) -> None:
        with client.routing.with_streaming_response.matrix(
            destinations={
                "coordinates": [0],
                "type": "Point",
            },
            origins={
                "coordinates": [0],
                "type": "Point",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = response.parse()
            assert_matches_type(MatrixResult, routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_nearest(self, client: Plaza) -> None:
        routing = client.routing.nearest(
            lat=0,
            lng=0,
        )
        assert_matches_type(NearestResult, routing, path=["response"])

    @parametrize
    def test_method_nearest_with_all_params(self, client: Plaza) -> None:
        routing = client.routing.nearest(
            lat=0,
            lng=0,
            radius=0,
        )
        assert_matches_type(NearestResult, routing, path=["response"])

    @parametrize
    def test_raw_response_nearest(self, client: Plaza) -> None:
        response = client.routing.with_raw_response.nearest(
            lat=0,
            lng=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = response.parse()
        assert_matches_type(NearestResult, routing, path=["response"])

    @parametrize
    def test_streaming_response_nearest(self, client: Plaza) -> None:
        with client.routing.with_streaming_response.nearest(
            lat=0,
            lng=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = response.parse()
            assert_matches_type(NearestResult, routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_route(self, client: Plaza) -> None:
        routing = client.routing.route(
            destination={
                "coordinates": [0],
                "type": "Point",
            },
            origin={
                "coordinates": [0],
                "type": "Point",
            },
        )
        assert_matches_type(RouteResult, routing, path=["response"])

    @parametrize
    def test_method_route_with_all_params(self, client: Plaza) -> None:
        routing = client.routing.route(
            destination={
                "coordinates": [0],
                "type": "Point",
            },
            origin={
                "coordinates": [0],
                "type": "Point",
            },
            mode="auto",
        )
        assert_matches_type(RouteResult, routing, path=["response"])

    @parametrize
    def test_raw_response_route(self, client: Plaza) -> None:
        response = client.routing.with_raw_response.route(
            destination={
                "coordinates": [0],
                "type": "Point",
            },
            origin={
                "coordinates": [0],
                "type": "Point",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = response.parse()
        assert_matches_type(RouteResult, routing, path=["response"])

    @parametrize
    def test_streaming_response_route(self, client: Plaza) -> None:
        with client.routing.with_streaming_response.route(
            destination={
                "coordinates": [0],
                "type": "Point",
            },
            origin={
                "coordinates": [0],
                "type": "Point",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = response.parse()
            assert_matches_type(RouteResult, routing, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRouting:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_isochrone(self, async_client: AsyncPlaza) -> None:
        routing = await async_client.routing.isochrone(
            lat=0,
            lng=0,
            time=0,
        )
        assert_matches_type(GeoJsonFeature, routing, path=["response"])

    @parametrize
    async def test_method_isochrone_with_all_params(self, async_client: AsyncPlaza) -> None:
        routing = await async_client.routing.isochrone(
            lat=0,
            lng=0,
            time=0,
            mode="mode",
        )
        assert_matches_type(GeoJsonFeature, routing, path=["response"])

    @parametrize
    async def test_raw_response_isochrone(self, async_client: AsyncPlaza) -> None:
        response = await async_client.routing.with_raw_response.isochrone(
            lat=0,
            lng=0,
            time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = await response.parse()
        assert_matches_type(GeoJsonFeature, routing, path=["response"])

    @parametrize
    async def test_streaming_response_isochrone(self, async_client: AsyncPlaza) -> None:
        async with async_client.routing.with_streaming_response.isochrone(
            lat=0,
            lng=0,
            time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = await response.parse()
            assert_matches_type(GeoJsonFeature, routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_matrix(self, async_client: AsyncPlaza) -> None:
        routing = await async_client.routing.matrix(
            destinations={
                "coordinates": [0],
                "type": "Point",
            },
            origins={
                "coordinates": [0],
                "type": "Point",
            },
        )
        assert_matches_type(MatrixResult, routing, path=["response"])

    @parametrize
    async def test_method_matrix_with_all_params(self, async_client: AsyncPlaza) -> None:
        routing = await async_client.routing.matrix(
            destinations={
                "coordinates": [0],
                "type": "Point",
            },
            origins={
                "coordinates": [0],
                "type": "Point",
            },
            mode="auto",
        )
        assert_matches_type(MatrixResult, routing, path=["response"])

    @parametrize
    async def test_raw_response_matrix(self, async_client: AsyncPlaza) -> None:
        response = await async_client.routing.with_raw_response.matrix(
            destinations={
                "coordinates": [0],
                "type": "Point",
            },
            origins={
                "coordinates": [0],
                "type": "Point",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = await response.parse()
        assert_matches_type(MatrixResult, routing, path=["response"])

    @parametrize
    async def test_streaming_response_matrix(self, async_client: AsyncPlaza) -> None:
        async with async_client.routing.with_streaming_response.matrix(
            destinations={
                "coordinates": [0],
                "type": "Point",
            },
            origins={
                "coordinates": [0],
                "type": "Point",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = await response.parse()
            assert_matches_type(MatrixResult, routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_nearest(self, async_client: AsyncPlaza) -> None:
        routing = await async_client.routing.nearest(
            lat=0,
            lng=0,
        )
        assert_matches_type(NearestResult, routing, path=["response"])

    @parametrize
    async def test_method_nearest_with_all_params(self, async_client: AsyncPlaza) -> None:
        routing = await async_client.routing.nearest(
            lat=0,
            lng=0,
            radius=0,
        )
        assert_matches_type(NearestResult, routing, path=["response"])

    @parametrize
    async def test_raw_response_nearest(self, async_client: AsyncPlaza) -> None:
        response = await async_client.routing.with_raw_response.nearest(
            lat=0,
            lng=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = await response.parse()
        assert_matches_type(NearestResult, routing, path=["response"])

    @parametrize
    async def test_streaming_response_nearest(self, async_client: AsyncPlaza) -> None:
        async with async_client.routing.with_streaming_response.nearest(
            lat=0,
            lng=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = await response.parse()
            assert_matches_type(NearestResult, routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_route(self, async_client: AsyncPlaza) -> None:
        routing = await async_client.routing.route(
            destination={
                "coordinates": [0],
                "type": "Point",
            },
            origin={
                "coordinates": [0],
                "type": "Point",
            },
        )
        assert_matches_type(RouteResult, routing, path=["response"])

    @parametrize
    async def test_method_route_with_all_params(self, async_client: AsyncPlaza) -> None:
        routing = await async_client.routing.route(
            destination={
                "coordinates": [0],
                "type": "Point",
            },
            origin={
                "coordinates": [0],
                "type": "Point",
            },
            mode="auto",
        )
        assert_matches_type(RouteResult, routing, path=["response"])

    @parametrize
    async def test_raw_response_route(self, async_client: AsyncPlaza) -> None:
        response = await async_client.routing.with_raw_response.route(
            destination={
                "coordinates": [0],
                "type": "Point",
            },
            origin={
                "coordinates": [0],
                "type": "Point",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = await response.parse()
        assert_matches_type(RouteResult, routing, path=["response"])

    @parametrize
    async def test_streaming_response_route(self, async_client: AsyncPlaza) -> None:
        async with async_client.routing.with_streaming_response.route(
            destination={
                "coordinates": [0],
                "type": "Point",
            },
            origin={
                "coordinates": [0],
                "type": "Point",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = await response.parse()
            assert_matches_type(RouteResult, routing, path=["response"])

        assert cast(Any, response.is_closed) is True
