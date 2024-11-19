from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Faqat adminlarga yozish, o'chirish va yangilash imkoniyati bor. Boshqalar faqat o'qiy oladi.
    """
    def has_permission(self, request, view):
        if request.method in ['GET']:
            return True
        return request.user and request.user.is_staff
