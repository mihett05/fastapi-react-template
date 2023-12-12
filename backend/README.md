# backend

## Модули

Каждый модуль представляет из себя папку вида:

- module/
  - router.py - роутер для fastapi, подключается в api.py в корне
  - models.py - модели pydantic для запросов или ответов
  - schemas.py - схемы для mongodb
  - service.py - логика работы с бд
  - deps.py - функции для DI fastapi

В каждом модуле можно создавать любые файлы, с любой логикой

## Корень

- api.py - подключение всех роутеров из модулей
- config.py - конфиги из secrets и .env
- main.py - fastapi app, запуск uvicorn
- mongodb.py - инициализация монги со всеми схемами

(каждая схема должна импортироваться только одним способом (типа `from auth.models import User`, а не `from .models import User`, такое нельзя одновременно делать), иначе beanie не поймёт, что это тот же самый документ)

## Настройки

- secrets/
  - mongodb_user - пользователь от монги
  - mongodb_password - пароль от монги
- .env
  - SECRET - секретный ключ (для JWT)
