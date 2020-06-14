from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    객체의 소유자에게만 쓰기를 허용하는 커스텀 권한
    """

    def has_object_permission(self, request, view, user):
        if request.method in permissions.SAFE_METHODS:
            return True

        return user.owner == request.user
