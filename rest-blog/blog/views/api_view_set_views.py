import json

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets

from blog.models import Blog
from blog.serializers import BlogSerializer, UserSerializer

User = get_user_model()


@csrf_exempt
def blog_list(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()

        data = {
            'blog_list': [{'id': blog.id, 'title': blog.title} for blog in blogs]
        }

        return JsonResponse(data, status=200)
    else:
        body = json.loads(request.body.decode('utf-8'))

        blog = Blog.objects.create(
            **body,
            author=User.objects.first()
        )

        data = {
            'id': blog.id,
            'title': blog.title,
            'content': blog.content,
            'author': blog.author.username
        }

        return JsonResponse(data, status=201)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

# ReadOnlyModelViewSet => List, Detail
# ModelViewSet => List, Detail, PUT, PATH, CREATE, DELETE


# /blog / GET => List / POST => Create
# /blog/1 / GET => Detail / PUT, PATCH => Update / DELETE => Delete


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all().order_by('-created_at').select_related('author')
    serializer_class = BlogSerializer
