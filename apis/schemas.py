from drf_yasg import openapi


top_k_params = openapi.Parameter(
    name='top_k',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_INTEGER,
    default=5,
    description='Number of top common words to retrieve. Default=5'
)
