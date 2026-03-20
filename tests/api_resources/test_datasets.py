# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from plaza import Plaza, AsyncPlaza
from plaza.types import Dataset, DatasetList, FeatureCollection
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Plaza) -> None:
        dataset = client.datasets.create(
            name="NYC Bike Lanes",
            slug="nyc-bike-lanes",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Plaza) -> None:
        dataset = client.datasets.create(
            name="NYC Bike Lanes",
            slug="nyc-bike-lanes",
            attribution="attribution",
            description="description",
            license="license",
            source_url="https://example.com",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Plaza) -> None:
        response = client.datasets.with_raw_response.create(
            name="NYC Bike Lanes",
            slug="nyc-bike-lanes",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Plaza) -> None:
        with client.datasets.with_streaming_response.create(
            name="NYC Bike Lanes",
            slug="nyc-bike-lanes",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Plaza) -> None:
        dataset = client.datasets.retrieve(
            "id",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Plaza) -> None:
        response = client.datasets.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Plaza) -> None:
        with client.datasets.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Plaza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.datasets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Plaza) -> None:
        dataset = client.datasets.list()
        assert_matches_type(DatasetList, dataset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Plaza) -> None:
        response = client.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetList, dataset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Plaza) -> None:
        with client.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetList, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Plaza) -> None:
        dataset = client.datasets.delete(
            "id",
        )
        assert dataset is None

    @parametrize
    def test_raw_response_delete(self, client: Plaza) -> None:
        response = client.datasets.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert dataset is None

    @parametrize
    def test_streaming_response_delete(self, client: Plaza) -> None:
        with client.datasets.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Plaza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.datasets.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_features(self, client: Plaza) -> None:
        dataset = client.datasets.features(
            id="id",
        )
        assert_matches_type(FeatureCollection, dataset, path=["response"])

    @parametrize
    def test_method_features_with_all_params(self, client: Plaza) -> None:
        dataset = client.datasets.features(
            id="id",
            cursor="cursor",
            limit=0,
            output_buffer=0,
            output_centroid=True,
            output_fields="output[fields]",
            output_geometry=True,
            output_include="output[include]",
            output_precision=0,
            output_simplify=0,
            output_sort="output[sort]",
        )
        assert_matches_type(FeatureCollection, dataset, path=["response"])

    @parametrize
    def test_raw_response_features(self, client: Plaza) -> None:
        response = client.datasets.with_raw_response.features(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(FeatureCollection, dataset, path=["response"])

    @parametrize
    def test_streaming_response_features(self, client: Plaza) -> None:
        with client.datasets.with_streaming_response.features(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(FeatureCollection, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_features(self, client: Plaza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.datasets.with_raw_response.features(
                id="",
            )


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncPlaza) -> None:
        dataset = await async_client.datasets.create(
            name="NYC Bike Lanes",
            slug="nyc-bike-lanes",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPlaza) -> None:
        dataset = await async_client.datasets.create(
            name="NYC Bike Lanes",
            slug="nyc-bike-lanes",
            attribution="attribution",
            description="description",
            license="license",
            source_url="https://example.com",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPlaza) -> None:
        response = await async_client.datasets.with_raw_response.create(
            name="NYC Bike Lanes",
            slug="nyc-bike-lanes",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPlaza) -> None:
        async with async_client.datasets.with_streaming_response.create(
            name="NYC Bike Lanes",
            slug="nyc-bike-lanes",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPlaza) -> None:
        dataset = await async_client.datasets.retrieve(
            "id",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPlaza) -> None:
        response = await async_client.datasets.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPlaza) -> None:
        async with async_client.datasets.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPlaza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.datasets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncPlaza) -> None:
        dataset = await async_client.datasets.list()
        assert_matches_type(DatasetList, dataset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPlaza) -> None:
        response = await async_client.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetList, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPlaza) -> None:
        async with async_client.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetList, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncPlaza) -> None:
        dataset = await async_client.datasets.delete(
            "id",
        )
        assert dataset is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPlaza) -> None:
        response = await async_client.datasets.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert dataset is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPlaza) -> None:
        async with async_client.datasets.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPlaza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.datasets.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_features(self, async_client: AsyncPlaza) -> None:
        dataset = await async_client.datasets.features(
            id="id",
        )
        assert_matches_type(FeatureCollection, dataset, path=["response"])

    @parametrize
    async def test_method_features_with_all_params(self, async_client: AsyncPlaza) -> None:
        dataset = await async_client.datasets.features(
            id="id",
            cursor="cursor",
            limit=0,
            output_buffer=0,
            output_centroid=True,
            output_fields="output[fields]",
            output_geometry=True,
            output_include="output[include]",
            output_precision=0,
            output_simplify=0,
            output_sort="output[sort]",
        )
        assert_matches_type(FeatureCollection, dataset, path=["response"])

    @parametrize
    async def test_raw_response_features(self, async_client: AsyncPlaza) -> None:
        response = await async_client.datasets.with_raw_response.features(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(FeatureCollection, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_features(self, async_client: AsyncPlaza) -> None:
        async with async_client.datasets.with_streaming_response.features(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(FeatureCollection, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_features(self, async_client: AsyncPlaza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.datasets.with_raw_response.features(
                id="",
            )
