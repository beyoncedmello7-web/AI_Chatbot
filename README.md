# 🥗 NutriBuddy - AI Nutrition Coach

NutriBuddy is a CLI-based AI Nutrition Coach built using Python and
the Gemini Large Language Model API.

The chatbot provides friendly and practical guidance to help users
develop healthy and sustainable eating habits.

## Features

- CLI-based interactive chatbot
- Powered by Google's Gemini LLM
- Dedicated Nutrition Coach persona
- Maintains conversation context
- Allows continuous interaction
- Secure API key management using environment variables
- Simple and beginner-friendly Python implementation

## Technologies Used

- Python
- Google Gemini API
- google-genai
- python-dotenv

## Project Structure

```text
nutrition-coach/
│
├── chatbot.py
├── .env
├── .gitignore
└── README.md
## Streamlit Web Interface

NutriBuddy also includes a basic Streamlit-based user interface.

To run the web application:

```bash
streamlit run app.py