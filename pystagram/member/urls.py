from django.urls import path

from . import views

app_name = 'profile'

urlpatterns = [
    path('<str:slug>/', views.UserProfileView.as_view(), name='detail'),
    path('<int:pk>/follow/', views.UserFollowingView.as_view(), name='follow'),
]