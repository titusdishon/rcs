from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = "You are not the author so you're not allowed to perform any action."
    my_safe_method = ["GET","PUT"]

    def has_permission(self, request, view):
        if request.method in self.my_safe_method:
            return True
        return False

    def has_object_permission(self, request,view, obj):

        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user