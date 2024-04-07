from django.contrib import admin

from bookmark.models import Bookmark


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url']
    list_display_links = ['name', 'url']
    list_filter = ['name', 'url']


# admin.site.register(Bookmark, BookmarkAdmin)
