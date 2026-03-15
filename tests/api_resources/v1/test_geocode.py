# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from plaza import Plaza, AsyncPlaza
from tests.utils import assert_matches_type
from plaza.types.v1 import (
    GeocodeForwardResponse,
    GeocodeReverseResponse,
    GeocodeAutocompleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGeocode:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_autocomplete(self, client: Plaza) -> None:
        geocode = client.v1.geocode.autocomplete(
            q="q",
        )
        assert_matches_type(GeocodeAutocompleteResponse, geocode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_autocomplete_with_all_params(self, client: Plaza) -> None:
        geocode = client.v1.geocode.autocomplete(
            q="q",
            lat=0,
            limit=0,
            lng=0,
        )
        assert_matches_type(GeocodeAutocompleteResponse, geocode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_autocomplete(self, client: Plaza) -> None:
        response = client.v1.geocode.with_raw_response.autocomplete(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geocode = response.parse()
        assert_matches_type(GeocodeAutocompleteResponse, geocode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_autocomplete(self, client: Plaza) -> None:
        with client.v1.geocode.with_streaming_response.autocomplete(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geocode = response.parse()
            assert_matches_type(GeocodeAutocompleteResponse, geocode, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_forward(self, client: Plaza) -> None:
        geocode = client.v1.geocode.forward(
            q="q",
        )
        assert_matches_type(GeocodeForwardResponse, geocode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_forward_with_all_params(self, client: Plaza) -> None:
        geocode = client.v1.geocode.forward(
            q="q",
            lat=0,
            limit=0,
            lng=0,
        )
        assert_matches_type(GeocodeForwardResponse, geocode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_forward(self, client: Plaza) -> None:
        response = client.v1.geocode.with_raw_response.forward(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geocode = response.parse()
        assert_matches_type(GeocodeForwardResponse, geocode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_forward(self, client: Plaza) -> None:
        with client.v1.geocode.with_streaming_response.forward(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geocode = response.parse()
            assert_matches_type(GeocodeForwardResponse, geocode, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reverse(self, client: Plaza) -> None:
        geocode = client.v1.geocode.reverse(
            lat=0,
            lng=0,
        )
        assert_matches_type(GeocodeReverseResponse, geocode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reverse_with_all_params(self, client: Plaza) -> None:
        geocode = client.v1.geocode.reverse(
            lat=0,
            lng=0,
            radius=0,
        )
        assert_matches_type(GeocodeReverseResponse, geocode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reverse(self, client: Plaza) -> None:
        response = client.v1.geocode.with_raw_response.reverse(
            lat=0,
            lng=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geocode = response.parse()
        assert_matches_type(GeocodeReverseResponse, geocode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reverse(self, client: Plaza) -> None:
        with client.v1.geocode.with_streaming_response.reverse(
            lat=0,
            lng=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geocode = response.parse()
            assert_matches_type(GeocodeReverseResponse, geocode, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGeocode:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_autocomplete(self, async_client: AsyncPlaza) -> None:
        geocode = await async_client.v1.geocode.autocomplete(
            q="q",
        )
        assert_matches_type(GeocodeAutocompleteResponse, geocode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_autocomplete_with_all_params(self, async_client: AsyncPlaza) -> None:
        geocode = await async_client.v1.geocode.autocomplete(
            q="q",
            lat=0,
            limit=0,
            lng=0,
        )
        assert_matches_type(GeocodeAutocompleteResponse, geocode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_autocomplete(self, async_client: AsyncPlaza) -> None:
        response = await async_client.v1.geocode.with_raw_response.autocomplete(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geocode = await response.parse()
        assert_matches_type(GeocodeAutocompleteResponse, geocode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_autocomplete(self, async_client: AsyncPlaza) -> None:
        async with async_client.v1.geocode.with_streaming_response.autocomplete(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geocode = await response.parse()
            assert_matches_type(GeocodeAutocompleteResponse, geocode, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_forward(self, async_client: AsyncPlaza) -> None:
        geocode = await async_client.v1.geocode.forward(
            q="q",
        )
        assert_matches_type(GeocodeForwardResponse, geocode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_forward_with_all_params(self, async_client: AsyncPlaza) -> None:
        geocode = await async_client.v1.geocode.forward(
            q="q",
            lat=0,
            limit=0,
            lng=0,
        )
        assert_matches_type(GeocodeForwardResponse, geocode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_forward(self, async_client: AsyncPlaza) -> None:
        response = await async_client.v1.geocode.with_raw_response.forward(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geocode = await response.parse()
        assert_matches_type(GeocodeForwardResponse, geocode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_forward(self, async_client: AsyncPlaza) -> None:
        async with async_client.v1.geocode.with_streaming_response.forward(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geocode = await response.parse()
            assert_matches_type(GeocodeForwardResponse, geocode, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reverse(self, async_client: AsyncPlaza) -> None:
        geocode = await async_client.v1.geocode.reverse(
            lat=0,
            lng=0,
        )
        assert_matches_type(GeocodeReverseResponse, geocode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reverse_with_all_params(self, async_client: AsyncPlaza) -> None:
        geocode = await async_client.v1.geocode.reverse(
            lat=0,
            lng=0,
            radius=0,
        )
        assert_matches_type(GeocodeReverseResponse, geocode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reverse(self, async_client: AsyncPlaza) -> None:
        response = await async_client.v1.geocode.with_raw_response.reverse(
            lat=0,
            lng=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geocode = await response.parse()
        assert_matches_type(GeocodeReverseResponse, geocode, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reverse(self, async_client: AsyncPlaza) -> None:
        async with async_client.v1.geocode.with_streaming_response.reverse(
            lat=0,
            lng=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geocode = await response.parse()
            assert_matches_type(GeocodeReverseResponse, geocode, path=["response"])

        assert cast(Any, response.is_closed) is True
