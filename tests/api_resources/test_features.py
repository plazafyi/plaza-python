# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from plaza import Plaza, AsyncPlaza
from plaza.types import GeoJsonFeature, FeatureCollection
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeatures:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Plaza) -> None:
        feature = client.features.retrieve(
            id=0,
            type="type",
        )
        assert_matches_type(GeoJsonFeature, feature, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Plaza) -> None:
        response = client.features.with_raw_response.retrieve(
            id=0,
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = response.parse()
        assert_matches_type(GeoJsonFeature, feature, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Plaza) -> None:
        with client.features.with_streaming_response.retrieve(
            id=0,
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = response.parse()
            assert_matches_type(GeoJsonFeature, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Plaza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            client.features.with_raw_response.retrieve(
                id=0,
                type="",
            )

    @parametrize
    def test_method_batch(self, client: Plaza) -> None:
        feature = client.features.batch(
            elements=[
                {
                    "id": 21154906,
                    "type": "node",
                },
                {
                    "id": 4589123,
                    "type": "way",
                },
            ],
        )
        assert_matches_type(FeatureCollection, feature, path=["response"])

    @parametrize
    def test_raw_response_batch(self, client: Plaza) -> None:
        response = client.features.with_raw_response.batch(
            elements=[
                {
                    "id": 21154906,
                    "type": "node",
                },
                {
                    "id": 4589123,
                    "type": "way",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = response.parse()
        assert_matches_type(FeatureCollection, feature, path=["response"])

    @parametrize
    def test_streaming_response_batch(self, client: Plaza) -> None:
        with client.features.with_streaming_response.batch(
            elements=[
                {
                    "id": 21154906,
                    "type": "node",
                },
                {
                    "id": 4589123,
                    "type": "way",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = response.parse()
            assert_matches_type(FeatureCollection, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query(self, client: Plaza) -> None:
        feature = client.features.query()
        assert_matches_type(FeatureCollection, feature, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Plaza) -> None:
        feature = client.features.query(
            cursor="cursor",
            format="format",
            h3="h3",
            limit=0,
            type="type",
            around={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            contains={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            crosses={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            intersects={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            not_contains={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            not_intersects={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            not_within={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            radius=500,
            touches={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            within={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
        )
        assert_matches_type(FeatureCollection, feature, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Plaza) -> None:
        response = client.features.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = response.parse()
        assert_matches_type(FeatureCollection, feature, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Plaza) -> None:
        with client.features.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = response.parse()
            assert_matches_type(FeatureCollection, feature, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFeatures:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPlaza) -> None:
        feature = await async_client.features.retrieve(
            id=0,
            type="type",
        )
        assert_matches_type(GeoJsonFeature, feature, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPlaza) -> None:
        response = await async_client.features.with_raw_response.retrieve(
            id=0,
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = await response.parse()
        assert_matches_type(GeoJsonFeature, feature, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPlaza) -> None:
        async with async_client.features.with_streaming_response.retrieve(
            id=0,
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = await response.parse()
            assert_matches_type(GeoJsonFeature, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPlaza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            await async_client.features.with_raw_response.retrieve(
                id=0,
                type="",
            )

    @parametrize
    async def test_method_batch(self, async_client: AsyncPlaza) -> None:
        feature = await async_client.features.batch(
            elements=[
                {
                    "id": 21154906,
                    "type": "node",
                },
                {
                    "id": 4589123,
                    "type": "way",
                },
            ],
        )
        assert_matches_type(FeatureCollection, feature, path=["response"])

    @parametrize
    async def test_raw_response_batch(self, async_client: AsyncPlaza) -> None:
        response = await async_client.features.with_raw_response.batch(
            elements=[
                {
                    "id": 21154906,
                    "type": "node",
                },
                {
                    "id": 4589123,
                    "type": "way",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = await response.parse()
        assert_matches_type(FeatureCollection, feature, path=["response"])

    @parametrize
    async def test_streaming_response_batch(self, async_client: AsyncPlaza) -> None:
        async with async_client.features.with_streaming_response.batch(
            elements=[
                {
                    "id": 21154906,
                    "type": "node",
                },
                {
                    "id": 4589123,
                    "type": "way",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = await response.parse()
            assert_matches_type(FeatureCollection, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query(self, async_client: AsyncPlaza) -> None:
        feature = await async_client.features.query()
        assert_matches_type(FeatureCollection, feature, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncPlaza) -> None:
        feature = await async_client.features.query(
            cursor="cursor",
            format="format",
            h3="h3",
            limit=0,
            type="type",
            around={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            contains={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            crosses={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            intersects={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            not_contains={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            not_intersects={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            not_within={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            radius=500,
            touches={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            within={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
        )
        assert_matches_type(FeatureCollection, feature, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncPlaza) -> None:
        response = await async_client.features.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = await response.parse()
        assert_matches_type(FeatureCollection, feature, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncPlaza) -> None:
        async with async_client.features.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = await response.parse()
            assert_matches_type(FeatureCollection, feature, path=["response"])

        assert cast(Any, response.is_closed) is True
