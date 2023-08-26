from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from products.models import Product

# For static views
class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home', 'contact', 'faq']

    def location(self, obj):
        return reverse(obj)

# For dynamic product views
class ProductSitemap(Sitemap):
    def items(self):
        return Product.objects.all()

    def location(self, obj):
        return reverse('product_detail', args=[str(obj.id)])
