from django.shortcuts import get_object_or_404, render

from blog.models import Blog


def blog_list(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs
    }
    return render(request, 'blog_list.html', context)


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {'blog': blog}
    return render(request, 'blog_detail.html', context)


# 쿠키와 세션에서 사용한 blog_list
# def blog_list_with_cookie_and_session(request):
#     blogs = Blog.objects.all()
#
#     visits = int(request.COOKIES.get('visits', 0)) + 1
#
#     request.session['count'] = request.session.get('count', 0) + 1
#
#     context = {
#         'blogs': blogs,
#         'count': request.session['count']
#     }
#
#     response = render(request, 'blog_list.html', context)
#
#     response.set_cookie('visits', visits)
#
#     return response
