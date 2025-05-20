from chat.chat_interface import run_chat
from agent.planner import generate_debt_plan

if __name__ == "__main__":
    print("👋 Welcome to NaijaFinance AI!")
    print("Type 'chat' to speak with the assistant or 'plan' for a debt strategy:")

    choice = input(">> ").strip().lower()

    if choice == 'chat':
        run_chat()
    elif choice == 'plan':
        amount = float(input("Enter total debt amount (₦): "))
        income = float(input("Enter monthly income (₦): "))
        result = generate_debt_plan(amount, income)
        print("\n📊 Debt Plan:")
        print(result)
    else:
        print("Invalid choice. Please type 'chat' or 'plan'.")
