import pytest
from django.urls import reverse_lazy


@pytest.mark.django_db
def test_home_url(client, test_user):
    """Тест доступности главной страницы"""
    client.force_login(test_user)
    response = client.get(reverse_lazy('home'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_home_without_login_url(client, test_user):
    """Тест не доступности главной страницы без авторизации"""
    response = client.get(reverse_lazy('home'))
    assert response.status_code == 302