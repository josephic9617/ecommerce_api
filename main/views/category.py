from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from main.models.category import Category
from main.serializers.category import CategorySerializer
from main.filters.category import CategoryFilter



class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all().filter(is_root_parent=True)
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter