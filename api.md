# V1

Types:

```python
from plaza.types import (
    V1CalculateDistanceMatrixResponse,
    V1CalculateRouteResponse,
    V1ExecuteSparqlResponse,
    V1SnapToNearestResponse,
)
```

Methods:

- <code title="post /api/v1/matrix">client.v1.<a href="./src/plaza/resources/v1/v1.py">calculate_distance_matrix</a>(\*\*<a href="src/plaza/types/v1_calculate_distance_matrix_params.py">params</a>) -> <a href="./src/plaza/types/v1_calculate_distance_matrix_response.py">V1CalculateDistanceMatrixResponse</a></code>
- <code title="get /api/v1/isochrone">client.v1.<a href="./src/plaza/resources/v1/v1.py">calculate_isochrone</a>(\*\*<a href="src/plaza/types/v1_calculate_isochrone_params.py">params</a>) -> <a href="./src/plaza/types/v1/geo_json_feature.py">GeoJsonFeature</a></code>
- <code title="post /api/v1/route">client.v1.<a href="./src/plaza/resources/v1/v1.py">calculate_route</a>(\*\*<a href="src/plaza/types/v1_calculate_route_params.py">params</a>) -> <a href="./src/plaza/types/v1_calculate_route_response.py">V1CalculateRouteResponse</a></code>
- <code title="post /api/v1/overpass">client.v1.<a href="./src/plaza/resources/v1/v1.py">execute_overpass</a>(\*\*<a href="src/plaza/types/v1_execute_overpass_params.py">params</a>) -> <a href="./src/plaza/types/v1/feature_collection.py">FeatureCollection</a></code>
- <code title="get /api/v1/query">client.v1.<a href="./src/plaza/resources/v1/v1.py">execute_query</a>(\*\*<a href="src/plaza/types/v1_execute_query_params.py">params</a>) -> <a href="./src/plaza/types/v1/feature_collection.py">FeatureCollection</a></code>
- <code title="post /api/v1/sparql">client.v1.<a href="./src/plaza/resources/v1/v1.py">execute_sparql</a>(\*\*<a href="src/plaza/types/v1_execute_sparql_params.py">params</a>) -> <a href="./src/plaza/types/v1_execute_sparql_response.py">V1ExecuteSparqlResponse</a></code>
- <code title="get /api/v1/nearby">client.v1.<a href="./src/plaza/resources/v1/v1.py">find_nearby</a>(\*\*<a href="src/plaza/types/v1_find_nearby_params.py">params</a>) -> <a href="./src/plaza/types/v1/feature_collection.py">FeatureCollection</a></code>
- <code title="get /api/v1/tiles/{z}/{x}/{y}">client.v1.<a href="./src/plaza/resources/v1/v1.py">get_tile</a>(y, \*, z, x) -> BinaryAPIResponse</code>
- <code title="get /api/v1/reverse-geocode">client.v1.<a href="./src/plaza/resources/v1/v1.py">reverse_geocode</a>(\*\*<a href="src/plaza/types/v1_reverse_geocode_params.py">params</a>) -> <a href="./src/plaza/types/v1/geo_json_feature.py">GeoJsonFeature</a></code>
- <code title="get /api/v1/search">client.v1.<a href="./src/plaza/resources/v1/v1.py">search_features</a>(\*\*<a href="src/plaza/types/v1_search_features_params.py">params</a>) -> <a href="./src/plaza/types/v1/feature_collection.py">FeatureCollection</a></code>
- <code title="get /api/v1/nearest">client.v1.<a href="./src/plaza/resources/v1/v1.py">snap_to_nearest</a>(\*\*<a href="src/plaza/types/v1_snap_to_nearest_params.py">params</a>) -> <a href="./src/plaza/types/v1_snap_to_nearest_response.py">V1SnapToNearestResponse</a></code>

## Datasets

Types:

```python
from plaza.types.v1 import DatasetResponse, FeatureCollection, DatasetListResponse
```

Methods:

- <code title="post /api/v1/datasets">client.v1.datasets.<a href="./src/plaza/resources/v1/datasets.py">create</a>(\*\*<a href="src/plaza/types/v1/dataset_create_params.py">params</a>) -> <a href="./src/plaza/types/v1/dataset_response.py">DatasetResponse</a></code>
- <code title="get /api/v1/datasets/{id}">client.v1.datasets.<a href="./src/plaza/resources/v1/datasets.py">retrieve</a>(id) -> <a href="./src/plaza/types/v1/dataset_response.py">DatasetResponse</a></code>
- <code title="get /api/v1/datasets">client.v1.datasets.<a href="./src/plaza/resources/v1/datasets.py">list</a>() -> <a href="./src/plaza/types/v1/dataset_list_response.py">DatasetListResponse</a></code>
- <code title="delete /api/v1/datasets/{id}">client.v1.datasets.<a href="./src/plaza/resources/v1/datasets.py">delete</a>(id) -> None</code>
- <code title="get /api/v1/datasets/{id}/features">client.v1.datasets.<a href="./src/plaza/resources/v1/datasets.py">query_features</a>(id, \*\*<a href="src/plaza/types/v1/dataset_query_features_params.py">params</a>) -> <a href="./src/plaza/types/v1/feature_collection.py">FeatureCollection</a></code>

## Elements

Types:

```python
from plaza.types.v1 import GeoJsonFeature, GeoJsonGeometry
```

Methods:

- <code title="get /api/v1/elements/{type}/{id}">client.v1.elements.<a href="./src/plaza/resources/v1/elements.py">retrieve</a>(id, \*, type) -> <a href="./src/plaza/types/v1/geo_json_feature.py">GeoJsonFeature</a></code>
- <code title="post /api/v1/elements/batch">client.v1.elements.<a href="./src/plaza/resources/v1/elements.py">fetch_batch</a>(\*\*<a href="src/plaza/types/v1/element_fetch_batch_params.py">params</a>) -> <a href="./src/plaza/types/v1/feature_collection.py">FeatureCollection</a></code>
- <code title="get /api/v1/elements">client.v1.elements.<a href="./src/plaza/resources/v1/elements.py">query</a>(\*\*<a href="src/plaza/types/v1/element_query_params.py">params</a>) -> <a href="./src/plaza/types/v1/feature_collection.py">FeatureCollection</a></code>

## Geocode

Types:

```python
from plaza.types.v1 import (
    GeocodeAutocompleteResponse,
    GeocodeForwardResponse,
    GeocodeReverseResponse,
)
```

Methods:

- <code title="get /api/v1/geocode/autocomplete">client.v1.geocode.<a href="./src/plaza/resources/v1/geocode.py">autocomplete</a>(\*\*<a href="src/plaza/types/v1/geocode_autocomplete_params.py">params</a>) -> <a href="./src/plaza/types/v1/geocode_autocomplete_response.py">GeocodeAutocompleteResponse</a></code>
- <code title="get /api/v1/geocode">client.v1.geocode.<a href="./src/plaza/resources/v1/geocode.py">forward</a>(\*\*<a href="src/plaza/types/v1/geocode_forward_params.py">params</a>) -> <a href="./src/plaza/types/v1/geocode_forward_response.py">GeocodeForwardResponse</a></code>
- <code title="get /api/v1/geocode/reverse">client.v1.geocode.<a href="./src/plaza/resources/v1/geocode.py">reverse</a>(\*\*<a href="src/plaza/types/v1/geocode_reverse_params.py">params</a>) -> <a href="./src/plaza/types/v1/geocode_reverse_response.py">GeocodeReverseResponse</a></code>
