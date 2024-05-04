from django.urls import path
from . import comment_views as views

app_name = 'comment'

urlpatterns = [
    path('create/<int:post_pk>/', views.CommentCreateView.as_view(), name='create')
]