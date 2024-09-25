from django.contrib import admin
from main.models.category import Category
from main.admins.category import CategoryAdmin
from main.models.clothing import Clothing, ClothingImage
from main.admins.clothing import ClothingAdmin, ClothingImageAdmin



admin.site.register(Category, CategoryAdmin)
admin.site.register(Clothing, ClothingAdmin)
admin.site.register(ClothingImage, ClothingImageAdmin)
