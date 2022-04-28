import django_filters
from Table.models import Stocktick


class DataFilter(django_filters.FilterSet):
    class Meta:
        model = Stocktick
        fields = '__all__'
