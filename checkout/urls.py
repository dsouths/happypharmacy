from django.urls import path
from . import views
from .webhooks import webhook
from .views import apply_coupon

app_name = 'checkout'

urlpatterns = [
    path('apply_coupon/', apply_coupon, name='apply_coupon'),
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]