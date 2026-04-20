ARG PYTHON_VERSION=3.12-slim
FROM python:${PYTHON_VERSION}

# Создаем пользователя
RUN useradd -m -u 1000 appuser

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY app.py .

# Меняем владельца
RUN chown -R appuser:appuser /app

# Переключаемся на непривилегированного пользователя
USER appuser

EXPOSE 8080

CMD ["python", "app.py"]