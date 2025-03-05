import os


def log_chat_history(session_token: str, messages: list):
    """
    Update the chat history log with new messages.

    Args:
        session_token (str): Unique identifier for the chat session.
        messages (list): List of dictionaries representing chat messages.
    """

    os.makedirs(f"aichatkit/sessions/{session_token}", exist_ok=True)
    file_path = f"aichatkit/sessions/{session_token}/chat_history.txt"

    log = ""
    for message in messages:
        log += f"{message['actor'].capitalize()}:\n{message['text']}\n\n"

    with open(file_path, "a") as file:
        file.write(log)
