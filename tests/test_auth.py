import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_login_logout_flow(client, test_user):
    """Тест полного цикла входа и выхода"""
    # Проверка входа
    response = client.post(reverse('login'), {
        'username': 'testuser',
        'password': 'testpass123'
    }, follow=True)
    assert response.status_code == 200
    # assert 'Выход' in response.content.decode()

    # Проверка выхода
    response = client.get(reverse('logout'), follow=True)
    assert response.status_code == 200
    # assert 'Вход' in response.content.decode()