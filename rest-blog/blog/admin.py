from django.contrib import admin

from blog.models import Blog


# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    class Meta:
        model = Blog
