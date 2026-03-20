# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from plaza import Plaza, AsyncPlaza
from plaza.types import (
    ElevationBatchResult,
    ElevationLookupResult,
    ElevationProfileResult,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestElevation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_batch(self, client: Plaza) -> None:
        elevation = client.elevation.batch(
            coordinates=[
                {
                    "lat": 48.8566,
                    "lng": 2.3522,
                },
                {
                    "lat": 45.764,
                    "lng": 4.8357,
                },
            ],
        )
        assert_matches_type(ElevationBatchResult, elevation, path=["response"])

    @parametrize
    def test_method_batch_with_all_params(self, client: Plaza) -> None:
        elevation = client.elevation.batch(
            coordinates=[
                {
                    "lat": 48.8566,
                    "lng": 2.3522,
                },
                {
                    "lat": 45.764,
                    "lng": 4.8357,
                },
            ],
            format="format",
        )
        assert_matches_type(ElevationBatchResult, elevation, path=["response"])

    @parametrize
    def test_raw_response_batch(self, client: Plaza) -> None:
        response = client.elevation.with_raw_response.batch(
            coordinates=[
                {
                    "lat": 48.8566,
                    "lng": 2.3522,
                },
                {
                    "lat": 45.764,
                    "lng": 4.8357,
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elevation = response.parse()
        assert_matches_type(ElevationBatchResult, elevation, path=["response"])

    @parametrize
    def test_streaming_response_batch(self, client: Plaza) -> None:
        with client.elevation.with_streaming_response.batch(
            coordinates=[
                {
                    "lat": 48.8566,
                    "lng": 2.3522,
                },
                {
                    "lat": 45.764,
                    "lng": 4.8357,
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elevation = response.parse()
            assert_matches_type(ElevationBatchResult, elevation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_lookup(self, client: Plaza) -> None:
        elevation = client.elevation.lookup()
        assert_matches_type(ElevationLookupResult, elevation, path=["response"])

    @parametrize
    def test_method_lookup_with_all_params(self, client: Plaza) -> None:
        elevation = client.elevation.lookup(
            format="format",
            lat=0,
            lng=0,
            locations="locations",
            output_fields="output[fields]",
            output_include="output[include]",
            output_precision=0,
        )
        assert_matches_type(ElevationLookupResult, elevation, path=["response"])

    @parametrize
    def test_raw_response_lookup(self, client: Plaza) -> None:
        response = client.elevation.with_raw_response.lookup()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elevation = response.parse()
        assert_matches_type(ElevationLookupResult, elevation, path=["response"])

    @parametrize
    def test_streaming_response_lookup(self, client: Plaza) -> None:
        with client.elevation.with_streaming_response.lookup() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elevation = response.parse()
            assert_matches_type(ElevationLookupResult, elevation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_lookup_post(self, client: Plaza) -> None:
        elevation = client.elevation.lookup_post()
        assert_matches_type(ElevationLookupResult, elevation, path=["response"])

    @parametrize
    def test_method_lookup_post_with_all_params(self, client: Plaza) -> None:
        elevation = client.elevation.lookup_post(
            format="format",
            lat=0,
            lng=0,
            locations="locations",
            output_fields="output[fields]",
            output_include="output[include]",
            output_precision=0,
        )
        assert_matches_type(ElevationLookupResult, elevation, path=["response"])

    @parametrize
    def test_raw_response_lookup_post(self, client: Plaza) -> None:
        response = client.elevation.with_raw_response.lookup_post()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elevation = response.parse()
        assert_matches_type(ElevationLookupResult, elevation, path=["response"])

    @parametrize
    def test_streaming_response_lookup_post(self, client: Plaza) -> None:
        with client.elevation.with_streaming_response.lookup_post() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elevation = response.parse()
            assert_matches_type(ElevationLookupResult, elevation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_profile(self, client: Plaza) -> None:
        elevation = client.elevation.profile(
            coordinates=[
                {
                    "lat": 48.8566,
                    "lng": 2.3522,
                },
                {
                    "lat": 48.858,
                    "lng": 2.34,
                },
                {
                    "lat": 48.8584,
                    "lng": 2.2945,
                },
            ],
        )
        assert_matches_type(ElevationProfileResult, elevation, path=["response"])

    @parametrize
    def test_raw_response_profile(self, client: Plaza) -> None:
        response = client.elevation.with_raw_response.profile(
            coordinates=[
                {
                    "lat": 48.8566,
                    "lng": 2.3522,
                },
                {
                    "lat": 48.858,
                    "lng": 2.34,
                },
                {
                    "lat": 48.8584,
                    "lng": 2.2945,
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elevation = response.parse()
        assert_matches_type(ElevationProfileResult, elevation, path=["response"])

    @parametrize
    def test_streaming_response_profile(self, client: Plaza) -> None:
        with client.elevation.with_streaming_response.profile(
            coordinates=[
                {
                    "lat": 48.8566,
                    "lng": 2.3522,
                },
                {
                    "lat": 48.858,
                    "lng": 2.34,
                },
                {
                    "lat": 48.8584,
                    "lng": 2.2945,
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elevation = response.parse()
            assert_matches_type(ElevationProfileResult, elevation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncElevation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_batch(self, async_client: AsyncPlaza) -> None:
        elevation = await async_client.elevation.batch(
            coordinates=[
                {
                    "lat": 48.8566,
                    "lng": 2.3522,
                },
                {
                    "lat": 45.764,
                    "lng": 4.8357,
                },
            ],
        )
        assert_matches_type(ElevationBatchResult, elevation, path=["response"])

    @parametrize
    async def test_method_batch_with_all_params(self, async_client: AsyncPlaza) -> None:
        elevation = await async_client.elevation.batch(
            coordinates=[
                {
                    "lat": 48.8566,
                    "lng": 2.3522,
                },
                {
                    "lat": 45.764,
                    "lng": 4.8357,
                },
            ],
            format="format",
        )
        assert_matches_type(ElevationBatchResult, elevation, path=["response"])

    @parametrize
    async def test_raw_response_batch(self, async_client: AsyncPlaza) -> None:
        response = await async_client.elevation.with_raw_response.batch(
            coordinates=[
                {
                    "lat": 48.8566,
                    "lng": 2.3522,
                },
                {
                    "lat": 45.764,
                    "lng": 4.8357,
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elevation = await response.parse()
        assert_matches_type(ElevationBatchResult, elevation, path=["response"])

    @parametrize
    async def test_streaming_response_batch(self, async_client: AsyncPlaza) -> None:
        async with async_client.elevation.with_streaming_response.batch(
            coordinates=[
                {
                    "lat": 48.8566,
                    "lng": 2.3522,
                },
                {
                    "lat": 45.764,
                    "lng": 4.8357,
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elevation = await response.parse()
            assert_matches_type(ElevationBatchResult, elevation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_lookup(self, async_client: AsyncPlaza) -> None:
        elevation = await async_client.elevation.lookup()
        assert_matches_type(ElevationLookupResult, elevation, path=["response"])

    @parametrize
    async def test_method_lookup_with_all_params(self, async_client: AsyncPlaza) -> None:
        elevation = await async_client.elevation.lookup(
            format="format",
            lat=0,
            lng=0,
            locations="locations",
            output_fields="output[fields]",
            output_include="output[include]",
            output_precision=0,
        )
        assert_matches_type(ElevationLookupResult, elevation, path=["response"])

    @parametrize
    async def test_raw_response_lookup(self, async_client: AsyncPlaza) -> None:
        response = await async_client.elevation.with_raw_response.lookup()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elevation = await response.parse()
        assert_matches_type(ElevationLookupResult, elevation, path=["response"])

    @parametrize
    async def test_streaming_response_lookup(self, async_client: AsyncPlaza) -> None:
        async with async_client.elevation.with_streaming_response.lookup() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elevation = await response.parse()
            assert_matches_type(ElevationLookupResult, elevation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_lookup_post(self, async_client: AsyncPlaza) -> None:
        elevation = await async_client.elevation.lookup_post()
        assert_matches_type(ElevationLookupResult, elevation, path=["response"])

    @parametrize
    async def test_method_lookup_post_with_all_params(self, async_client: AsyncPlaza) -> None:
        elevation = await async_client.elevation.lookup_post(
            format="format",
            lat=0,
            lng=0,
            locations="locations",
            output_fields="output[fields]",
            output_include="output[include]",
            output_precision=0,
        )
        assert_matches_type(ElevationLookupResult, elevation, path=["response"])

    @parametrize
    async def test_raw_response_lookup_post(self, async_client: AsyncPlaza) -> None:
        response = await async_client.elevation.with_raw_response.lookup_post()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elevation = await response.parse()
        assert_matches_type(ElevationLookupResult, elevation, path=["response"])

    @parametrize
    async def test_streaming_response_lookup_post(self, async_client: AsyncPlaza) -> None:
        async with async_client.elevation.with_streaming_response.lookup_post() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elevation = await response.parse()
            assert_matches_type(ElevationLookupResult, elevation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_profile(self, async_client: AsyncPlaza) -> None:
        elevation = await async_client.elevation.profile(
            coordinates=[
                {
                    "lat": 48.8566,
                    "lng": 2.3522,
                },
                {
                    "lat": 48.858,
                    "lng": 2.34,
                },
                {
                    "lat": 48.8584,
                    "lng": 2.2945,
                },
            ],
        )
        assert_matches_type(ElevationProfileResult, elevation, path=["response"])

    @parametrize
    async def test_raw_response_profile(self, async_client: AsyncPlaza) -> None:
        response = await async_client.elevation.with_raw_response.profile(
            coordinates=[
                {
                    "lat": 48.8566,
                    "lng": 2.3522,
                },
                {
                    "lat": 48.858,
                    "lng": 2.34,
                },
                {
                    "lat": 48.8584,
                    "lng": 2.2945,
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elevation = await response.parse()
        assert_matches_type(ElevationProfileResult, elevation, path=["response"])

    @parametrize
    async def test_streaming_response_profile(self, async_client: AsyncPlaza) -> None:
        async with async_client.elevation.with_streaming_response.profile(
            coordinates=[
                {
                    "lat": 48.8566,
                    "lng": 2.3522,
                },
                {
                    "lat": 48.858,
                    "lng": 2.34,
                },
                {
                    "lat": 48.8584,
                    "lng": 2.2945,
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elevation = await response.parse()
            assert_matches_type(ElevationProfileResult, elevation, path=["response"])

        assert cast(Any, response.is_closed) is True
