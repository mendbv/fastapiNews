# FastAPI News
News project based on FastAPI
## Содержание

- [Начало работы](#начало-работы)
- [Установка](#установка)
- [Использование](#использование)
  
## Начало работы

Удостоверьтесь, что у вас установлен python 3 версии и все его компоненты (pip, venv)

### Требования

- Python версии 3.x
- Fastapi[standard]

### Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/mendbv/fastapiNews
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd fastapiNews
   ```
3. Создайте и активируйте виртуальное окружение (рекомендуется):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # для Linux/Mac
   venv\Scripts\activate  # для Windows
   ```
4. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
5. Создайте .env файл:
   ```ENV EXAMPLE
   DB_NAME = "name"
   DB_USER = "username"
   DB_PASSWORD = "password"
   DB_HOST = 127.0.0.1
   DB_PORT = 5432
   ```
## Использование

Пример, как использовать проект или запустить скрипты. Например:

```bash
fastapi dev main.py
```
