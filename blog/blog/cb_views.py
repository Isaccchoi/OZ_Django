from django.db.models import Q
from django.views.generic import ListView

from blog.models import Blog


class BlogListView(ListView):
    # model = Blog
    # queryset = Blog.objects.all().order_by('-created_at')
    queryset = Blog.objects.all()
    template_name = 'blog_list.html'
    paginate_by = 10
    ordering = ('-created_at', )

    def get_queryset(self):
        queryset = super().get_queryset()

        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(content__icontains=q)
            )
        return queryset
