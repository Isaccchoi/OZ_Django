from django.shortcuts import get_object_or_404, render

from blog.models import Blog


def blog_list(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs
    }
    return render(request, 'blog_list.html', context)
