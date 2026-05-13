# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from plaza import Plaza, AsyncPlaza
from plaza.types import MapMatchResult
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMapMatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_match(self, client: Plaza) -> None:
        map_match = client.map_match.match(
            geometry={
                "coordinates": [[2.3522, 48.8566], [2.353, 48.857], [2.354, 48.8575]],
                "type": "LineString",
            },
        )
        assert_matches_type(MapMatchResult, map_match, path=["response"])

    @parametrize
    def test_method_match_with_all_params(self, client: Plaza) -> None:
        map_match = client.map_match.match(
            geometry={
                "coordinates": [[2.3522, 48.8566], [2.353, 48.857], [2.354, 48.8575]],
                "type": "LineString",
            },
            radiuses=[0],
        )
        assert_matches_type(MapMatchResult, map_match, path=["response"])

    @parametrize
    def test_raw_response_match(self, client: Plaza) -> None:
        response = client.map_match.with_raw_response.match(
            geometry={
                "coordinates": [[2.3522, 48.8566], [2.353, 48.857], [2.354, 48.8575]],
                "type": "LineString",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        map_match = response.parse()
        assert_matches_type(MapMatchResult, map_match, path=["response"])

    @parametrize
    def test_streaming_response_match(self, client: Plaza) -> None:
        with client.map_match.with_streaming_response.match(
            geometry={
                "coordinates": [[2.3522, 48.8566], [2.353, 48.857], [2.354, 48.8575]],
                "type": "LineString",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            map_match = response.parse()
            assert_matches_type(MapMatchResult, map_match, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMapMatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_match(self, async_client: AsyncPlaza) -> None:
        map_match = await async_client.map_match.match(
            geometry={
                "coordinates": [[2.3522, 48.8566], [2.353, 48.857], [2.354, 48.8575]],
                "type": "LineString",
            },
        )
        assert_matches_type(MapMatchResult, map_match, path=["response"])

    @parametrize
    async def test_method_match_with_all_params(self, async_client: AsyncPlaza) -> None:
        map_match = await async_client.map_match.match(
            geometry={
                "coordinates": [[2.3522, 48.8566], [2.353, 48.857], [2.354, 48.8575]],
                "type": "LineString",
            },
            radiuses=[0],
        )
        assert_matches_type(MapMatchResult, map_match, path=["response"])

    @parametrize
    async def test_raw_response_match(self, async_client: AsyncPlaza) -> None:
        response = await async_client.map_match.with_raw_response.match(
            geometry={
                "coordinates": [[2.3522, 48.8566], [2.353, 48.857], [2.354, 48.8575]],
                "type": "LineString",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        map_match = await response.parse()
        assert_matches_type(MapMatchResult, map_match, path=["response"])

    @parametrize
    async def test_streaming_response_match(self, async_client: AsyncPlaza) -> None:
        async with async_client.map_match.with_streaming_response.match(
            geometry={
                "coordinates": [[2.3522, 48.8566], [2.353, 48.857], [2.354, 48.8575]],
                "type": "LineString",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            map_match = await response.parse()
            assert_matches_type(MapMatchResult, map_match, path=["response"])

        assert cast(Any, response.is_closed) is True
