# DjangoSoftMall

Управление пользователями, компаниями и ролями с REST API на Django.

## Особенности

- 🐳 Полная Docker-интеграция (PostgreSQL + Django)
- 🔐 Система ролевых разрешений
- 📊 Модели данных:
  - Компании с реквизитами
  - Пользователи с расширенными свойствами
  - Иерархия ролей и функций
  - Группы пользователей
- 🚀 REST API (DRF) для всех сущностей
- ⚙️ Миграции через отдельный Docker-сервис
- 🔧 Настройки через переменные окружения
- 🧪 Юнит-тесты для ключевых функций

## Технологии

![Django](https://img.shields.io/badge/Django-5.1-092E20?logo=django)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-25-2496ED?logo=docker)

- 🐍 Python 3.10+
- 🟩 Django 5.1
- 🚀 Django REST Framework
- 🐘 PostgreSQL 16
- 🐳 Docker Compose
- 🧪 pytest для тестирования

[![Django](https://static.djangoproject.com/img/logos/django-logo-negative.png)](https://www.djangoproject.com/)

## Быстрый старт

### Требования

- Docker 25+
- Docker Compose 2.20+

### Установка

1. Клонировать репозиторий:
```bash
git clone https://github.com/DoubleCitizen/DjangoSoftMall.git
cd DjangoSoftMall
```
2. Создать .env_docker файл:
```
POSTGRES_DB=softmall
POSTGRES_USER=admin
POSTGRES_PASSWORD=secret
SECRET_KEY=ваш-secret-key
```

3. Запустить сервисы:
```
docker-compose up --build -d
```

Сервис будет доступен на http://localhost:8001

### API Endpoints

|Ресурс |	URL|
|---|---|
|Компании |	/api/companies/|
|Пользователи |	/api/users/|
|Роли |	/api/role_dict/|
|Группы пользователей |	/api/user_groups/|
Лицензии |	/api/license/|

Пример запроса:

```
curl -X GET http://localhost:8001/api/companies/
```

### Структура проекта

```
DjangoSoftMall/
├── api/           - REST API endpoints
├── core/          - Основная бизнес-логика
│   ├── models/    - Модели данных
│   ├── views/     - CBV для веб-интерфейса
│   └── management - Скрипты управления данными
├── softmall/      - Настройки проекта
├── tests/         - Юнит-тесты
└── docker-compose.yml - Конфигурация Docker
```

## Тестирование

Проект включает комплекс юнит-тестов, покрывающих ключевые функции:

- 🔐 Аутентификация и авторизация
- 👥 Регистрация пользователей и компаний
- 🛠️ Обработка ошибок и валидация форм
- 🔗 Проверка доступности URL-адресов

### Запуск тестов

Для запуска тестов используйте следующую команду:
```bash
pytest
```
Для запуска тестов с подробным выводом:
```bash
pytest -v
```

