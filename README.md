# Books App
Это веб-приложение о книгах, созданное с помощью FastAPI, которое предоставляет данные о книгах, авторах и isbn. Приложение интегрированное с помощью Google Books API 

## Особенности 
- Просмотр по названию книг
- Просмотр по названию автора
- Совместный поиск: автор + название книги
- Просмотр с помощью ISBN

## Используемые технологии
- **FastAPI** - Веб-фреймворк для создания API.
- **httpx** - Для выполнения асинхронных HTTP-запросов к Google Books API
- **pydantic** - Для валидации данных
- **Google Books API** - Предоставляет данные о книгах 
- **Alembic** - Для миграций
- 
## Requirements
- **Install `uv`**
```bash
   pip install uv
```
    uv venv
    source .venv/bin/activate  # Linux/macOS
    # OR
    .venv\\Scripts\\activate  # Windows
```
uv pip install -e .
```

## Установка
Перед запуском приложения вам необходимо создать файл ".env` в корневом каталоге проекта. Этот файл будет содержать ваш личный API-ключ для доступа к данным о книгах.

```python
API_KEY = 'your_api_key_here'
```

Замените **your_api_key_here** на ваш фактический API-ключ из https://console.developers.google.com