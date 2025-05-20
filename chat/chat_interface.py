import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

chat_history = []

def run_chat():
    print("\n🧠 NaijaFinance AI is listening... (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        chat_history.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a financial assistant focused on debt repayment and Nigerian money tools."},
                *chat_history
            ]
        )

        reply = response.choices[0].message.content.strip()
        print("AI:", reply)
        chat_history.append({"role": "assistant", "content": reply})
