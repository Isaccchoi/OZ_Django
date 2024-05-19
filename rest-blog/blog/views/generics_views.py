from datetime import datetime

from django.db.models import Q
from django.utils import timezone
from rest_framework.generics import DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, \
    get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import Blog, Comment
from blog.serializers import BlogSerializer, CommentSerializer, CommentUpdateSerializer
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


class BlogRetrieveUpdateDestroyAPIView(BlogQuerySetMixin, RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly, ]


class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        blog = self.get_blog_object()
        serializer.save(author=self.request.user, blog=blog)

    def get_queryset(self):
        queryset = super().get_queryset()
        blog = self.get_blog_object()
        return queryset.filter(blog=blog)

    def get_blog_object(self):
        return get_object_or_404(Blog, pk=self.kwargs.get('blog_pk'))


class CommentUpdateDestroyAPIView(UpdateAPIView, DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer
    permission_classes = [IsAuthorOrReadOnly]
