# Generated by Django 4.1.1 on 2023-08-23 21:04

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_image_url_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dghprmi1e/image/upload/v1692824558/noimage.jpg', max_length=255, verbose_name='image'),
        ),
    ]