# Plaza

Types:

```python
from plaza.types import Error, FeatureCollection, GeoJsonFeature, GeoJsonGeometry
```

# Elements

Types:

```python
from plaza.types import BatchRequest
```

Methods:

- <code title="get /api/v1/features/{type}/{id}">client.elements.<a href="./src/plaza/resources/elements.py">retrieve</a>(id, \*, type) -> <a href="./src/plaza/types/geo_json_feature.py">GeoJsonFeature</a></code>
- <code title="post /api/v1/features/batch">client.elements.<a href="./src/plaza/resources/elements.py">batch</a>(\*\*<a href="src/plaza/types/element_batch_params.py">params</a>) -> <a href="./src/plaza/types/feature_collection.py">FeatureCollection</a></code>
- <code title="post /api/v1/features/lookup">client.elements.<a href="./src/plaza/resources/elements.py">lookup</a>() -> <a href="./src/plaza/types/geo_json_feature.py">GeoJsonFeature</a></code>
- <code title="get /api/v1/features/nearby">client.elements.<a href="./src/plaza/resources/elements.py">nearby</a>(\*\*<a href="src/plaza/types/element_nearby_params.py">params</a>) -> <a href="./src/plaza/types/feature_collection.py">FeatureCollection</a></code>
- <code title="post /api/v1/features/nearby">client.elements.<a href="./src/plaza/resources/elements.py">nearby_post</a>(\*\*<a href="src/plaza/types/element_nearby_post_params.py">params</a>) -> <a href="./src/plaza/types/feature_collection.py">FeatureCollection</a></code>
- <code title="get /api/v1/features">client.elements.<a href="./src/plaza/resources/elements.py">query</a>(\*\*<a href="src/plaza/types/element_query_params.py">params</a>) -> <a href="./src/plaza/types/feature_collection.py">FeatureCollection</a></code>
- <code title="post /api/v1/features">client.elements.<a href="./src/plaza/resources/elements.py">query_post</a>(\*\*<a href="src/plaza/types/element_query_post_params.py">params</a>) -> <a href="./src/plaza/types/feature_collection.py">FeatureCollection</a></code>

# Datasets

Types:

```python
from plaza.types import Dataset, DatasetList
```

Methods:

- <code title="post /api/v1/datasets">client.datasets.<a href="./src/plaza/resources/datasets.py">create</a>(\*\*<a href="src/plaza/types/dataset_create_params.py">params</a>) -> <a href="./src/plaza/types/dataset.py">Dataset</a></code>
- <code title="get /api/v1/datasets/{id}">client.datasets.<a href="./src/plaza/resources/datasets.py">retrieve</a>(id) -> <a href="./src/plaza/types/dataset.py">Dataset</a></code>
- <code title="get /api/v1/datasets">client.datasets.<a href="./src/plaza/resources/datasets.py">list</a>() -> <a href="./src/plaza/types/dataset_list.py">DatasetList</a></code>
- <code title="delete /api/v1/datasets/{id}">client.datasets.<a href="./src/plaza/resources/datasets.py">delete</a>(id) -> None</code>
- <code title="get /api/v1/datasets/{id}/features">client.datasets.<a href="./src/plaza/resources/datasets.py">features</a>(id, \*\*<a href="src/plaza/types/dataset_features_params.py">params</a>) -> <a href="./src/plaza/types/feature_collection.py">FeatureCollection</a></code>

# Geocode

Types:

```python
from plaza.types import (
    AutocompleteResult,
    GeocodeResult,
    GeocodingFeature,
    ReverseGeocodeResult,
    GeocodeBatchResponse,
)
```

Methods:

- <code title="get /api/v1/geocode/autocomplete">client.geocode.<a href="./src/plaza/resources/geocode.py">autocomplete</a>(\*\*<a href="src/plaza/types/geocode_autocomplete_params.py">params</a>) -> <a href="./src/plaza/types/autocomplete_result.py">AutocompleteResult</a></code>
- <code title="post /api/v1/geocode/autocomplete">client.geocode.<a href="./src/plaza/resources/geocode.py">autocomplete_post</a>(\*\*<a href="src/plaza/types/geocode_autocomplete_post_params.py">params</a>) -> <a href="./src/plaza/types/autocomplete_result.py">AutocompleteResult</a></code>
- <code title="post /api/v1/geocode/batch">client.geocode.<a href="./src/plaza/resources/geocode.py">batch</a>(\*\*<a href="src/plaza/types/geocode_batch_params.py">params</a>) -> <a href="./src/plaza/types/geocode_batch_response.py">GeocodeBatchResponse</a></code>
- <code title="get /api/v1/geocode">client.geocode.<a href="./src/plaza/resources/geocode.py">forward</a>(\*\*<a href="src/plaza/types/geocode_forward_params.py">params</a>) -> <a href="./src/plaza/types/geocode_result.py">GeocodeResult</a></code>
- <code title="post /api/v1/geocode">client.geocode.<a href="./src/plaza/resources/geocode.py">forward_post</a>(\*\*<a href="src/plaza/types/geocode_forward_post_params.py">params</a>) -> <a href="./src/plaza/types/geocode_result.py">GeocodeResult</a></code>
- <code title="get /api/v1/geocode/reverse">client.geocode.<a href="./src/plaza/resources/geocode.py">reverse</a>(\*\*<a href="src/plaza/types/geocode_reverse_params.py">params</a>) -> <a href="./src/plaza/types/reverse_geocode_result.py">ReverseGeocodeResult</a></code>
- <code title="post /api/v1/geocode/reverse">client.geocode.<a href="./src/plaza/resources/geocode.py">reverse_post</a>(\*\*<a href="src/plaza/types/geocode_reverse_post_params.py">params</a>) -> <a href="./src/plaza/types/reverse_geocode_result.py">ReverseGeocodeResult</a></code>

# Search

Methods:

- <code title="get /api/v1/search">client.search.<a href="./src/plaza/resources/search.py">query</a>(\*\*<a href="src/plaza/types/search_query_params.py">params</a>) -> <a href="./src/plaza/types/feature_collection.py">FeatureCollection</a></code>
- <code title="post /api/v1/search">client.search.<a href="./src/plaza/resources/search.py">query_post</a>(\*\*<a href="src/plaza/types/search_query_post_params.py">params</a>) -> <a href="./src/plaza/types/feature_collection.py">FeatureCollection</a></code>

# Routing

Types:

```python
from plaza.types import (
    MatrixRequest,
    MatrixResult,
    NearestResult,
    RouteRequest,
    RouteResult,
    RoutingIsochroneResponse,
    RoutingIsochronePostResponse,
)
```

Methods:

- <code title="get /api/v1/isochrone">client.routing.<a href="./src/plaza/resources/routing.py">isochrone</a>(\*\*<a href="src/plaza/types/routing_isochrone_params.py">params</a>) -> <a href="./src/plaza/types/routing_isochrone_response.py">RoutingIsochroneResponse</a></code>
- <code title="post /api/v1/isochrone">client.routing.<a href="./src/plaza/resources/routing.py">isochrone_post</a>(\*\*<a href="src/plaza/types/routing_isochrone_post_params.py">params</a>) -> <a href="./src/plaza/types/routing_isochrone_post_response.py">RoutingIsochronePostResponse</a></code>
- <code title="post /api/v1/matrix">client.routing.<a href="./src/plaza/resources/routing.py">matrix</a>(\*\*<a href="src/plaza/types/routing_matrix_params.py">params</a>) -> <a href="./src/plaza/types/matrix_result.py">MatrixResult</a></code>
- <code title="get /api/v1/nearest">client.routing.<a href="./src/plaza/resources/routing.py">nearest</a>(\*\*<a href="src/plaza/types/routing_nearest_params.py">params</a>) -> <a href="./src/plaza/types/nearest_result.py">NearestResult</a></code>
- <code title="post /api/v1/nearest">client.routing.<a href="./src/plaza/resources/routing.py">nearest_post</a>(\*\*<a href="src/plaza/types/routing_nearest_post_params.py">params</a>) -> <a href="./src/plaza/types/nearest_result.py">NearestResult</a></code>
- <code title="post /api/v1/route">client.routing.<a href="./src/plaza/resources/routing.py">route</a>(\*\*<a href="src/plaza/types/routing_route_params.py">params</a>) -> <a href="./src/plaza/types/route_result.py">RouteResult</a></code>

# Elevation

Types:

```python
from plaza.types import (
    ElevationBatchResult,
    ElevationLookupResult,
    ElevationProfileRequest,
    ElevationProfileResult,
)
```

Methods:

- <code title="post /api/v1/elevation/batch">client.elevation.<a href="./src/plaza/resources/elevation.py">batch</a>(\*\*<a href="src/plaza/types/elevation_batch_params.py">params</a>) -> <a href="./src/plaza/types/elevation_batch_result.py">ElevationBatchResult</a></code>
- <code title="get /api/v1/elevation">client.elevation.<a href="./src/plaza/resources/elevation.py">lookup</a>(\*\*<a href="src/plaza/types/elevation_lookup_params.py">params</a>) -> <a href="./src/plaza/types/elevation_lookup_result.py">ElevationLookupResult</a></code>
- <code title="post /api/v1/elevation">client.elevation.<a href="./src/plaza/resources/elevation.py">lookup_post</a>(\*\*<a href="src/plaza/types/elevation_lookup_post_params.py">params</a>) -> <a href="./src/plaza/types/elevation_lookup_result.py">ElevationLookupResult</a></code>
- <code title="post /api/v1/elevation/profile">client.elevation.<a href="./src/plaza/resources/elevation.py">profile</a>(\*\*<a href="src/plaza/types/elevation_profile_params.py">params</a>) -> <a href="./src/plaza/types/elevation_profile_result.py">ElevationProfileResult</a></code>

# MapMatch

Types:

```python
from plaza.types import MapMatchRequest, MapMatchResult
```

Methods:

- <code title="post /api/v1/map-match">client.map_match.<a href="./src/plaza/resources/map_match.py">match</a>(\*\*<a href="src/plaza/types/map_match_match_params.py">params</a>) -> <a href="./src/plaza/types/map_match_result.py">MapMatchResult</a></code>

# Optimize

Types:

```python
from plaza.types import (
    OptimizeCompletedResult,
    OptimizeJobStatus,
    OptimizeProcessingResult,
    OptimizeRequest,
    OptimizeResult,
)
```

Methods:

- <code title="post /api/v1/optimize">client.optimize.<a href="./src/plaza/resources/optimize.py">create</a>(\*\*<a href="src/plaza/types/optimize_create_params.py">params</a>) -> <a href="./src/plaza/types/optimize_result.py">OptimizeResult</a></code>
- <code title="get /api/v1/optimize/{job_id}">client.optimize.<a href="./src/plaza/resources/optimize.py">retrieve</a>(job_id) -> <a href="./src/plaza/types/optimize_job_status.py">OptimizeJobStatus</a></code>

# Query

Types:

```python
from plaza.types import PlazaqlQuery
```

Methods:

- <code title="post /api/v1/query">client.query.<a href="./src/plaza/resources/query.py">execute</a>(\*\*<a href="src/plaza/types/query_execute_params.py">params</a>) -> <a href="./src/plaza/types/feature_collection.py">FeatureCollection</a></code>

# Tiles

Methods:

- <code title="get /api/v1/tiles/{z}/{x}/{y}">client.tiles.<a href="./src/plaza/resources/tiles.py">get</a>(y, \*, z, x) -> BinaryAPIResponse</code>
