from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = "You must be the owner of this object."

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
