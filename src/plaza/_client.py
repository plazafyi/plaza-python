# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import PlazaError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import query, tiles, search, geocode, routing, datasets, features, optimize, elevation, map_match
    from .resources.query import QueryResource, AsyncQueryResource
    from .resources.tiles import TilesResource, AsyncTilesResource
    from .resources.search import SearchResource, AsyncSearchResource
    from .resources.geocode import GeocodeResource, AsyncGeocodeResource
    from .resources.routing import RoutingResource, AsyncRoutingResource
    from .resources.datasets import DatasetsResource, AsyncDatasetsResource
    from .resources.features import FeaturesResource, AsyncFeaturesResource
    from .resources.optimize import OptimizeResource, AsyncOptimizeResource
    from .resources.elevation import ElevationResource, AsyncElevationResource
    from .resources.map_match import MapMatchResource, AsyncMapMatchResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Plaza",
    "AsyncPlaza",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://plaza.fyi",
    "local": "http://localhost:4000",
}


class Plaza(SyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["production", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "local"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Plaza client instance.

        This automatically infers the `api_key` argument from the `PLAZA_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("PLAZA_API_KEY")
        if api_key is None:
            raise PlazaError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PLAZA_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("PLAZA_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `PLAZA_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def features(self) -> FeaturesResource:
        from .resources.features import FeaturesResource

        return FeaturesResource(self)

    @cached_property
    def datasets(self) -> DatasetsResource:
        from .resources.datasets import DatasetsResource

        return DatasetsResource(self)

    @cached_property
    def geocode(self) -> GeocodeResource:
        from .resources.geocode import GeocodeResource

        return GeocodeResource(self)

    @cached_property
    def search(self) -> SearchResource:
        from .resources.search import SearchResource

        return SearchResource(self)

    @cached_property
    def routing(self) -> RoutingResource:
        from .resources.routing import RoutingResource

        return RoutingResource(self)

    @cached_property
    def elevation(self) -> ElevationResource:
        from .resources.elevation import ElevationResource

        return ElevationResource(self)

    @cached_property
    def map_match(self) -> MapMatchResource:
        from .resources.map_match import MapMatchResource

        return MapMatchResource(self)

    @cached_property
    def optimize(self) -> OptimizeResource:
        from .resources.optimize import OptimizeResource

        return OptimizeResource(self)

    @cached_property
    def query(self) -> QueryResource:
        from .resources.query import QueryResource

        return QueryResource(self)

    @cached_property
    def tiles(self) -> TilesResource:
        from .resources.tiles import TilesResource

        return TilesResource(self)

    @cached_property
    def with_raw_response(self) -> PlazaWithRawResponse:
        return PlazaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlazaWithStreamedResponse:
        return PlazaWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncPlaza(AsyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["production", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "local"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncPlaza client instance.

        This automatically infers the `api_key` argument from the `PLAZA_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("PLAZA_API_KEY")
        if api_key is None:
            raise PlazaError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PLAZA_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("PLAZA_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `PLAZA_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def features(self) -> AsyncFeaturesResource:
        from .resources.features import AsyncFeaturesResource

        return AsyncFeaturesResource(self)

    @cached_property
    def datasets(self) -> AsyncDatasetsResource:
        from .resources.datasets import AsyncDatasetsResource

        return AsyncDatasetsResource(self)

    @cached_property
    def geocode(self) -> AsyncGeocodeResource:
        from .resources.geocode import AsyncGeocodeResource

        return AsyncGeocodeResource(self)

    @cached_property
    def search(self) -> AsyncSearchResource:
        from .resources.search import AsyncSearchResource

        return AsyncSearchResource(self)

    @cached_property
    def routing(self) -> AsyncRoutingResource:
        from .resources.routing import AsyncRoutingResource

        return AsyncRoutingResource(self)

    @cached_property
    def elevation(self) -> AsyncElevationResource:
        from .resources.elevation import AsyncElevationResource

        return AsyncElevationResource(self)

    @cached_property
    def map_match(self) -> AsyncMapMatchResource:
        from .resources.map_match import AsyncMapMatchResource

        return AsyncMapMatchResource(self)

    @cached_property
    def optimize(self) -> AsyncOptimizeResource:
        from .resources.optimize import AsyncOptimizeResource

        return AsyncOptimizeResource(self)

    @cached_property
    def query(self) -> AsyncQueryResource:
        from .resources.query import AsyncQueryResource

        return AsyncQueryResource(self)

    @cached_property
    def tiles(self) -> AsyncTilesResource:
        from .resources.tiles import AsyncTilesResource

        return AsyncTilesResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncPlazaWithRawResponse:
        return AsyncPlazaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlazaWithStreamedResponse:
        return AsyncPlazaWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class PlazaWithRawResponse:
    _client: Plaza

    def __init__(self, client: Plaza) -> None:
        self._client = client

    @cached_property
    def features(self) -> features.FeaturesResourceWithRawResponse:
        from .resources.features import FeaturesResourceWithRawResponse

        return FeaturesResourceWithRawResponse(self._client.features)

    @cached_property
    def datasets(self) -> datasets.DatasetsResourceWithRawResponse:
        from .resources.datasets import DatasetsResourceWithRawResponse

        return DatasetsResourceWithRawResponse(self._client.datasets)

    @cached_property
    def geocode(self) -> geocode.GeocodeResourceWithRawResponse:
        from .resources.geocode import GeocodeResourceWithRawResponse

        return GeocodeResourceWithRawResponse(self._client.geocode)

    @cached_property
    def search(self) -> search.SearchResourceWithRawResponse:
        from .resources.search import SearchResourceWithRawResponse

        return SearchResourceWithRawResponse(self._client.search)

    @cached_property
    def routing(self) -> routing.RoutingResourceWithRawResponse:
        from .resources.routing import RoutingResourceWithRawResponse

        return RoutingResourceWithRawResponse(self._client.routing)

    @cached_property
    def elevation(self) -> elevation.ElevationResourceWithRawResponse:
        from .resources.elevation import ElevationResourceWithRawResponse

        return ElevationResourceWithRawResponse(self._client.elevation)

    @cached_property
    def map_match(self) -> map_match.MapMatchResourceWithRawResponse:
        from .resources.map_match import MapMatchResourceWithRawResponse

        return MapMatchResourceWithRawResponse(self._client.map_match)

    @cached_property
    def optimize(self) -> optimize.OptimizeResourceWithRawResponse:
        from .resources.optimize import OptimizeResourceWithRawResponse

        return OptimizeResourceWithRawResponse(self._client.optimize)

    @cached_property
    def query(self) -> query.QueryResourceWithRawResponse:
        from .resources.query import QueryResourceWithRawResponse

        return QueryResourceWithRawResponse(self._client.query)

    @cached_property
    def tiles(self) -> tiles.TilesResourceWithRawResponse:
        from .resources.tiles import TilesResourceWithRawResponse

        return TilesResourceWithRawResponse(self._client.tiles)


class AsyncPlazaWithRawResponse:
    _client: AsyncPlaza

    def __init__(self, client: AsyncPlaza) -> None:
        self._client = client

    @cached_property
    def features(self) -> features.AsyncFeaturesResourceWithRawResponse:
        from .resources.features import AsyncFeaturesResourceWithRawResponse

        return AsyncFeaturesResourceWithRawResponse(self._client.features)

    @cached_property
    def datasets(self) -> datasets.AsyncDatasetsResourceWithRawResponse:
        from .resources.datasets import AsyncDatasetsResourceWithRawResponse

        return AsyncDatasetsResourceWithRawResponse(self._client.datasets)

    @cached_property
    def geocode(self) -> geocode.AsyncGeocodeResourceWithRawResponse:
        from .resources.geocode import AsyncGeocodeResourceWithRawResponse

        return AsyncGeocodeResourceWithRawResponse(self._client.geocode)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithRawResponse:
        from .resources.search import AsyncSearchResourceWithRawResponse

        return AsyncSearchResourceWithRawResponse(self._client.search)

    @cached_property
    def routing(self) -> routing.AsyncRoutingResourceWithRawResponse:
        from .resources.routing import AsyncRoutingResourceWithRawResponse

        return AsyncRoutingResourceWithRawResponse(self._client.routing)

    @cached_property
    def elevation(self) -> elevation.AsyncElevationResourceWithRawResponse:
        from .resources.elevation import AsyncElevationResourceWithRawResponse

        return AsyncElevationResourceWithRawResponse(self._client.elevation)

    @cached_property
    def map_match(self) -> map_match.AsyncMapMatchResourceWithRawResponse:
        from .resources.map_match import AsyncMapMatchResourceWithRawResponse

        return AsyncMapMatchResourceWithRawResponse(self._client.map_match)

    @cached_property
    def optimize(self) -> optimize.AsyncOptimizeResourceWithRawResponse:
        from .resources.optimize import AsyncOptimizeResourceWithRawResponse

        return AsyncOptimizeResourceWithRawResponse(self._client.optimize)

    @cached_property
    def query(self) -> query.AsyncQueryResourceWithRawResponse:
        from .resources.query import AsyncQueryResourceWithRawResponse

        return AsyncQueryResourceWithRawResponse(self._client.query)

    @cached_property
    def tiles(self) -> tiles.AsyncTilesResourceWithRawResponse:
        from .resources.tiles import AsyncTilesResourceWithRawResponse

        return AsyncTilesResourceWithRawResponse(self._client.tiles)


class PlazaWithStreamedResponse:
    _client: Plaza

    def __init__(self, client: Plaza) -> None:
        self._client = client

    @cached_property
    def features(self) -> features.FeaturesResourceWithStreamingResponse:
        from .resources.features import FeaturesResourceWithStreamingResponse

        return FeaturesResourceWithStreamingResponse(self._client.features)

    @cached_property
    def datasets(self) -> datasets.DatasetsResourceWithStreamingResponse:
        from .resources.datasets import DatasetsResourceWithStreamingResponse

        return DatasetsResourceWithStreamingResponse(self._client.datasets)

    @cached_property
    def geocode(self) -> geocode.GeocodeResourceWithStreamingResponse:
        from .resources.geocode import GeocodeResourceWithStreamingResponse

        return GeocodeResourceWithStreamingResponse(self._client.geocode)

    @cached_property
    def search(self) -> search.SearchResourceWithStreamingResponse:
        from .resources.search import SearchResourceWithStreamingResponse

        return SearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def routing(self) -> routing.RoutingResourceWithStreamingResponse:
        from .resources.routing import RoutingResourceWithStreamingResponse

        return RoutingResourceWithStreamingResponse(self._client.routing)

    @cached_property
    def elevation(self) -> elevation.ElevationResourceWithStreamingResponse:
        from .resources.elevation import ElevationResourceWithStreamingResponse

        return ElevationResourceWithStreamingResponse(self._client.elevation)

    @cached_property
    def map_match(self) -> map_match.MapMatchResourceWithStreamingResponse:
        from .resources.map_match import MapMatchResourceWithStreamingResponse

        return MapMatchResourceWithStreamingResponse(self._client.map_match)

    @cached_property
    def optimize(self) -> optimize.OptimizeResourceWithStreamingResponse:
        from .resources.optimize import OptimizeResourceWithStreamingResponse

        return OptimizeResourceWithStreamingResponse(self._client.optimize)

    @cached_property
    def query(self) -> query.QueryResourceWithStreamingResponse:
        from .resources.query import QueryResourceWithStreamingResponse

        return QueryResourceWithStreamingResponse(self._client.query)

    @cached_property
    def tiles(self) -> tiles.TilesResourceWithStreamingResponse:
        from .resources.tiles import TilesResourceWithStreamingResponse

        return TilesResourceWithStreamingResponse(self._client.tiles)


class AsyncPlazaWithStreamedResponse:
    _client: AsyncPlaza

    def __init__(self, client: AsyncPlaza) -> None:
        self._client = client

    @cached_property
    def features(self) -> features.AsyncFeaturesResourceWithStreamingResponse:
        from .resources.features import AsyncFeaturesResourceWithStreamingResponse

        return AsyncFeaturesResourceWithStreamingResponse(self._client.features)

    @cached_property
    def datasets(self) -> datasets.AsyncDatasetsResourceWithStreamingResponse:
        from .resources.datasets import AsyncDatasetsResourceWithStreamingResponse

        return AsyncDatasetsResourceWithStreamingResponse(self._client.datasets)

    @cached_property
    def geocode(self) -> geocode.AsyncGeocodeResourceWithStreamingResponse:
        from .resources.geocode import AsyncGeocodeResourceWithStreamingResponse

        return AsyncGeocodeResourceWithStreamingResponse(self._client.geocode)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithStreamingResponse:
        from .resources.search import AsyncSearchResourceWithStreamingResponse

        return AsyncSearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def routing(self) -> routing.AsyncRoutingResourceWithStreamingResponse:
        from .resources.routing import AsyncRoutingResourceWithStreamingResponse

        return AsyncRoutingResourceWithStreamingResponse(self._client.routing)

    @cached_property
    def elevation(self) -> elevation.AsyncElevationResourceWithStreamingResponse:
        from .resources.elevation import AsyncElevationResourceWithStreamingResponse

        return AsyncElevationResourceWithStreamingResponse(self._client.elevation)

    @cached_property
    def map_match(self) -> map_match.AsyncMapMatchResourceWithStreamingResponse:
        from .resources.map_match import AsyncMapMatchResourceWithStreamingResponse

        return AsyncMapMatchResourceWithStreamingResponse(self._client.map_match)

    @cached_property
    def optimize(self) -> optimize.AsyncOptimizeResourceWithStreamingResponse:
        from .resources.optimize import AsyncOptimizeResourceWithStreamingResponse

        return AsyncOptimizeResourceWithStreamingResponse(self._client.optimize)

    @cached_property
    def query(self) -> query.AsyncQueryResourceWithStreamingResponse:
        from .resources.query import AsyncQueryResourceWithStreamingResponse

        return AsyncQueryResourceWithStreamingResponse(self._client.query)

    @cached_property
    def tiles(self) -> tiles.AsyncTilesResourceWithStreamingResponse:
        from .resources.tiles import AsyncTilesResourceWithStreamingResponse

        return AsyncTilesResourceWithStreamingResponse(self._client.tiles)


Client = Plaza

AsyncClient = AsyncPlaza
