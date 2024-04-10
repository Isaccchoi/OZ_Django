from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from bookmark.models import Bookmark


def bookmark_list(request):
    bookmarks = Bookmark.objects.filter(id__gte=50)
    # SELECT * FROM bookmark

    context = {
        'bookmarks': bookmarks
    }
    return render(request, 'bookmark_list.html', context)


def bookmark_detail(request, pk):
    # try:
    #     bookmark = Bookmark.objects.get(pk=pk)
    # except:
    #     # from django.http import Http404
    #     raise Http404

    # from django.shortcuts import get_object_or_404
    bookmark = get_object_or_404(Bookmark, pk=pk)

    context = {'bookmark': bookmark}
    return render(request, 'bookmark_detail.html', context)


################
# Mini Project #
################

# for i in range(10):
#     Bookmark.objects.create(name=f'테스트 네이버 {i}', url=f'https://naver.com')

# bookmark_list = [Bookmark(name=f'테스트 구글 {i}', url=f'https://google.com') for i in range(10)]
# Bookmark.objects.bulk_create(bookmark_list)
# new_bookmark_list = [Bookmark(name=f'테스트 야후 {i}', url=f'https://yahoo.com') for i in range(80)]
# Bookmark.objects.bulk_create(new_bookmark_list)
# Bookmark.objects.count()
