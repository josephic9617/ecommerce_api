import django_filters
from main.models.clothing import Clothing


class ClothingFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains", label="Clothing name")

    class Meta:
        model = Clothing
        fields = ('name',)