# Generated by Django 5.0.6 on 2024-09-24 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_clothing_clothingimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clothingimage',
            old_name='image_name',
            new_name='name',
        ),
    ]
