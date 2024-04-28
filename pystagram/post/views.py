from django.shortcuts import render
from django.views.generic import ListView

from post.models import Post


class PostListView(ListView):
    queryset = Post.objects.all().select_related('user').prefetch_related('images')
    template_name = 'post/list.html'
    paginate_by = 20
    ordering = ('-created_at', )
