from datetime import datetime

from django.db.models import Q
from django.utils import timezone
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import Blog
from blog.serializers import BlogSerializer
from utils.permissions import IsAuthorOrReadOnly


class BlogQuerySetMixin:
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(
            Q(published_at__isnull=True) |
            Q(published_at__gte=timezone.now())
        ).order_by('-created_at').select_related('author')


class BlogListAPIView(BlogQuerySetMixin, ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogRetrieveAPIView(BlogQuerySetMixin, RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly, ]
