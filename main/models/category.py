from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_root_parent = models.BooleanField(default=False)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    icon_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name