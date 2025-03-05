from openai import OpenAI


class GPT:
    def __init__(self, model: str = "gpt-3.5-turbo-0125", temperature: float = 1):
        self.model = model
        self.temperature = temperature
        self.client = OpenAI()

    def stream_response(self, chat_history: list):
        messages = [
            {
                "role": "assistant" if message["actor"] == "bot" else "user",
                "content": message["text"],
            }
            for message in chat_history
        ]

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            messages=messages,
            stream=True,
            timeout=30.0,
        )

        for chunk in response:
            content = chunk.choices[0].delta.content
            if content:
                yield content
