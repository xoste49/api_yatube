from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Проверка является ли автором или безопасный метод
    """
    def has_permission(self, request, view):
        # Проверяем авторизован ли пользователь или только безопасные запросы
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        # Разрешения на чтение разрешены для любого запроса,
        # поэтому мы всегда разрешаем запросы GET, HEAD или OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Экземпляр должен иметь атрибут с именем `author`.
        return obj.author == request.user
