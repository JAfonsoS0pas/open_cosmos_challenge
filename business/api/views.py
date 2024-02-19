from rest_framework import viewsets
from business.models import Value
from .serializers import ValueSerializer
from .filters import ValueFilter
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter('timestamp__gt', openapi.IN_QUERY, description="Filter by timestamp greater than", type=openapi.TYPE_STRING),
        openapi.Parameter('timestamp__lt', openapi.IN_QUERY, description="Filter by timestamp less than", type=openapi.TYPE_STRING),
        openapi.Parameter('timestamp__gte', openapi.IN_QUERY, description="Filter by timestamp greater than or equal to", type=openapi.TYPE_STRING),
        openapi.Parameter('timestamp__lte', openapi.IN_QUERY, description="Filter by timestamp less than or equal to", type=openapi.TYPE_STRING),
    ],
    operation_summary="Filter values by timestamp",
    operation_description="Filter values based on timestamp field",
)
class ValueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer
    filterset_class = ValueFilter
