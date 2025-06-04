#!/bin/bash

set -e

echo "Environment variables:"
env | grep POSTGRES
echo "Hosts:"
cat /etc/hosts

# Ожидаем доступности PostgreSQL
echo "Ожидание готовности PostgreSQL..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 1
done
echo "PostgreSQL готов!"

# Путь к файлу-флагу инициализации
INIT_FLAG="/opt/airflow/airflow-init-complete"

# Проверяем, выполнена ли уже инициализация
if [ ! -f "$INIT_FLAG" ]; then
    echo "Выполнение инициализации Airflow..."

    # Инициализация БД
    airflow db migrate

    # Создание пользователя
    airflow users create \
        --username admin \
        --firstname Admin \
        --lastname User \
        --role Admin \
        --email admin@example.com \
        --password admin

    # Создаем файл-флаг
    touch "$INIT_FLAG"
    echo "Инициализация Airflow завершена!"
else
    echo "Airflow уже инициализирован, пропускаем инициализацию."
fi

# Запуск основных компонентов Airflow
echo "Запуск Airflow..."
exec airflow standalone