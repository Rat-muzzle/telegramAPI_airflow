from airflow.models import BaseOperator
from plugins.hooks.telegram_hook import TelegramHook
import  os

class TelegramOperator(BaseOperator):
    """
    Operator for sending messages via Telegram.

    :param telegram_conn_id: The connection ID to use for Telegram.
    :type telegram_conn_id: str
    :param chat_id: The ID of the chat where the message will be sent.
    :type chat_id: str
    :param message: The message to send.
    :type message: str
    :param args: Additional arguments for the BaseOperator
    :param kwargs: Additional keyword arguments for the BaseOperator
    """
    template_fields = ("message",)

    def __init__(self,
                 message,
                 attachment_path=None,
                 parse_mode="HTML",
                 **kwargs):
        super().__init__(**kwargs)
        self.message = message
        self.attachment_path = attachment_path
        self.parse_mode = parse_mode

    def execute(self, context):
        hook = TelegramHook()

        # Рендеринг шаблонов Airflow
        rendered_message = self.render_template(
            self.message,
            context
        )

        if self.attachment_path:
            # Рендеринг пути к файлу
            rendered_path = self.render_template(
                self.attachment_path,
                context
            )
            if not os.path.exists(rendered_path):
                self.log.error(f"File not found: {rendered_path}")
                raise FileNotFoundError(f"Report file not found: {rendered_path}")
            hook.send_document(rendered_path)
            self.log.info(f"Sent document: {rendered_path}")

        hook.send_message(
            text=rendered_message,
            parse_mode=self.parse_mode
        )
        self.log.info(f"Sent message: {rendered_message}")
