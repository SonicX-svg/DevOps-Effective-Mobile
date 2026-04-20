# Используем переменную из build args
ARG PYTHON_VERSION=3.12-slim
FROM python:${PYTHON_VERSION}

# Явно указываем WORKDIR
WORKDIR /app

ENV PYTHONUNBUFFERED=1

# Копируем приложение
COPY app.py .

# Запускаем приложение (порт будет из переменной окружения)
CMD python app.py
