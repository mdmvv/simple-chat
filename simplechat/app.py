import os

from dotenv import load_dotenv
import streamlit as st

from aichatkit import configure
from aichatkit import Chat
from aichatkit.models import GPT, Gemini, Claude


def initialize_chat():
    load_dotenv()
    openai_api_key = os.environ.get("OPENAI_API_KEY", "")
    google_api_key = os.environ.get("GOOGLE_API_KEY", "")
    anthropic_api_key = os.environ.get("GOOGLE_API_KEY", "")  # TODO check

    configure(
        openai_api_key=openai_api_key,
        google_api_key=google_api_key,
        anthropic_api_key=anthropic_api_key
    )

    settings = {"log_chat_history": True}
    # llm = GPT(model="gpt-3.5-turbo")
    # llm = GPT(model="gpt-3.5-turbo", temperature=0)
    # llm = GPT(model="gpt-4-turbo")
    # llm = GPT(model="gpt-4-turbo", temperature=0)
    # llm = Claude(model="claude-3-haiku-20240307")
    # llm = Claude(model="claude-3-sonnet-20240229")
    llm = Claude(model="claude-3-opus-20240229")
    # llm = Claude(model="claude-3-5-sonnet-20240620")
    # llm = Gemini(model="gemini-1.0-pro-latest")
    # llm = Gemini(model="gemini-pro")

    # gemini-1.0-pro
    # gemini-1.0-pro-001
    # gemini-1.0-pro-latest
    # gemini-1.0-pro-vision-latest
    # gemini-pro
    # gemini-pro-vision

    chat = Chat(settings=settings, llm=llm)

    return chat


def main():
    st.title("Simple chat")

    if "chat" not in st.session_state:
        st.session_state.chat = initialize_chat()

    for message in st.session_state.chat.history:
        with st.chat_message("assistant" if message["actor"] == "bot" else "user"):
            st.markdown(message["text"])

    if message := st.chat_input("Write a message..."):
        with st.chat_message("user"):
            st.markdown(message)
        with st.chat_message("assistant"):
            st.write_stream(st.session_state.chat.handle(message))


if __name__ == "__main__":
    main()
