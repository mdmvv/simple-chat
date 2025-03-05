# Simple Chat: AI Conversational Playground

## Overview
Simple Chat is a versatile Streamlit application that demonstrates integration with multiple AI language models, serving as a personal playground for AI technologies.

## Features
- Multi-LLM Support
  - OpenAI GPT Models
  - Google Gemini
  - Anthropic Claude
- Streaming chat responses
- Configurable chat settings
- Chat history logging

## Requirements
- Python 3.8+
- Streamlit
- API Keys for:
  - OpenAI
  - Google AI
  - Anthropic

## Installation
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create `.env` file with API keys
4. Run the application: `python run.py`

## Configuration
Copy `.env.example` to `.env` and fill in your API keys:
```
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_key
ANTHROPIC_API_KEY=your_anthropic_key
```

## Usage
- Select AI model in `app.py`
- Customize model parameters
- Start chatting!

## Technologies
- Streamlit
- OpenAI API
- Google Generative AI
- Anthropic Claude API
