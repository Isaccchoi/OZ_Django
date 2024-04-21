from django.urls import path

from blog import cb_views

app_name = 'blog'

urlpatterns = [
    # CBV blog
    path('', cb_views.BlogListView.as_view(), name='list'),
    path('<int:pk>/', cb_views.BlogDetailView.as_view(), name='detail'),
    path('create/', cb_views.BlogCreateView.as_view(), name='create'),
    path('<int:pk>/update/', cb_views.BlogUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', cb_views.BlogDeleteView.as_view(), name='delete'),

    path('comment/create/<int:blog_pk>/', cb_views.CommentCreateView.as_view(), name='comment_create'),
]

# {% url 'blog_list' %}
# {% url 'blog:list' %}
# {% url 'comment:list' %}