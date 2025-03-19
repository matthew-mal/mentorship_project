## Развертывание

### 1. Клонирование репозитория
```bash
git clone <repository-url>
cd mentorship
```

### 2. Установка виртуального окружения
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Установка зависимостей
```bash
pip install django djangorestframework djangorestframework-simplejwt
```

### 4. Настройка базы данных
Примените миграции для создания базы данных (по умолчанию используется SQLite):
```bash
python manage.py migrate
```

### 5. Запуск сервера
```bash
python manage.py runserver
```

## API

### Регистрация
- **URL**: `POST /api/registration/`
- **Тело запроса**:
  ```json
  {
      "username": "user1",
      "password": "password123",
      "phone": "123456789",
      "email": "user@example.com"
  }
  ```
     ```bash
   curl -X POST http://127.0.0.1:8000/api/registration/ \
   -H "Content-Type: application/json" \
   -d '{"username": "user1", "password": "pass123", "phone": "123456789", "email": "user1@example.com"}'
   ```
- **Ответ**:
  - `201 Created`: Успешная регистрация.
  - `400 Bad Request`: Ошибка валидации.

### Логин
- **URL**: `POST /api/login/`
- **Тело запроса**:
  ```json
  {
      "username": "user1",
      "password": "password123"
  }
  ```
     ```bash
   curl -X POST http://127.0.0.1:8000/api/login/ \
   -H "Content-Type: application/json" \
   -d '{"username": "user1", "password": "password123"}'
   ```
- **Ответ**:
  - `200 OK`:
    ```json
    {
        "refresh": "<refresh_token>",
        "access": "<access_token>"
    }
    ```
  - `401 Unauthorized`: Неверные учетные данные.

### Обновление токена
- **URL**: `POST /api/token/refresh/`
- **Тело запроса**:
  ```json
  {
      "refresh": "<refresh_token>"
  }
  ```
- **Ответ**:
  - `200 OK`:
    ```json
    {
        "access": "<new_access_token>"
    }
    ```

### Список пользователей
- **URL**: `GET /api/users/`
- **Заголовок**: `Authorization: Bearer <access_token>`
```bash
   curl -X GET http://127.0.0.1:8000/api/users/ \
   -H "Authorization: Bearer <access_token>"
   ```
- **Ответ**:
  ```json
  [
      {
          "id": 1,
          "username": "user1",
          "is_mentor": false,
          "phone": "123456789",
          "email": "user1@example.com",
          "mentees": [],
          "mentor": "mentor1"
      },
      {
          "id": 2,
          "username": "mentor1",
          "is_mentor": true,
          "phone": "987654321",
          "email": "mentor1@example.com",
          "mentees": ["user1"],
          "mentor": null
      }
  ]
  ```

### Детали пользователя и обновление
- **URL**: `GET /api/users/<id>/` или `PATCH /api/users/<id>/`
- **Заголовок**: `Authorization: Bearer <access_token>`
- **Тело запроса (для PATCH)**:
  ```json
  {
      "password": "newpassword"
  }
  ```
- **Ответ**:
  - `200 OK`: Успешное получение или обновление.
  - `403 Forbidden`: Попытка обновить чужой профиль.

### Логаут
- **URL**: `POST /api/logout/`
- **Заголовок**: `Authorization: Bearer <access_token>`
- **Ответ**:
  - `205 Reset Content`:
    ```json
    {
        "message": "Successfully logged out"
    }
    ```
  - **Примечание**: Без черного списка токены остаются валидными до истечения срока действия. 
