import pytest
from django.urls import reverse, reverse_lazy
from django.utils import timezone

from core.models import Users, Companies, RolesDict, UserRoles
from tests.conftest import create_permissions


@pytest.mark.django_db
def test_user_registration_flow(client):
    """Полный тест процесса регистрации пользователя через UI"""
    # Шаг 1: Получение формы регистрации
    create_permissions()
    response = client.get(reverse_lazy('register'))
    assert response.status_code == 200
    username = 'new_user'
    # Шаг 2: Отправка валидных данных
    response = client.post(reverse_lazy('register'), {
        'username': username,
        'password': 'SecurePass123!',
        'password_confirm': 'SecurePass123!',
        'firstname': 'Иван',
        'lastname': 'Петров'
    }, follow=True)
    role = RolesDict.objects.get(name='Супер админ')
    user = Users.objects.get(username=username)
    if role:
        UserRoles.objects.create(
            user=user,
            role=role,
            active_from=timezone.now().date(),
            active_to=None
        )

    # Проверка редиректа после успешной регистрации
    assert response.status_code == 200

    # Проверка создания пользователя в БД
    assert Users.objects.filter(username='new_user').exists()


@pytest.mark.django_db
def test_company_registration_flow(client, authenticated_user):
    """Тест регистрации компании через UI"""
    create_permissions()
    # Аутентификация пользователя
    client.force_login(authenticated_user)
    role = RolesDict.objects.get(name='Супер админ')
    user = Users.objects.get(username=authenticated_user.username)
    if role:
        UserRoles.objects.create(
            user=user,
            role=role,
            active_from=timezone.now().date(),
            active_to=None
        )

    # Получение формы
    response = client.get(reverse_lazy('register_company'))
    assert response.status_code == 200

    # Отправка данных
    response = client.post(reverse_lazy('register_company'), {
        'name': 'Тестовая компания',
        'inn': '1234567890',
        'kpp': '123456789',
        'ogrn': '1234567890123'
    }, follow=True)

    # Проверка результатов
    assert response.status_code == 200
    assert Companies.objects.filter(inn='1234567890').exists()