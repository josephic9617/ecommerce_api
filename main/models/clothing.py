from django.db import models
from main.models.product import Product
from django.conf import settings


class Clothing(Product):
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ClothingImage(models.Model):
    clothing = models.ForeignKey(Clothing, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='clothing_images')
    image_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.clothing.name

    def get_image(self):
        if self.image:
            return settings.API_URL + self.image.url
        else:
            return ''