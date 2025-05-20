import openai
import os
from utils.db import add_spending, save_recommendation  # Optional: if AI suggests something actionable

openai.api_key = os.getenv("OPENAI_API_KEY")

chat_history = []

def run_chat(user_id):
    print("\n🧠 NaijaFinance AI is listening... (type 'exit' to quit)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        chat_history.append({"role": "user", "content": user_input})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a Nigerian financial assistant who gives tailored advice based on user's spending habits and financial goals."},
                    *chat_history
                ]
            )

            reply = response.choices[0].message.content.strip()
            print("AI:", reply)

            # Save AI recommendation for the user
            save_recommendation(user_id, reply)

            chat_history.append({"role": "assistant", "content": reply})

        except Exception as e:
            print("❌ Error:", str(e))
