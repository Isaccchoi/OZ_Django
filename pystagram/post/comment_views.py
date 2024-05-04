from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView

from post.forms import CommentForm
from post.models import Comment, Post


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user

        post = Post.objects.get(pk=self.kwargs.get('post_pk'))
        self.object.post = post
        self.object.save()

        return HttpResponseRedirect(reverse('main'))
