from rest_framework import serializers
from main.models.clothing import Clothing, ClothingImage


class ClothingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingImage
        fields = ('get_image', 'image_name')

class ClothingSerializer(serializers.ModelSerializer):
    images = ClothingImageSerializer(many=True, read_only=True)

    def get_images(self, instance):
        images = instance.images.all()

    class Meta:
        model = Clothing
        fields = '__all__'