from django.urls import path

from blog.views import api_views

app_name = 'api'

urlpatterns = [
    path('', api_views.blog_list, name='blog_list'),
]