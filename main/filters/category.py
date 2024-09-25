import django_filters
from main.models.category import Category


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains", label="Category name")
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), label="Parent Category")

    class Meta:
        model = Category
        fields = ('name', 'category',)