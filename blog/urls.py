from django.conf import settings
from django.contrib import admin
from django.urls import path
from blog.views import blog, post, category_post_list, allposts


urlpatterns = [
    path('post/<slug>/', post, name='post'),
    path('posts/', allposts, name='allposts'),
]
