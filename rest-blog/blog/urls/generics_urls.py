from django.urls import path

from blog.views import generics_views as views

app_name = 'generics_api'


urlpatterns = [
    path('blog', views.BlogListAPIView.as_view(), name='blog_list'),
    path('blog/<int:pk>', views.BlogRetrieveAPIView.as_view(), name='blog_detail'),
]
