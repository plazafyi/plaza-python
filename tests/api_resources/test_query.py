# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from plaza import Plaza, AsyncPlaza
from plaza.types import FeatureCollection
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_execute(self, client: Plaza) -> None:
        query = client.query.execute(
            data='$$ = search(node, amenity: "cafe").around(distance: 500, geometry: point(48.8566, 2.3522));',
        )
        assert_matches_type(FeatureCollection, query, path=["response"])

    @parametrize
    def test_method_execute_with_all_params(self, client: Plaza) -> None:
        query = client.query.execute(
            data='$$ = search(node, amenity: "cafe").around(distance: 500, geometry: point(48.8566, 2.3522));',
            format="format",
        )
        assert_matches_type(FeatureCollection, query, path=["response"])

    @parametrize
    def test_raw_response_execute(self, client: Plaza) -> None:
        response = client.query.with_raw_response.execute(
            data='$$ = search(node, amenity: "cafe").around(distance: 500, geometry: point(48.8566, 2.3522));',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(FeatureCollection, query, path=["response"])

    @parametrize
    def test_streaming_response_execute(self, client: Plaza) -> None:
        with client.query.with_streaming_response.execute(
            data='$$ = search(node, amenity: "cafe").around(distance: 500, geometry: point(48.8566, 2.3522));',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(FeatureCollection, query, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQuery:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_execute(self, async_client: AsyncPlaza) -> None:
        query = await async_client.query.execute(
            data='$$ = search(node, amenity: "cafe").around(distance: 500, geometry: point(48.8566, 2.3522));',
        )
        assert_matches_type(FeatureCollection, query, path=["response"])

    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncPlaza) -> None:
        query = await async_client.query.execute(
            data='$$ = search(node, amenity: "cafe").around(distance: 500, geometry: point(48.8566, 2.3522));',
            format="format",
        )
        assert_matches_type(FeatureCollection, query, path=["response"])

    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncPlaza) -> None:
        response = await async_client.query.with_raw_response.execute(
            data='$$ = search(node, amenity: "cafe").around(distance: 500, geometry: point(48.8566, 2.3522));',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(FeatureCollection, query, path=["response"])

    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncPlaza) -> None:
        async with async_client.query.with_streaming_response.execute(
            data='$$ = search(node, amenity: "cafe").around(distance: 500, geometry: point(48.8566, 2.3522));',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(FeatureCollection, query, path=["response"])

        assert cast(Any, response.is_closed) is True
