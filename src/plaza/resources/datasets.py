# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import dataset_create_params, dataset_features_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.dataset import Dataset
from ..types.dataset_list import DatasetList
from ..types.feature_collection import FeatureCollection

__all__ = ["DatasetsResource", "AsyncDatasetsResource"]


class DatasetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plazafyi/plaza-python#accessing-raw-response-data-eg-headers
        """
        return DatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plazafyi/plaza-python#with_streaming_response
        """
        return DatasetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        slug: str,
        attribution: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        license: Optional[str] | Omit = omit,
        source_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dataset:
        """
        Create a new dataset (admin only)

        Args:
          name: Human-readable dataset name

          slug: URL-friendly identifier (lowercase, hyphens, no spaces)

          attribution: Required attribution text

          description: Dataset description

          license: License identifier (e.g. CC-BY-4.0)

          source_url: Source data URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/datasets",
            body=maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "attribution": attribution,
                    "description": description,
                    "license": license,
                    "source_url": source_url,
                },
                dataset_create_params.DatasetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dataset,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dataset:
        """
        Get dataset by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/v1/datasets/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dataset,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetList:
        """List all datasets"""
        return self._get(
            "/api/v1/datasets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetList,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a dataset

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/v1/datasets/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def features(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        output_buffer: float | Omit = omit,
        output_centroid: bool | Omit = omit,
        output_fields: str | Omit = omit,
        output_geometry: bool | Omit = omit,
        output_include: str | Omit = omit,
        output_precision: int | Omit = omit,
        output_simplify: float | Omit = omit,
        output_sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """
        Query features in a dataset

        Args:
          cursor: Cursor for pagination

          limit: Maximum results

          output_buffer: Buffer geometry by meters

          output_centroid: Replace geometry with centroid

          output_fields: Comma-separated property fields to include

          output_geometry: Include geometry (default true)

          output_include: Extra computed fields: bbox, distance, center

          output_precision: Coordinate decimal precision (1-15, default 7)

          output_simplify: Simplify geometry tolerance in meters

          output_sort: Sort by: distance, name, osm_id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/v1/datasets/{id}/features", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "output_buffer": output_buffer,
                        "output_centroid": output_centroid,
                        "output_fields": output_fields,
                        "output_geometry": output_geometry,
                        "output_include": output_include,
                        "output_precision": output_precision,
                        "output_simplify": output_simplify,
                        "output_sort": output_sort,
                    },
                    dataset_features_params.DatasetFeaturesParams,
                ),
            ),
            cast_to=FeatureCollection,
        )


class AsyncDatasetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plazafyi/plaza-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plazafyi/plaza-python#with_streaming_response
        """
        return AsyncDatasetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        slug: str,
        attribution: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        license: Optional[str] | Omit = omit,
        source_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dataset:
        """
        Create a new dataset (admin only)

        Args:
          name: Human-readable dataset name

          slug: URL-friendly identifier (lowercase, hyphens, no spaces)

          attribution: Required attribution text

          description: Dataset description

          license: License identifier (e.g. CC-BY-4.0)

          source_url: Source data URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/datasets",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "attribution": attribution,
                    "description": description,
                    "license": license,
                    "source_url": source_url,
                },
                dataset_create_params.DatasetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dataset,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dataset:
        """
        Get dataset by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/v1/datasets/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dataset,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetList:
        """List all datasets"""
        return await self._get(
            "/api/v1/datasets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetList,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a dataset

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/v1/datasets/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def features(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        output_buffer: float | Omit = omit,
        output_centroid: bool | Omit = omit,
        output_fields: str | Omit = omit,
        output_geometry: bool | Omit = omit,
        output_include: str | Omit = omit,
        output_precision: int | Omit = omit,
        output_simplify: float | Omit = omit,
        output_sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeatureCollection:
        """
        Query features in a dataset

        Args:
          cursor: Cursor for pagination

          limit: Maximum results

          output_buffer: Buffer geometry by meters

          output_centroid: Replace geometry with centroid

          output_fields: Comma-separated property fields to include

          output_geometry: Include geometry (default true)

          output_include: Extra computed fields: bbox, distance, center

          output_precision: Coordinate decimal precision (1-15, default 7)

          output_simplify: Simplify geometry tolerance in meters

          output_sort: Sort by: distance, name, osm_id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/v1/datasets/{id}/features", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "output_buffer": output_buffer,
                        "output_centroid": output_centroid,
                        "output_fields": output_fields,
                        "output_geometry": output_geometry,
                        "output_include": output_include,
                        "output_precision": output_precision,
                        "output_simplify": output_simplify,
                        "output_sort": output_sort,
                    },
                    dataset_features_params.DatasetFeaturesParams,
                ),
            ),
            cast_to=FeatureCollection,
        )


class DatasetsResourceWithRawResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.create = to_raw_response_wrapper(
            datasets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            datasets.retrieve,
        )
        self.list = to_raw_response_wrapper(
            datasets.list,
        )
        self.delete = to_raw_response_wrapper(
            datasets.delete,
        )
        self.features = to_raw_response_wrapper(
            datasets.features,
        )


class AsyncDatasetsResourceWithRawResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.create = async_to_raw_response_wrapper(
            datasets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            datasets.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            datasets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            datasets.delete,
        )
        self.features = async_to_raw_response_wrapper(
            datasets.features,
        )


class DatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.create = to_streamed_response_wrapper(
            datasets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            datasets.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            datasets.list,
        )
        self.delete = to_streamed_response_wrapper(
            datasets.delete,
        )
        self.features = to_streamed_response_wrapper(
            datasets.features,
        )


class AsyncDatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.create = async_to_streamed_response_wrapper(
            datasets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            datasets.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            datasets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            datasets.delete,
        )
        self.features = async_to_streamed_response_wrapper(
            datasets.features,
        )
