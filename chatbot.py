import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Start a chat session (keeps conversation history automatically)
chat = model.start_chat(history=[])

print("=" * 40)
print("   AI Chatbot  (type 'quit' to exit)")
print("=" * 40)

while True:
    user_input = input("\nYou: ").strip()

    if not user_input:
        continue

    if user_input.lower() in ["quit", "exit", "bye"]:
        print("Bot: Goodbye! Have a great day!")
        break

    try:
        response = chat.send_message(user_input)
        print(f"\nBot: {response.text}")
    except Exception as e:
        print(f"\nError: {e}")