from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_root_parent = models.BooleanField(default=False)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    icon_name = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name