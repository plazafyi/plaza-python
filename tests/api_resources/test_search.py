# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from plaza import Plaza, AsyncPlaza
from plaza.types import FeatureCollection
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_query(self, client: Plaza) -> None:
        search = client.search.query(
            q="q",
        )
        assert_matches_type(FeatureCollection, search, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Plaza) -> None:
        search = client.search.query(
            q="q",
            cursor="cursor",
            format="format",
            limit=0,
            output_fields="output[fields]",
            output_include="output[include]",
            output_precision=0,
            output_sort="output[sort]",
        )
        assert_matches_type(FeatureCollection, search, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Plaza) -> None:
        response = client.search.with_raw_response.query(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(FeatureCollection, search, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Plaza) -> None:
        with client.search.with_streaming_response.query(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(FeatureCollection, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_query(self, async_client: AsyncPlaza) -> None:
        search = await async_client.search.query(
            q="q",
        )
        assert_matches_type(FeatureCollection, search, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncPlaza) -> None:
        search = await async_client.search.query(
            q="q",
            cursor="cursor",
            format="format",
            limit=0,
            output_fields="output[fields]",
            output_include="output[include]",
            output_precision=0,
            output_sort="output[sort]",
        )
        assert_matches_type(FeatureCollection, search, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncPlaza) -> None:
        response = await async_client.search.with_raw_response.query(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(FeatureCollection, search, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncPlaza) -> None:
        async with async_client.search.with_streaming_response.query(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(FeatureCollection, search, path=["response"])

        assert cast(Any, response.is_closed) is True
