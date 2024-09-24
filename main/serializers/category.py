from rest_framework import serializers
from main.models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'icon_name', 'subcategories',)

    def get_subcategories(self, instance):
        subcategories = instance.category_set.all()
        serializer = CategorySerializer(subcategories, many=True)
        return serializer.data