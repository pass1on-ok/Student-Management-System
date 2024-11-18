from rest_framework import permissions

class IsNotStudent(permissions.BasePermission):
    """
    Custom permission to allow access only to users who are not students.
    """

    def has_permission(self, request, view):
        # Проверяем, что пользователь аутентифицирован и его роль не 'student'
        return request.user.is_authenticated and (getattr(request.user, 'role', None) == 'admin' or getattr(request.user, 'role', None) != 'teacher')