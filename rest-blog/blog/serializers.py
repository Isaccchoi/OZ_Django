from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog.models import Blog

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Blog
        fields = ['title', 'content', 'author', 'published_at', 'created_at', 'updated_at']
