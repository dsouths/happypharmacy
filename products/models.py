from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Category(models.Model):
    verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    directions = models.TextField()
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True)
    image = CloudinaryField('image', default='https://res.cloudinary.com/dghprmi1e/image/upload/v1692824558/noimage.jpg')
    stock_level = models.IntegerField(default=10)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name


class ProductReview(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='reviews',
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        related_name='reviews',
        on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=10000)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title



