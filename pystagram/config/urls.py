"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from member import views as member_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # auth
    path('signup/', member_views.SignupView.as_view(), name='signup'),
    path('verify/', member_views.verify_email, name='verify_email'),
    # path('signup/done/', TemplateView.as_view(template_name='auth/signup_done.html'),
    #      name='signup_done'),

]
