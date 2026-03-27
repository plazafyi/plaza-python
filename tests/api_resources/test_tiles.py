# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from plaza import Plaza, AsyncPlaza
from plaza._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: Plaza, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/tiles/0/0/0").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tile = client.tiles.get(
            y=0,
            z=0,
            x=0,
        )
        assert tile.is_closed
        assert tile.json() == {"foo": "bar"}
        assert cast(Any, tile.is_closed) is True
        assert isinstance(tile, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: Plaza, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/tiles/0/0/0").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        tile = client.tiles.with_raw_response.get(
            y=0,
            z=0,
            x=0,
        )

        assert tile.is_closed is True
        assert tile.http_request.headers.get("X-Stainless-Lang") == "python"
        assert tile.json() == {"foo": "bar"}
        assert isinstance(tile, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: Plaza, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/tiles/0/0/0").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.tiles.with_streaming_response.get(
            y=0,
            z=0,
            x=0,
        ) as tile:
            assert not tile.is_closed
            assert tile.http_request.headers.get("X-Stainless-Lang") == "python"

            assert tile.json() == {"foo": "bar"}
            assert cast(Any, tile.is_closed) is True
            assert isinstance(tile, StreamedBinaryAPIResponse)

        assert cast(Any, tile.is_closed) is True


class TestAsyncTiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncPlaza, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/tiles/0/0/0").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tile = await async_client.tiles.get(
            y=0,
            z=0,
            x=0,
        )
        assert tile.is_closed
        assert await tile.json() == {"foo": "bar"}
        assert cast(Any, tile.is_closed) is True
        assert isinstance(tile, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncPlaza, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/tiles/0/0/0").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        tile = await async_client.tiles.with_raw_response.get(
            y=0,
            z=0,
            x=0,
        )

        assert tile.is_closed is True
        assert tile.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await tile.json() == {"foo": "bar"}
        assert isinstance(tile, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncPlaza, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/tiles/0/0/0").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.tiles.with_streaming_response.get(
            y=0,
            z=0,
            x=0,
        ) as tile:
            assert not tile.is_closed
            assert tile.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await tile.json() == {"foo": "bar"}
            assert cast(Any, tile.is_closed) is True
            assert isinstance(tile, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, tile.is_closed) is True
