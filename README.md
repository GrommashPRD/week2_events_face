# Events-face.

## Начало работы:
### Для запуска на локальном ПК:
1. `pip install uv`
2. `uv sync`
3. `source .venv/bin/activate`  # для Linux/MacOS\
`.venv\Scripts\activate  `   # для Windows

### Для запуска с использованием Docker:
1. `make start` - Запустить.
2. `make stop` - Остановить.

## Примеры использования.
1. Создание нового пользователя.
```
curl --location --request POST 'http://127.0.0.1:8000/api/auth/register/' \
--header 'Content-Type: application/json' \
--data '{
    "username": "someusername",
    "password": "somepassword59"
}'
```
2. Вход в систему.
```
curl --location --request POST 'http://127.0.0.1:8000/api/auth/login/' \
--header 'Content-Type: application/json' \
--data '{
    "username": "someusername",
    "password": "somepassword59"
}'
```
3. Получить список всех Events.
```
curl --location --request GET 'http://127.0.0.1:8000/api/events/' \
--header 'Authorization: Bearer <YOUR ACCESS TOKEN> \
--data ''
```
4. Получить Access Token по Refresh Token.
```
curl --location --request POST 'http://127.0.0.1:8000/api/auth/token/refresh/' \
--header 'Content-Type: application/json' \
--data '{
    "refresh": "<YOUR REFRESH TOKEN>"
}'
```
5. Выход из системы.
```
curl --location --request POST 'http://127.0.0.1:8000/api/auth/logout/' \
--header 'Authorization: Bearer <YOUR TOKEN>' \
--data ''
```

## Система синхронизации Events.
1. `python manage.py events_sync --all` - Синхронизация всех ивентов. (Первоначальная синхронизация)
2. `python manage.py events_sync --date YY-MM-DD` - Синхронизация только тех ивентов, \
у которых дата проведения равна указанной.
3. `python manage.py events_sync` - Синхронизация по дате изменения последнего синхронизованного ивента.