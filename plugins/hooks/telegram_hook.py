from airflow.hooks.base import BaseHook
import requests, os
from dotenv import load_dotenv


class TelegramHook(BaseHook):
    def __init__(self, token=None, chat_id=None):
        """
        Initialize the TelegramHook with the given connection ID.
        :param token:
        :param chat_id:
        """
        super().__init__()
        load_dotenv()
        # self.token = token or os.getenv("TOKEN")
        # self.chat_id = chat_id or os.getenv("TELEGRAM_CHAT_ID")
        env_path = os.getenv('AIRFLOW__ENV_FILE_PATH', '.env')
        load_dotenv(env_path)

        self.token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")



    def send_message(self, text, parse_mode="HTML", disable_web_page_preview=True):
        """
        Send a message text to a Telegram chat.
        :param text:
        :param parse_mode:
        :param disable_web_page_preview:
        :return:
        """
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        load  = {
            "chat_id": self.chat_id,
            "text": text,
            "parse_mode": parse_mode,
            "disable_web_page_preview": disable_web_page_preview
        }
        response = requests.post(url, json=load)
        response.raise_for_status()
        return response.json()

    def send_document(self, document_path):
        """
        Send a message_document to a Telegram chat
        :param document_path:
        :return:
        """
        url = f"https://api.telegram.org/bot{self.token}/sendDocument"
        with open(document_path, "rb") as file:
            files = {"document": file}
            data = {"chat_id": self.chat_id}
            response = requests.post(url, files=files, data=data)
        response.raise_for_status()
        return response.json()