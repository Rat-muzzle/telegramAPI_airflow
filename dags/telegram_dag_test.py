# dags/my_telegram_dag.py
from airflow import DAG
from plugins.operators.telegram_operator import TelegramOperator
from airflow.operators.python import PythonOperator
from datetime import datetime



def task_success_handler(context):
    success_message = f"""
    <b>✅ DAG Success Notification</b>
    <b>DAG:</b> {context['dag'].dag_id}
    <b>Task:</b> {context['task'].task_id}
    <b>Execution Time:</b> {context['execution_date']}
    """
    TelegramOperator(
        task_id="send_success",
        message=success_message
    ).execute(context)


def task_failure_handler(context):
    error_message = f"""
    <b>❌ DAG Failure Alert</b>
    <b>DAG:</b> {context['dag'].dag_id}
    <b>Task:</b> {context['task'].task_id}
    <b>Error:</b> {context['exception']}
    <b>Log:</b> <a href="{context.get('task_instance').log_url}">View Logs</a>
    """
    TelegramOperator(
        task_id="send_failure",
        message=error_message
    ).execute(context)


default_args = {
    "owner": "data_team",
    "on_failure_callback": task_failure_handler,
    "on_success_callback": task_success_handler,
    "retries": 2
}

with DAG(
        "data_processing_pipeline",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=datetime(2023, 1, 1),
        catchup=False,
) as dag:
    process_data = PythonOperator(
        task_id="process_data",
        python_callable=lambda: print("Processing data..."),
    )

    send_report = TelegramOperator(
        task_id="send_daily_report",
        message="""
        <b>📊 Daily Data Report</b>
        <b>Date:</b> {{ ds }}
        <b>Processed:</b> {{ ti.xcom_pull(task_ids='process_data') }} records
        """,
        attachment_path="/reports/daily_report_{{ ds }}.csv"
    )

    process_data >> send_report