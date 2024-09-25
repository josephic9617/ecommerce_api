from django.contrib import admin

class ClothingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'made_in',
        'description',
        'price',
        'category',
        'size',
        'color',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'name',
        'made_in',
        'description',
        'price',
        'category',
        'size',
        'color',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'id',
        'name',
        'made_in',
        'description',
        'price',
        'category',
        'size',
        'color',
        'created_at',
        'updated_at',
    )

class ClothingImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'get_image',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'name',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'id',
        'name',
        'get_image',
        'created_at',
        'updated_at',
    )