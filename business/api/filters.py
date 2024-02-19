import django_filters
from business.models import Value

class ValueFilter(django_filters.FilterSet):
    timestamp__gt = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='gt')
    timestamp__lt = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='lt')
    timestamp__lte = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='lte')
    timestamp__gte = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='gte')

    class Meta:
        model = Value
        fields = []