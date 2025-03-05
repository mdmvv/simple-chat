import secrets

from aichatkit.models import GPT
from aichatkit.chat.data_management import log_chat_history


class Chat:
    def __init__(self, session_token: str = None, settings: dict = {}, llm=None):
        self.session_token = session_token if session_token else secrets.token_hex(16)
        self.settings = {"log_chat_history": settings.get("log_chat_history", False)}
        self.history = []
        self.llm = llm if llm else GPT()

    def handle(self, message: str = None):
        if message:
            self.__add_message({"actor": "user", "text": message})

        response_message = {"actor": "bot", "text": ""}
        for chunk in self.llm.stream_response(chat_history=self.history):
            response_message["text"] += chunk
            yield chunk

        self.__add_message(response_message)

    def __add_message(self, message: dict):
        self.history.append(message)
        if self.settings["log_chat_history"]:
            log_chat_history(session_token=self.session_token, messages=[message])
