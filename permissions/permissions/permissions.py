from rest_framework import permissions, viewsets


class IsAnalyst(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_anonymous and user.is_analyst:
            return True

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Check if user Bank Analyst
        obj = getattr(obj, "bank", obj)
        return obj.user == user


class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_anonymous and user.is_customer:
            return True

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class PermissionsViewSet(viewsets.ViewSet):
    permissions = []
    read_permissions = []
    update_permissions = []

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = self.read_permissions
        elif self.request.method == 'PUT':
            self.permission_classes = self.update_permissions

        return super().get_permissions()
