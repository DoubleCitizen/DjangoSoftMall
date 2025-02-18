from django.http import HttpResponseForbidden
from rest_framework import permissions

from core.consts import RolesFunctionsViewSet
from core.models import UserRoles, RoleFunctions, FunctionsDict


def has_permission(user, function_code):
    """
    Проверяет, есть ли у пользователя право на выполнение функции.
    """
    # Получаем все роли пользователя
    user_roles = UserRoles.objects.filter(user=user)

    # Получаем все функции, связанные с ролями пользователя
    role_functions = RoleFunctions.objects.filter(role__in=user_roles.values_list('role', flat=True))

    # Проверяем, есть ли нужная функция среди доступных
    if isinstance(function_code, str):
        return role_functions.filter(
            function_code__code=function_code
        ).exists()
    else:
        return role_functions.filter(
            function_code__code=function_code.value
        ).exists()

def role_required(function_code):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not has_permission(request.user, function_code):
                return HttpResponseForbidden("У вас нет прав для выполнения этого действия.")
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

class CustomPermission(permissions.BasePermission):
    """
    Разрешение, основанное на роли пользователя и коде функции.
    """
    function_code = None

    def has_permission(self, request, view):
        # Проверяем, что пользователь аутентифицирован
        if not request.user.is_authenticated:
            return False

        # Проверяем, есть ли у пользователя разрешение на выполнение функции
        return has_permission(request.user, self.function_code)

class PermissionClasses:
    permission_classes = {}

    # Создаем классы разрешений для разных кодов
    for code in RolesFunctionsViewSet:
        permission_class = type(
            f'{code.value}',
            (CustomPermission,),
            {'function_code': code.value}  # Устанавливаем атрибут класса
        )

        permission_classes[code.value] = permission_class

