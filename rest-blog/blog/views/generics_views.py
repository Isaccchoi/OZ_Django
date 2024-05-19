from datetime import datetime

from django.db.models import Q
from django.utils import timezone
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import Blog
from blog.serializers import BlogSerializer


class BlogQuerySetMixin:
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(
            Q(published_at__isnull=True) |
            Q(published_at__gte=timezone.now())
        ).order_by('-created_at').select_related('author')


class BlogListAPIView(BlogQuerySetMixin, ListAPIView):
    pass


class BlogRetrieveAPIView(BlogQuerySetMixin, RetrieveAPIView):
    pass
