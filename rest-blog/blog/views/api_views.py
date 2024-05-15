from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Blog
from blog.serializers import BlogSerializer


class BlogListAPIView(APIView):
    def get(self, request, format=None):
        blog_list = Blog.objects.all().order_by('-created_at').select_related('author')
        paginator = PageNumberPagination()
        queryset = paginator.paginate_queryset(blog_list, request)

        serializer = BlogSerializer(queryset, many=True)
        return paginator.get_paginated_response(serializer.data)
