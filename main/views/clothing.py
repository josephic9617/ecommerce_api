from rest_framework import generics
from main.models.clothing import Clothing
from main.serializers.clothing import ClothingSerializer



class ClothingView(generics.ListAPIView):
    queryset = Clothing.objects.all()
    serializer_class = ClothingSerializer