FROM apache/airflow:2.7.3

# Установка netcat для проверки доступности БД
USER root
RUN apt-get update && \
    apt-get install -y netcat && \
    apt-get clean

# Добавляем путь к плагинам в PYTHONPATH
ENV PYTHONPATH "${PYTHONPATH}:/opt/airflow/plugins"


# Копируем entrypoint-скрипт
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Возвращаемся к пользователю airflow
USER airflow

# Устанавливаем entrypoint
ENTRYPOINT ["/entrypoint.sh"]