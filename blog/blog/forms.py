from django import forms

from blog.models import Blog, Comment


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content')


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
