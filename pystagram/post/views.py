from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView

from post.forms import PostForm
from post.models import Post


class PostListView(ListView):
    queryset = Post.objects.all().select_related('user').prefetch_related('images')
    template_name = 'post/list.html'
    paginate_by = 5
    ordering = ('-created_at', )


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post/form.html'
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user

        return HttpResponseRedirect(reverse('main'))
