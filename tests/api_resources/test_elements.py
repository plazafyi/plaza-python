# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from plaza import Plaza, AsyncPlaza
from plaza.types import (
    GeoJsonFeature,
    FeatureCollection,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestElements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Plaza) -> None:
        element = client.elements.retrieve(
            id=0,
            type="type",
        )
        assert_matches_type(GeoJsonFeature, element, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Plaza) -> None:
        response = client.elements.with_raw_response.retrieve(
            id=0,
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        element = response.parse()
        assert_matches_type(GeoJsonFeature, element, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Plaza) -> None:
        with client.elements.with_streaming_response.retrieve(
            id=0,
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            element = response.parse()
            assert_matches_type(GeoJsonFeature, element, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Plaza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            client.elements.with_raw_response.retrieve(
                id=0,
                type="",
            )

    @parametrize
    def test_method_batch(self, client: Plaza) -> None:
        element = client.elements.batch(
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
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    def test_raw_response_batch(self, client: Plaza) -> None:
        response = client.elements.with_raw_response.batch(
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
        element = response.parse()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    def test_streaming_response_batch(self, client: Plaza) -> None:
        with client.elements.with_streaming_response.batch(
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

            element = response.parse()
            assert_matches_type(FeatureCollection, element, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_lookup(self, client: Plaza) -> None:
        element = client.elements.lookup()
        assert_matches_type(GeoJsonFeature, element, path=["response"])

    @parametrize
    def test_raw_response_lookup(self, client: Plaza) -> None:
        response = client.elements.with_raw_response.lookup()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        element = response.parse()
        assert_matches_type(GeoJsonFeature, element, path=["response"])

    @parametrize
    def test_streaming_response_lookup(self, client: Plaza) -> None:
        with client.elements.with_streaming_response.lookup() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            element = response.parse()
            assert_matches_type(GeoJsonFeature, element, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_nearby(self, client: Plaza) -> None:
        element = client.elements.nearby()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    def test_method_nearby_with_all_params(self, client: Plaza) -> None:
        element = client.elements.nearby(
            lat=0,
            limit=0,
            lng=0,
            near="near",
            output_buffer=0,
            output_centroid=True,
            output_fields="output[fields]",
            output_geometry=True,
            output_include="output[include]",
            output_precision=0,
            output_simplify=0,
            output_sort="output[sort]",
            radius=0,
        )
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    def test_raw_response_nearby(self, client: Plaza) -> None:
        response = client.elements.with_raw_response.nearby()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        element = response.parse()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    def test_streaming_response_nearby(self, client: Plaza) -> None:
        with client.elements.with_streaming_response.nearby() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            element = response.parse()
            assert_matches_type(FeatureCollection, element, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_nearby_post(self, client: Plaza) -> None:
        element = client.elements.nearby_post()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    def test_method_nearby_post_with_all_params(self, client: Plaza) -> None:
        element = client.elements.nearby_post(
            lat=0,
            limit=0,
            lng=0,
            near="near",
            output_buffer=0,
            output_centroid=True,
            output_fields="output[fields]",
            output_geometry=True,
            output_include="output[include]",
            output_precision=0,
            output_simplify=0,
            output_sort="output[sort]",
            radius=0,
        )
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    def test_raw_response_nearby_post(self, client: Plaza) -> None:
        response = client.elements.with_raw_response.nearby_post()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        element = response.parse()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    def test_streaming_response_nearby_post(self, client: Plaza) -> None:
        with client.elements.with_streaming_response.nearby_post() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            element = response.parse()
            assert_matches_type(FeatureCollection, element, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query(self, client: Plaza) -> None:
        element = client.elements.query()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Plaza) -> None:
        element = client.elements.query(
            bbox="bbox",
            contains="contains",
            crosses="crosses",
            cursor="cursor",
            format="format",
            h3="h3",
            intersects="intersects",
            limit=0,
            near="near",
            output_buffer=0,
            output_centroid=True,
            output_fields="output[fields]",
            output_geometry=True,
            output_include="output[include]",
            output_precision=0,
            output_simplify=0,
            output_sort="output[sort]",
            radius=0,
            touches="touches",
            type="type",
            within="within",
        )
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Plaza) -> None:
        response = client.elements.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        element = response.parse()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Plaza) -> None:
        with client.elements.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            element = response.parse()
            assert_matches_type(FeatureCollection, element, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_post(self, client: Plaza) -> None:
        element = client.elements.query_post()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    def test_method_query_post_with_all_params(self, client: Plaza) -> None:
        element = client.elements.query_post(
            bbox="bbox",
            contains="contains",
            crosses="crosses",
            cursor="cursor",
            format="format",
            h3="h3",
            intersects="intersects",
            limit=0,
            near="near",
            output_buffer=0,
            output_centroid=True,
            output_fields="output[fields]",
            output_geometry=True,
            output_include="output[include]",
            output_precision=0,
            output_simplify=0,
            output_sort="output[sort]",
            radius=0,
            touches="touches",
            type="type",
            within="within",
        )
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    def test_raw_response_query_post(self, client: Plaza) -> None:
        response = client.elements.with_raw_response.query_post()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        element = response.parse()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    def test_streaming_response_query_post(self, client: Plaza) -> None:
        with client.elements.with_streaming_response.query_post() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            element = response.parse()
            assert_matches_type(FeatureCollection, element, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncElements:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPlaza) -> None:
        element = await async_client.elements.retrieve(
            id=0,
            type="type",
        )
        assert_matches_type(GeoJsonFeature, element, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPlaza) -> None:
        response = await async_client.elements.with_raw_response.retrieve(
            id=0,
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        element = await response.parse()
        assert_matches_type(GeoJsonFeature, element, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPlaza) -> None:
        async with async_client.elements.with_streaming_response.retrieve(
            id=0,
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            element = await response.parse()
            assert_matches_type(GeoJsonFeature, element, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPlaza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            await async_client.elements.with_raw_response.retrieve(
                id=0,
                type="",
            )

    @parametrize
    async def test_method_batch(self, async_client: AsyncPlaza) -> None:
        element = await async_client.elements.batch(
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
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    async def test_raw_response_batch(self, async_client: AsyncPlaza) -> None:
        response = await async_client.elements.with_raw_response.batch(
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
        element = await response.parse()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    async def test_streaming_response_batch(self, async_client: AsyncPlaza) -> None:
        async with async_client.elements.with_streaming_response.batch(
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

            element = await response.parse()
            assert_matches_type(FeatureCollection, element, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_lookup(self, async_client: AsyncPlaza) -> None:
        element = await async_client.elements.lookup()
        assert_matches_type(GeoJsonFeature, element, path=["response"])

    @parametrize
    async def test_raw_response_lookup(self, async_client: AsyncPlaza) -> None:
        response = await async_client.elements.with_raw_response.lookup()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        element = await response.parse()
        assert_matches_type(GeoJsonFeature, element, path=["response"])

    @parametrize
    async def test_streaming_response_lookup(self, async_client: AsyncPlaza) -> None:
        async with async_client.elements.with_streaming_response.lookup() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            element = await response.parse()
            assert_matches_type(GeoJsonFeature, element, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_nearby(self, async_client: AsyncPlaza) -> None:
        element = await async_client.elements.nearby()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    async def test_method_nearby_with_all_params(self, async_client: AsyncPlaza) -> None:
        element = await async_client.elements.nearby(
            lat=0,
            limit=0,
            lng=0,
            near="near",
            output_buffer=0,
            output_centroid=True,
            output_fields="output[fields]",
            output_geometry=True,
            output_include="output[include]",
            output_precision=0,
            output_simplify=0,
            output_sort="output[sort]",
            radius=0,
        )
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    async def test_raw_response_nearby(self, async_client: AsyncPlaza) -> None:
        response = await async_client.elements.with_raw_response.nearby()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        element = await response.parse()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    async def test_streaming_response_nearby(self, async_client: AsyncPlaza) -> None:
        async with async_client.elements.with_streaming_response.nearby() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            element = await response.parse()
            assert_matches_type(FeatureCollection, element, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_nearby_post(self, async_client: AsyncPlaza) -> None:
        element = await async_client.elements.nearby_post()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    async def test_method_nearby_post_with_all_params(self, async_client: AsyncPlaza) -> None:
        element = await async_client.elements.nearby_post(
            lat=0,
            limit=0,
            lng=0,
            near="near",
            output_buffer=0,
            output_centroid=True,
            output_fields="output[fields]",
            output_geometry=True,
            output_include="output[include]",
            output_precision=0,
            output_simplify=0,
            output_sort="output[sort]",
            radius=0,
        )
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    async def test_raw_response_nearby_post(self, async_client: AsyncPlaza) -> None:
        response = await async_client.elements.with_raw_response.nearby_post()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        element = await response.parse()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    async def test_streaming_response_nearby_post(self, async_client: AsyncPlaza) -> None:
        async with async_client.elements.with_streaming_response.nearby_post() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            element = await response.parse()
            assert_matches_type(FeatureCollection, element, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query(self, async_client: AsyncPlaza) -> None:
        element = await async_client.elements.query()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncPlaza) -> None:
        element = await async_client.elements.query(
            bbox="bbox",
            contains="contains",
            crosses="crosses",
            cursor="cursor",
            format="format",
            h3="h3",
            intersects="intersects",
            limit=0,
            near="near",
            output_buffer=0,
            output_centroid=True,
            output_fields="output[fields]",
            output_geometry=True,
            output_include="output[include]",
            output_precision=0,
            output_simplify=0,
            output_sort="output[sort]",
            radius=0,
            touches="touches",
            type="type",
            within="within",
        )
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncPlaza) -> None:
        response = await async_client.elements.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        element = await response.parse()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncPlaza) -> None:
        async with async_client.elements.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            element = await response.parse()
            assert_matches_type(FeatureCollection, element, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_post(self, async_client: AsyncPlaza) -> None:
        element = await async_client.elements.query_post()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    async def test_method_query_post_with_all_params(self, async_client: AsyncPlaza) -> None:
        element = await async_client.elements.query_post(
            bbox="bbox",
            contains="contains",
            crosses="crosses",
            cursor="cursor",
            format="format",
            h3="h3",
            intersects="intersects",
            limit=0,
            near="near",
            output_buffer=0,
            output_centroid=True,
            output_fields="output[fields]",
            output_geometry=True,
            output_include="output[include]",
            output_precision=0,
            output_simplify=0,
            output_sort="output[sort]",
            radius=0,
            touches="touches",
            type="type",
            within="within",
        )
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    async def test_raw_response_query_post(self, async_client: AsyncPlaza) -> None:
        response = await async_client.elements.with_raw_response.query_post()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        element = await response.parse()
        assert_matches_type(FeatureCollection, element, path=["response"])

    @parametrize
    async def test_streaming_response_query_post(self, async_client: AsyncPlaza) -> None:
        async with async_client.elements.with_streaming_response.query_post() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            element = await response.parse()
            assert_matches_type(FeatureCollection, element, path=["response"])

        assert cast(Any, response.is_closed) is True
