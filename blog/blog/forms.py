from django import forms
from django_summernote.widgets import SummernoteWidget

from blog.models import Blog, Comment


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('category', 'title', 'image', 'content', )
        widgets = {
            'content': SummernoteWidget()
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'content': '댓글'
        }
