from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, schema
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
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


class BlogDetailAPIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        blog_list = Blog.objects.all().select_related('author')
        pk = kwargs.get('pk', 0)
        # if not pk:
        #     raise Http404

        # blog = blog_list.filter(pk=pk).first()
        # if not blog:
        #     raise Http404

        blog = get_object_or_404(blog_list, pk=pk)

        serializer = BlogSerializer(blog, many=False)
        return Response(serializer.data)


@api_view(['GET'])
@schema(AutoSchema())
def detail_view(request, pk):
    blog_list = Blog.objects.all().select_related('author')

    blog = get_object_or_404(blog_list, pk=pk)

    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)
