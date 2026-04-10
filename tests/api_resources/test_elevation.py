# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from plaza import Plaza, AsyncPlaza
from plaza.types import (
    ElevationLookupResult,
    ElevationProfileResult,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestElevation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_lookup(self, client: Plaza) -> None:
        elevation = client.elevation.lookup(
            geometry={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
        )
        assert_matches_type(ElevationLookupResult, elevation, path=["response"])

    @parametrize
    def test_method_lookup_with_all_params(self, client: Plaza) -> None:
        elevation = client.elevation.lookup(
            geometry={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            format="format",
        )
        assert_matches_type(ElevationLookupResult, elevation, path=["response"])

    @parametrize
    def test_raw_response_lookup(self, client: Plaza) -> None:
        response = client.elevation.with_raw_response.lookup(
            geometry={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elevation = response.parse()
        assert_matches_type(ElevationLookupResult, elevation, path=["response"])

    @parametrize
    def test_streaming_response_lookup(self, client: Plaza) -> None:
        with client.elevation.with_streaming_response.lookup(
            geometry={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elevation = response.parse()
            assert_matches_type(ElevationLookupResult, elevation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_profile(self, client: Plaza) -> None:
        elevation = client.elevation.profile(
            geometry={
                "coordinates": [[2.3522, 48.8566], [2.34, 48.858], [2.2945, 48.8584]],
                "type": "LineString",
            },
        )
        assert_matches_type(ElevationProfileResult, elevation, path=["response"])

    @parametrize
    def test_raw_response_profile(self, client: Plaza) -> None:
        response = client.elevation.with_raw_response.profile(
            geometry={
                "coordinates": [[2.3522, 48.8566], [2.34, 48.858], [2.2945, 48.8584]],
                "type": "LineString",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elevation = response.parse()
        assert_matches_type(ElevationProfileResult, elevation, path=["response"])

    @parametrize
    def test_streaming_response_profile(self, client: Plaza) -> None:
        with client.elevation.with_streaming_response.profile(
            geometry={
                "coordinates": [[2.3522, 48.8566], [2.34, 48.858], [2.2945, 48.8584]],
                "type": "LineString",
            },
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
    async def test_method_lookup(self, async_client: AsyncPlaza) -> None:
        elevation = await async_client.elevation.lookup(
            geometry={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
        )
        assert_matches_type(ElevationLookupResult, elevation, path=["response"])

    @parametrize
    async def test_method_lookup_with_all_params(self, async_client: AsyncPlaza) -> None:
        elevation = await async_client.elevation.lookup(
            geometry={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            format="format",
        )
        assert_matches_type(ElevationLookupResult, elevation, path=["response"])

    @parametrize
    async def test_raw_response_lookup(self, async_client: AsyncPlaza) -> None:
        response = await async_client.elevation.with_raw_response.lookup(
            geometry={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elevation = await response.parse()
        assert_matches_type(ElevationLookupResult, elevation, path=["response"])

    @parametrize
    async def test_streaming_response_lookup(self, async_client: AsyncPlaza) -> None:
        async with async_client.elevation.with_streaming_response.lookup(
            geometry={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elevation = await response.parse()
            assert_matches_type(ElevationLookupResult, elevation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_profile(self, async_client: AsyncPlaza) -> None:
        elevation = await async_client.elevation.profile(
            geometry={
                "coordinates": [[2.3522, 48.8566], [2.34, 48.858], [2.2945, 48.8584]],
                "type": "LineString",
            },
        )
        assert_matches_type(ElevationProfileResult, elevation, path=["response"])

    @parametrize
    async def test_raw_response_profile(self, async_client: AsyncPlaza) -> None:
        response = await async_client.elevation.with_raw_response.profile(
            geometry={
                "coordinates": [[2.3522, 48.8566], [2.34, 48.858], [2.2945, 48.8584]],
                "type": "LineString",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        elevation = await response.parse()
        assert_matches_type(ElevationProfileResult, elevation, path=["response"])

    @parametrize
    async def test_streaming_response_profile(self, async_client: AsyncPlaza) -> None:
        async with async_client.elevation.with_streaming_response.profile(
            geometry={
                "coordinates": [[2.3522, 48.8566], [2.34, 48.858], [2.2945, 48.8584]],
                "type": "LineString",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            elevation = await response.parse()
            assert_matches_type(ElevationProfileResult, elevation, path=["response"])

        assert cast(Any, response.is_closed) is True
