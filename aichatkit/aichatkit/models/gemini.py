from google.generativeai import GenerativeModel


class Gemini:
    def __init__(self, model: str = "gemini-pro"):
        self.model = GenerativeModel(model_name=model)

    def stream_response(self, chat_history: list):
        contents = [
            {
                "role": "model" if message["actor"] == "bot" else "user",
                "parts": [message["text"]],
            }
            for message in chat_history
        ]

        response = self.model.generate_content(contents=contents, stream=True)

        for chunk in response:
            yield chunk.text
