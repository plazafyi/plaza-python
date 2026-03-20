# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from plaza import Plaza, AsyncPlaza
from plaza.types import OptimizeResult, OptimizeJobStatus
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOptimize:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Plaza) -> None:
        optimize = client.optimize.create(
            waypoints={
                "coordinates": [0],
                "type": "Point",
            },
        )
        assert_matches_type(OptimizeResult, optimize, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Plaza) -> None:
        optimize = client.optimize.create(
            waypoints={
                "coordinates": [0],
                "type": "Point",
            },
            mode="auto",
            roundtrip=True,
        )
        assert_matches_type(OptimizeResult, optimize, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Plaza) -> None:
        response = client.optimize.with_raw_response.create(
            waypoints={
                "coordinates": [0],
                "type": "Point",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimize = response.parse()
        assert_matches_type(OptimizeResult, optimize, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Plaza) -> None:
        with client.optimize.with_streaming_response.create(
            waypoints={
                "coordinates": [0],
                "type": "Point",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimize = response.parse()
            assert_matches_type(OptimizeResult, optimize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Plaza) -> None:
        optimize = client.optimize.retrieve(
            "job_id",
        )
        assert_matches_type(OptimizeJobStatus, optimize, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Plaza) -> None:
        response = client.optimize.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimize = response.parse()
        assert_matches_type(OptimizeJobStatus, optimize, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Plaza) -> None:
        with client.optimize.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimize = response.parse()
            assert_matches_type(OptimizeJobStatus, optimize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Plaza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.optimize.with_raw_response.retrieve(
                "",
            )


class TestAsyncOptimize:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncPlaza) -> None:
        optimize = await async_client.optimize.create(
            waypoints={
                "coordinates": [0],
                "type": "Point",
            },
        )
        assert_matches_type(OptimizeResult, optimize, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPlaza) -> None:
        optimize = await async_client.optimize.create(
            waypoints={
                "coordinates": [0],
                "type": "Point",
            },
            mode="auto",
            roundtrip=True,
        )
        assert_matches_type(OptimizeResult, optimize, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPlaza) -> None:
        response = await async_client.optimize.with_raw_response.create(
            waypoints={
                "coordinates": [0],
                "type": "Point",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimize = await response.parse()
        assert_matches_type(OptimizeResult, optimize, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPlaza) -> None:
        async with async_client.optimize.with_streaming_response.create(
            waypoints={
                "coordinates": [0],
                "type": "Point",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimize = await response.parse()
            assert_matches_type(OptimizeResult, optimize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPlaza) -> None:
        optimize = await async_client.optimize.retrieve(
            "job_id",
        )
        assert_matches_type(OptimizeJobStatus, optimize, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPlaza) -> None:
        response = await async_client.optimize.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimize = await response.parse()
        assert_matches_type(OptimizeJobStatus, optimize, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPlaza) -> None:
        async with async_client.optimize.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimize = await response.parse()
            assert_matches_type(OptimizeJobStatus, optimize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPlaza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.optimize.with_raw_response.retrieve(
                "",
            )
