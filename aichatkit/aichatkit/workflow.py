import openai
import google.generativeai as genai
import anthropic


def configure(**kwargs):
    if "openai_api_key" in kwargs:
        openai.api_key = kwargs["openai_api_key"]
    if "google_api_key" in kwargs:
        genai.configure(api_key=kwargs["google_api_key"])
    if "anthropic_api_key" in kwargs:
        anthropic.api_key = kwargs["anthropic_api_key"]
