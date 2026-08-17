import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# For Streamlit Cloud
if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        api_key = None

if not api_key:
    st.error("GEMINI_API_KEY not found. Please check Streamlit Secrets.")
    st.stop()
# Page configuration
st.set_page_config(
    page_title="NutriBuddy - AI Nutrition Coach",
    page_icon="🥗",
    layout="centered"
)

# Title
st.title("🥗 NutriBuddy")
st.subheader("Your AI Nutrition Coach")

st.write(
    "Ask me about healthy eating, balanced meals, hydration, "
    "healthy snacks, and sustainable eating habits."
)

# Check API key
if not api_key:
    st.error("GEMINI_API_KEY not found. Please check your .env file.")
    st.stop()

# Create Gemini client
client = genai.Client(api_key=api_key)

# Nutrition Coach persona
SYSTEM_PROMPT = """
You are NutriBuddy, a friendly and supportive AI Nutrition Coach.

Your goal is to help users build healthy and sustainable eating habits.

Guidelines:
- Be friendly, encouraging, and non-judgmental.
- Give practical and simple nutrition advice.
- Encourage balanced meals, fruits, vegetables, whole grains,
  protein, healthy fats, and hydration.
- Avoid extreme diets and unsafe weight-loss advice.
- Do not diagnose medical conditions.
- For serious medical concerns, recommend consulting
  a qualified healthcare professional.
- Keep responses clear and easy to understand.
"""

# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_message = st.chat_input("Ask NutriBuddy a nutrition question...")

if user_message:

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_message)

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    # Build conversation history
    conversation = SYSTEM_PROMPT + "\n\nConversation history:\n"

    for message in st.session_state.messages:
        conversation += (
            f"{message['role']}: {message['content']}\n"
        )

    try:

        # Generate response
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=conversation
        )

        assistant_message = response.text

        # Display response
        with st.chat_message("assistant"):
            st.markdown(assistant_message)

        # Save assistant response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": assistant_message
            }
        )

    except Exception as e:
        st.error(f"Error: {e}")

# Clear conversation button
if st.button("🗑️ Clear Conversation"):
    st.session_state.messages = []
    st.rerun()