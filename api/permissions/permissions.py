from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        return request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        return request.user.is_staff

    
class IsAdminOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'PUT', 'PATCH', 'DELETE']:
            return request.user.is_staff or obj.user == request.user
        return False

    # def has_permission(self, request, view):
    #     return request.method in ['GET', 'PUT', 'PATCH', 'DELETE']
    
