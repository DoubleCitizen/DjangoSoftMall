import os

import pytest
from django.core.management import call_command

from core.consts import RolesFunctions, RolesFunctionsViewSet
from core.models import Users, FunctionsDict, RolesDict, RoleFunctions


def pytest_addoption(parser):
    """Регистрация кастомных опций командной строки"""
    parser.addoption(
        "--custom-recreate-db",
        action="store_true",
        default=False,
        help="Recreate test database"
    )
    parser.addoption(
        "--custom-fill-db",
        action="store_true",
        default=False,
        help="Fill database with test data"
    )


def pytest_configure(config):
    """Обработка кастомных опций"""
    if config.getoption("--custom-recreate-db"):
        print("\nCustom database recreation triggered")
        os.environ['DJANGO_KEEP_DB'] = '0'

    if config.getoption("--custom-fill-db"):
        from django.core.management import call_command
        print("\nCustom database filling triggered")
        call_command('start_fill_db')

def create_permissions():
    functions_dict_data = []
    for i, role in enumerate(RolesFunctions):
        functions_dict_data.append(FunctionsDict(code=role.value, version=str(i + 1)))
    for i, role in enumerate(RolesFunctionsViewSet):
        functions_dict_data.append(FunctionsDict(code=role.value, version=str((i + 1) * (-1))))
    FunctionsDict.objects.bulk_create(functions_dict_data)
    RolesDict.objects.create(name="Пользователь", code='1')
    role = RolesDict.objects.create(name="Супер админ", code='2')
    role_functions_data = []
    for function_code in FunctionsDict.objects.all():
        role_functions_data.append(RoleFunctions(
            role=role,
            function_code=function_code
        ))
    RoleFunctions.objects.bulk_create(role_functions_data)

# @pytest.fixture(scope='session')
# def django_db_setup():
#     """Переопределение стандартной фикстуры для контроля создания БД"""
#     from django.conf import settings
#     settings.DATABASES['default']['NAME'] = 'test_' + settings.DATABASES['default']['NAME']


@pytest.fixture
def test_user():
    return Users.objects.create_user(
        username='testuser',
        password='testpass123',
        firstname='Test',
        lastname='User'
    )

@pytest.fixture
def admin_user():
    # return Users.objects.create_superuser(
    return Users.objects.create_user(
        username='admin',
        password='adminpass',
        firstname='Admin',
        lastname='User'
    )

@pytest.fixture
def authenticated_user(client, test_user):
    client.force_login(test_user)
    return test_user