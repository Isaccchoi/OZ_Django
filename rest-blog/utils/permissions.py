from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            obj = view.get_object(request, *view.args, **view.kwargs)
        except TypeError:
            obj = view.get_object()
        return obj.author == request.user
