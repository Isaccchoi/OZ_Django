from django.urls import path

from blog.views.api_views import BlogListAPIView

app_name = 'api'


urlpatterns = [
    path('blog', BlogListAPIView.as_view(), name='blog_list'),
]
