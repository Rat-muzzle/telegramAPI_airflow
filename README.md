<h1 align="center">
  <img src="https://img.icons8.com/color/96/000000/telegram-app--v1.png" alt="Telegram" width="50"/>
  Telegram API + Apache Airflow Integration
  <img src="https://img.icons8.com/color/96/000000/airflow.png" alt="Airflow" width="50"/>
  <img src="https://img.icons8.com/color/96/000000/docker.png" alt="Docker" width="50"/>
</h1>

<p align="center">
  <b>Полностью Docker-изированное решение для интеграции Telegram и Airflow</b><br>
  Запуск в один клик с готовой конфигурацией и PostgreSQL
</p>

<p align="center">
  <a href="https://github.com/Rat-muzzle/telegramAPI_airflow/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/Rat-muzzle/telegramAPI_airflow/python-package.yml?style=flat-square" alt="Build Status">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-3.11-blue?style=flat-square&logo=python" alt="Python version">
  </a>
  <a href="https://hub.docker.com/">
    <img src="https://img.shields.io/badge/docker-compose-%230db7ed.svg?style=flat-square&logo=docker&logoColor=white" alt="Docker Compose">
  </a>
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/1627842/167292436-1d7a6d7d-9a5e-4a4a-97b7-1d0d4d8b0a7a.png" alt="Dockerized Airflow with Telegram" width="800">
</p>

## 🚀 Особенности проекта

- **Полная Docker-изация**:
  - Готовый `docker-compose.yml` с настройками Airflow
  - PostgreSQL как основное хранилище
  - Автоматическая инициализация через `entrypoint.sh`
  - Поддержка .env файла для конфигурации

- **Telegram интеграция**:
  - Отправка текстовых сообщений
  - Передача файлов и документов
  - Уведомления о статусе DAG
  - Готовые шаблоны для сообщений

- **Оптимизированный стек**:
  - Airflow 2.0+ с поддержкой Python 3.11
  - Легковесные Docker-образы
  - Автоматическое обновление зависимостей

## ⚡ Запуск за 60 секунд

### Предварительные требования
- Docker Engine 20.10+
- Docker Compose 2.0+
- Telegram Bot Token от [@BotFather](https://t.me/BotFather)
- Chat ID ([получите через](https://github.com/Rat-muzzle/get_aiogram_chat_id))
- python 3.11
### 1. Клонируйте репозиторий
```bash
git clone https://github.com/Rat-muzzle/telegramAPI_airflow.git
cd telegramAPI_airflow

### Создайте файл .env в корне проекта:
# Обязательные переменные
TELEGRAM_BOT_TOKEN=ваш_токен_бота
TELEGRAM_CHAT_ID=ваш_chat_id
