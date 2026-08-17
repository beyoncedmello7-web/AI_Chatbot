import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY not found.")
    exit()

# Create Gemini client
client = genai.Client(api_key=api_key)

SYSTEM_PROMPT = """
You are NutriBuddy, a friendly and supportive AI Nutrition Coach.

Your goal is to help users build healthy and sustainable eating habits.

Guidelines:
- Be friendly, encouraging, and non-judgmental.
- Give practical and simple nutrition advice.
- Encourage balanced meals, fruits, vegetables, whole grains,
  protein, healthy fats, and hydration.
- Do not recommend extreme diets or unsafe weight-loss methods.
- Do not diagnose medical conditions.
- For serious medical concerns, recommend consulting a
  qualified healthcare professional.
- Keep answers clear and easy to understand.
"""

previous_interaction_id = None


def get_response(user_message):
    global previous_interaction_id

    if previous_interaction_id:
        interaction = client.interactions.create(
            model="gemini-3.6-flash",
            previous_interaction_id=previous_interaction_id,
            input=user_message
        )
    else:
        interaction = client.interactions.create(
            model="gemini-3.6-flash",
            system_instruction=SYSTEM_PROMPT,
            input=user_message
        )

    previous_interaction_id = interaction.id

    return interaction.output_text


def main():

    print("=" * 60)
    print("🥗 Welcome to NutriBuddy - AI Nutrition Coach")
    print("=" * 60)
    print("Ask me anything about healthy eating and nutrition.")
    print("Type 'exit' or 'quit' to end the chatbot.")
    print("=" * 60)

    while True:

        user_message = input("\nYou: ").strip()

        if user_message.lower() in ["exit", "quit"]:
            print("\nNutriBuddy: Goodbye! Keep making healthy choices! 🥗")
            break

        if not user_message:
            print("NutriBuddy: Please enter a message.")
            continue

        try:
            answer = get_response(user_message)
            print("\nNutriBuddy:", answer)

        except Exception as e:
            print("\nError:", e)


if __name__ == "__main__":
    main()