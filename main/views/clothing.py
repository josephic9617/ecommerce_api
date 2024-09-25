from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from main.models.clothing import Clothing
from main.serializers.clothing import ClothingSerializer
from main.filters.clothing import ClothingFilter



class ClothingView(generics.ListAPIView):
    queryset = Clothing.objects.all()
    serializer_class = ClothingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClothingFilter
