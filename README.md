# DevOps Test Task: Web Application with Nginx Reverse Proxy

## 📋 Описание проекта

Простое веб-приложение, развернутое с помощью Docker и Docker Compose. Приложение состоит из двух сервисов:
- **Backend** — HTTP-сервер на Python
- **Nginx** — reverse proxy, который принимает запросы от пользователя и перенаправляет их на backend

Взаимодействие между сервисами осуществляется через изолированную Docker-сеть. Пользователю доступен только Nginx (порт 80), backend скрыт внутри сети.


### Как это работает:

1. **Пользователь** отправляет HTTP-запрос на `http://localhost`
2. **Nginx** (порт 80) принимает запрос и проксирует его на backend-сервис
3. **Backend** (Python сервер на порту 8080) обрабатывает запрос и возвращает ответ
4. **Nginx** передает ответ обратно пользователю

При этом:
- Backend доступен **только внутри Docker-сети**, доступа с хоста к нему нет
- Nginx выступает как единая точка входа (reverse proxy)
- Docker-сеть изолирует сервисы друг от друга

## 🛠 Использованные технологии

| Технология | Версия | Назначение |
|-----------|--------|------------|
| Docker | 20.10+ | Контейнеризация приложений |
| Docker Compose | 2.0+ | Оркестрация многоконтейнерных приложений |
| Nginx | 1.26-alpine | Reverse proxy |
| Python | 3.12-slim | Backend сервер |
| curl | latest | Healthcheck для nginx |

## 📁 Структура проекта
```
.
├── backend/
│ ├── Dockerfile # Сборка образа Python-приложения
│ └── app.py # HTTP-сервер на Python
├── nginx/
│ ├── Dockerfile # Сборка образа Nginx
│ └── nginx.conf # Конфигурация reverse proxy
├── docker-compose.yml # Оркестрация сервисов
├── .env # Переменные окружения 
└── README.md # Документация
```

## 🚀 Запуск проекта

### Требования

- Docker (версия 20.10 или выше)
- Docker Compose (версия 2.0 или выше)
- Git (для клонирования репозитория)

### Шаг 1: Клонирование репозитория

```bash
git clone https://github.com/SonicX-svg/DevOps-Effective-Mobile.git
cd DevOps-Effective-Mobile
```

### Шаг 2: Настройка переменных окружения

```bash
APP_NAME=myapp
BACKEND_PORT=8080
NGINX_PORT=8080
NGINX_HOST_PORT=80
BACKEND_MEMORY_LIMIT=128M
NGINX_MEMORY_LIMIT=64M
PYTHON_VERSION=3.12-slim
NGINX_VERSION=1.26-alpine
```

### Шаг 3: Сборка и запуск
```bash
# Сборка образов и запуск контейнеров
docker-compose up -d

# Просмотр логов
docker-compose logs -f

# Проверка статуса контейнеров
docker-compose ps
```

### Шаг 4: Проверка
```bash
# Основной эндпоинт
curl http://localhost
# Ожидаемый ответ: Hello from Effective Mobile!

# Healthcheck nginx
curl http://localhost/nginx-health
# Ожидаемый ответ: nginx healthy

# Healthcheck backend (через nginx)
curl http://localhost/nginx-python-health
# Ожидаемый ответ: OK
```







