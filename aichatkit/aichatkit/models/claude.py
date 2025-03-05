import anthropic


class Claude:
    def __init__(self, model: str = "claude-3-opus-20240229"):
        self.model = model
        self.client = anthropic.Anthropic()

    def stream_response(self, chat_history: list):
        messages = [
            {
                "role": "assistant" if message["actor"] == "bot" else "user",
                "content": message["text"],
            }
            for message in chat_history
        ]

        with self.client.messages.stream(
            max_tokens=1024,
            # system="Respond only in Yoda-speak.",
            messages=messages,
            model=self.model,
        ) as stream:
            for text in stream.text_stream:
                yield text
