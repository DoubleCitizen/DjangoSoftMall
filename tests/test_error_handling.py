import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_404_handler(client):
    """Тест обработки несуществующих страниц"""
    response = client.get('/non-existent-page/')
    assert response.status_code == 404

@pytest.mark.django_db
def test_invalid_form_submission(client):
    """Тест обработки невалидных данных формы"""
    response = client.post(reverse('register'), {
        'username': 'user',
        'password': '123',
        'password_confirm': '456'
    })
    assert 'Пароли не совпадают' in response.content.decode()