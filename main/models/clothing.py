from django.db import models
from main.models.product import Product
from django.conf import settings


class Clothing(Product):
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name

class ClothingImage(models.Model):
    clothing = models.ForeignKey(Clothing, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='clothing_images')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.clothing.name

    def get_image(self):
        if self.image:
            return settings.API_URL + self.image.url
        else:
            return ''