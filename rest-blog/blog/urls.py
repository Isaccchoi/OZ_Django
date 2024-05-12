from django.urls import include, path
from rest_framework import routers

from blog.views import api_views

app_name = 'api'

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', api_views.UserViewSet, basename='user')
router.register(r'blogs', api_views.BlogViewSet, basename='blog')

urlpatterns = [
    # path('', api_views.blog_list, name='blog_list'),
    path('', include(router.urls)),
]
