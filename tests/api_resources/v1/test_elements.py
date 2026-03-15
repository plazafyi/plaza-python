# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from plaza import Plaza, AsyncPlaza
from tests.utils import assert_matches_type
from plaza.types.v1 import GeoJsonFeature, FeatureCollection

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestElements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Plaza) -> None:
        element = client.v1.elements.retrieve(
            id=0,
            type="type",
        )
        assert_matches_type(GeoJsonFeature, element, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Plaza) -> None:
        response = client.v1.elements.with_raw_response.retrieve(
            id=0,
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        element = response.parse()
        assert_matches_type(GeoJsonFeature, element, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Plaza) -> None:
        with client.v1.elements.with_streaming_response.retrieve(
            id=0,
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            element = response.parse()
            assert_matches_type(GeoJsonFeature, element, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Plaza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            client.v1.elements.with_raw_response.retrieve(
                id=0,
                type="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_fetch_batch(self, client: Plaza) -> None:
        element = client.v1.elements.fetch_batch(
            elements=[
                {
                    "id": 0,
                    "type": "node",
                }
            ],
        )
        assert_matches_type(FeatureCollection, element, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_fetch_batch(self, client: Plaza) -> None:
        response = client.v1.elements.with_raw_response.fetch_batch(
            elements=[
                {
                    "id": 0,
                    "type": "node",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        element = response.parse()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_fetch_batch(self, client: Plaza) -> None:
        with client.v1.elements.with_streaming_response.fetch_batch(
            elements=[
                {
                    "id": 0,
                    "type": "node",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            element = response.parse()
            assert_matches_type(FeatureCollection, element, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query(self, client: Plaza) -> None:
        element = client.v1.elements.query()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_with_all_params(self, client: Plaza) -> None:
        element = client.v1.elements.query(
            bbox="bbox",
            cursor="cursor",
            h3="h3",
            limit=0,
            type="type",
        )
        assert_matches_type(FeatureCollection, element, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_query(self, client: Plaza) -> None:
        response = client.v1.elements.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        element = response.parse()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_query(self, client: Plaza) -> None:
        with client.v1.elements.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            element = response.parse()
            assert_matches_type(FeatureCollection, element, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncElements:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPlaza) -> None:
        element = await async_client.v1.elements.retrieve(
            id=0,
            type="type",
        )
        assert_matches_type(GeoJsonFeature, element, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPlaza) -> None:
        response = await async_client.v1.elements.with_raw_response.retrieve(
            id=0,
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        element = await response.parse()
        assert_matches_type(GeoJsonFeature, element, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPlaza) -> None:
        async with async_client.v1.elements.with_streaming_response.retrieve(
            id=0,
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            element = await response.parse()
            assert_matches_type(GeoJsonFeature, element, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPlaza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            await async_client.v1.elements.with_raw_response.retrieve(
                id=0,
                type="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_fetch_batch(self, async_client: AsyncPlaza) -> None:
        element = await async_client.v1.elements.fetch_batch(
            elements=[
                {
                    "id": 0,
                    "type": "node",
                }
            ],
        )
        assert_matches_type(FeatureCollection, element, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_fetch_batch(self, async_client: AsyncPlaza) -> None:
        response = await async_client.v1.elements.with_raw_response.fetch_batch(
            elements=[
                {
                    "id": 0,
                    "type": "node",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        element = await response.parse()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_fetch_batch(self, async_client: AsyncPlaza) -> None:
        async with async_client.v1.elements.with_streaming_response.fetch_batch(
            elements=[
                {
                    "id": 0,
                    "type": "node",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            element = await response.parse()
            assert_matches_type(FeatureCollection, element, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query(self, async_client: AsyncPlaza) -> None:
        element = await async_client.v1.elements.query()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncPlaza) -> None:
        element = await async_client.v1.elements.query(
            bbox="bbox",
            cursor="cursor",
            h3="h3",
            limit=0,
            type="type",
        )
        assert_matches_type(FeatureCollection, element, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncPlaza) -> None:
        response = await async_client.v1.elements.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        element = await response.parse()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncPlaza) -> None:
        async with async_client.v1.elements.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            element = await response.parse()
            assert_matches_type(FeatureCollection, element, path=["response"])

        assert cast(Any, response.is_closed) is True
