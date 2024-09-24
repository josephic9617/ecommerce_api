from rest_framework import generics
from main.models.category import Category
from main.serializers.category import CategorySerializer



class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all().filter(is_root_parent=True)
    serializer_class = CategorySerializer