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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path

from member import views as member_views
from post import views as post_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # post
    path('', post_views.PostListView.as_view(), name='main'),
    path('create/', post_views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/update/', post_views.PostUpdateView.as_view(), name='update'),

    # like
    path('like/', post_views.toggle_like, name='toggle_like'),

    # auth
    path('signup/', member_views.SignupView.as_view(), name='signup'),
    path('verify/', member_views.verify_email, name='verify_email'),
    path('login/', member_views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # search
    path('search/', post_views.search, name='search'),

    # include
    path('comment/', include('post.comment_urls')),
    path('profile/', include('member.urls')),
    path('oauth/', include('member.oauth_urls')),

    # path('signup/done/', TemplateView.as_view(template_name='auth/signup_done.html'),
    #      name='signup_done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
