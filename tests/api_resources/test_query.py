# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from plaza import Plaza, AsyncPlaza
from plaza.types import SparqlResult, FeatureCollection
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_method_overpass(self, client: Plaza) -> None:
        query = client.query.overpass(
            data="data",
        )
        assert_matches_type(FeatureCollection, query, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_raw_response_overpass(self, client: Plaza) -> None:
        response = client.query.with_raw_response.overpass(
            data="data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(FeatureCollection, query, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_overpass(self, client: Plaza) -> None:
        with client.query.with_streaming_response.overpass(
            data="data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(FeatureCollection, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_method_sparql(self, client: Plaza) -> None:
        query = client.query.sparql(
            query="query",
        )
        assert_matches_type(SparqlResult, query, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_raw_response_sparql(self, client: Plaza) -> None:
        response = client.query.with_raw_response.sparql(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(SparqlResult, query, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_sparql(self, client: Plaza) -> None:
        with client.query.with_streaming_response.sparql(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(SparqlResult, query, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQuery:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_method_overpass(self, async_client: AsyncPlaza) -> None:
        query = await async_client.query.overpass(
            data="data",
        )
        assert_matches_type(FeatureCollection, query, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_overpass(self, async_client: AsyncPlaza) -> None:
        response = await async_client.query.with_raw_response.overpass(
            data="data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(FeatureCollection, query, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_overpass(self, async_client: AsyncPlaza) -> None:
        async with async_client.query.with_streaming_response.overpass(
            data="data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(FeatureCollection, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_method_sparql(self, async_client: AsyncPlaza) -> None:
        query = await async_client.query.sparql(
            query="query",
        )
        assert_matches_type(SparqlResult, query, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_sparql(self, async_client: AsyncPlaza) -> None:
        response = await async_client.query.with_raw_response.sparql(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(SparqlResult, query, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_sparql(self, async_client: AsyncPlaza) -> None:
        async with async_client.query.with_streaming_response.sparql(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(SparqlResult, query, path=["response"])

        assert cast(Any, response.is_closed) is True
