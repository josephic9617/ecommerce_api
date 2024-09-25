from django.contrib import admin
from main.models.category import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'is_root_parent',
        'parent_category',
        'icon_name',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'name',
        'description',
        'is_root_parent',
        'parent_category',
        'icon_name',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'id',
        'name',
        'description',
        'is_root_parent',
        'parent_category',
        'icon_name',
        'created_at',
        'updated_at',
    )