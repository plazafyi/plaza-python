# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from plaza import Plaza, AsyncPlaza
from plaza.types import (
    GeocodeResult,
    AutocompleteResult,
    GeocodeBatchResponse,
    ReverseGeocodeResult,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGeocode:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_autocomplete(self, client: Plaza) -> None:
        geocode = client.geocode.autocomplete(
            q="221B Bak",
        )
        assert_matches_type(AutocompleteResult, geocode, path=["response"])

    @parametrize
    def test_method_autocomplete_with_all_params(self, client: Plaza) -> None:
        geocode = client.geocode.autocomplete(
            q="221B Bak",
            format="format",
            country_code="xx",
            focus={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            lang="lang",
            layer="layer",
            limit=1,
        )
        assert_matches_type(AutocompleteResult, geocode, path=["response"])

    @parametrize
    def test_raw_response_autocomplete(self, client: Plaza) -> None:
        response = client.geocode.with_raw_response.autocomplete(
            q="221B Bak",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geocode = response.parse()
        assert_matches_type(AutocompleteResult, geocode, path=["response"])

    @parametrize
    def test_streaming_response_autocomplete(self, client: Plaza) -> None:
        with client.geocode.with_streaming_response.autocomplete(
            q="221B Bak",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geocode = response.parse()
            assert_matches_type(AutocompleteResult, geocode, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_batch(self, client: Plaza) -> None:
        geocode = client.geocode.batch(
            addresses=["string"],
        )
        assert_matches_type(GeocodeBatchResponse, geocode, path=["response"])

    @parametrize
    def test_raw_response_batch(self, client: Plaza) -> None:
        response = client.geocode.with_raw_response.batch(
            addresses=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geocode = response.parse()
        assert_matches_type(GeocodeBatchResponse, geocode, path=["response"])

    @parametrize
    def test_streaming_response_batch(self, client: Plaza) -> None:
        with client.geocode.with_streaming_response.batch(
            addresses=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geocode = response.parse()
            assert_matches_type(GeocodeBatchResponse, geocode, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_forward(self, client: Plaza) -> None:
        geocode = client.geocode.forward(
            q="221B Baker Street, London",
        )
        assert_matches_type(GeocodeResult, geocode, path=["response"])

    @parametrize
    def test_method_forward_with_all_params(self, client: Plaza) -> None:
        geocode = client.geocode.forward(
            q="221B Baker Street, London",
            format="format",
            country_code="xx",
            focus={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            lang="lang",
            layer="layer",
            limit=1,
        )
        assert_matches_type(GeocodeResult, geocode, path=["response"])

    @parametrize
    def test_raw_response_forward(self, client: Plaza) -> None:
        response = client.geocode.with_raw_response.forward(
            q="221B Baker Street, London",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geocode = response.parse()
        assert_matches_type(GeocodeResult, geocode, path=["response"])

    @parametrize
    def test_streaming_response_forward(self, client: Plaza) -> None:
        with client.geocode.with_streaming_response.forward(
            q="221B Baker Street, London",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geocode = response.parse()
            assert_matches_type(GeocodeResult, geocode, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_reverse(self, client: Plaza) -> None:
        geocode = client.geocode.reverse(
            geometry={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
        )
        assert_matches_type(ReverseGeocodeResult, geocode, path=["response"])

    @parametrize
    def test_method_reverse_with_all_params(self, client: Plaza) -> None:
        geocode = client.geocode.reverse(
            geometry={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            format="format",
            lang="lang",
            limit=1,
            radius=1,
        )
        assert_matches_type(ReverseGeocodeResult, geocode, path=["response"])

    @parametrize
    def test_raw_response_reverse(self, client: Plaza) -> None:
        response = client.geocode.with_raw_response.reverse(
            geometry={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geocode = response.parse()
        assert_matches_type(ReverseGeocodeResult, geocode, path=["response"])

    @parametrize
    def test_streaming_response_reverse(self, client: Plaza) -> None:
        with client.geocode.with_streaming_response.reverse(
            geometry={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geocode = response.parse()
            assert_matches_type(ReverseGeocodeResult, geocode, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGeocode:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_autocomplete(self, async_client: AsyncPlaza) -> None:
        geocode = await async_client.geocode.autocomplete(
            q="221B Bak",
        )
        assert_matches_type(AutocompleteResult, geocode, path=["response"])

    @parametrize
    async def test_method_autocomplete_with_all_params(self, async_client: AsyncPlaza) -> None:
        geocode = await async_client.geocode.autocomplete(
            q="221B Bak",
            format="format",
            country_code="xx",
            focus={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            lang="lang",
            layer="layer",
            limit=1,
        )
        assert_matches_type(AutocompleteResult, geocode, path=["response"])

    @parametrize
    async def test_raw_response_autocomplete(self, async_client: AsyncPlaza) -> None:
        response = await async_client.geocode.with_raw_response.autocomplete(
            q="221B Bak",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geocode = await response.parse()
        assert_matches_type(AutocompleteResult, geocode, path=["response"])

    @parametrize
    async def test_streaming_response_autocomplete(self, async_client: AsyncPlaza) -> None:
        async with async_client.geocode.with_streaming_response.autocomplete(
            q="221B Bak",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geocode = await response.parse()
            assert_matches_type(AutocompleteResult, geocode, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_batch(self, async_client: AsyncPlaza) -> None:
        geocode = await async_client.geocode.batch(
            addresses=["string"],
        )
        assert_matches_type(GeocodeBatchResponse, geocode, path=["response"])

    @parametrize
    async def test_raw_response_batch(self, async_client: AsyncPlaza) -> None:
        response = await async_client.geocode.with_raw_response.batch(
            addresses=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geocode = await response.parse()
        assert_matches_type(GeocodeBatchResponse, geocode, path=["response"])

    @parametrize
    async def test_streaming_response_batch(self, async_client: AsyncPlaza) -> None:
        async with async_client.geocode.with_streaming_response.batch(
            addresses=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geocode = await response.parse()
            assert_matches_type(GeocodeBatchResponse, geocode, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_forward(self, async_client: AsyncPlaza) -> None:
        geocode = await async_client.geocode.forward(
            q="221B Baker Street, London",
        )
        assert_matches_type(GeocodeResult, geocode, path=["response"])

    @parametrize
    async def test_method_forward_with_all_params(self, async_client: AsyncPlaza) -> None:
        geocode = await async_client.geocode.forward(
            q="221B Baker Street, London",
            format="format",
            country_code="xx",
            focus={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            lang="lang",
            layer="layer",
            limit=1,
        )
        assert_matches_type(GeocodeResult, geocode, path=["response"])

    @parametrize
    async def test_raw_response_forward(self, async_client: AsyncPlaza) -> None:
        response = await async_client.geocode.with_raw_response.forward(
            q="221B Baker Street, London",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geocode = await response.parse()
        assert_matches_type(GeocodeResult, geocode, path=["response"])

    @parametrize
    async def test_streaming_response_forward(self, async_client: AsyncPlaza) -> None:
        async with async_client.geocode.with_streaming_response.forward(
            q="221B Baker Street, London",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geocode = await response.parse()
            assert_matches_type(GeocodeResult, geocode, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_reverse(self, async_client: AsyncPlaza) -> None:
        geocode = await async_client.geocode.reverse(
            geometry={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
        )
        assert_matches_type(ReverseGeocodeResult, geocode, path=["response"])

    @parametrize
    async def test_method_reverse_with_all_params(self, async_client: AsyncPlaza) -> None:
        geocode = await async_client.geocode.reverse(
            geometry={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
            format="format",
            lang="lang",
            limit=1,
            radius=1,
        )
        assert_matches_type(ReverseGeocodeResult, geocode, path=["response"])

    @parametrize
    async def test_raw_response_reverse(self, async_client: AsyncPlaza) -> None:
        response = await async_client.geocode.with_raw_response.reverse(
            geometry={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geocode = await response.parse()
        assert_matches_type(ReverseGeocodeResult, geocode, path=["response"])

    @parametrize
    async def test_streaming_response_reverse(self, async_client: AsyncPlaza) -> None:
        async with async_client.geocode.with_streaming_response.reverse(
            geometry={
                "coordinates": [2.3522, 48.8566],
                "type": "Point",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geocode = await response.parse()
            assert_matches_type(ReverseGeocodeResult, geocode, path=["response"])

        assert cast(Any, response.is_closed) is True
