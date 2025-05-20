from chat.chat_interface import run_chat
from agent.planner import generate_debt_plan
from utils.db import save_user_profile, get_user_id_by_email, add_spending


def collect_user_profile():
    print("\n📝 Let’s get to know you first:")
    name = input("Your name: ")
    email = input("Your email: ")
    income_range = input("Your income range (e.g. ₦50k - ₦200k): ")
    goal = input("What’s your financial goal? ")

    # Save to DB
    save_user_profile(name, email, income_range, goal)
    print("✅ Profile saved!\n")
    return email  # Used for further tracking


def collect_spending(user_id):
    print("\n🧾 Let's quickly add your recent spending (type 'done' to finish):")
    while True:
        category = input("Category (e.g. food, bills, transport): ")
        if category.lower() == "done":
            break
        try:
            amount = float(input("Amount spent (₦): "))
            note = input("Optional note: ")
            add_spending(user_id, category, amount, note)
            print("✅ Spending added!\n")
        except ValueError:
            print("❌ Invalid amount. Try again.")


if __name__ == "__main__":
    print("👋 Welcome to NaijaFinance AI!")
    user_email = collect_user_profile()
    user_id = get_user_id_by_email(user_email)

    collect_spending(user_id)

    print("Type 'chat' to speak with the assistant or 'plan' for a debt strategy:")
    choice = input(">> ").strip().lower()

    if choice == 'chat':
        run_chat(user_id)
    elif choice == 'plan':
        amount = float(input("Enter total debt amount (₦): "))
        income = float(input("Enter monthly income (₦): "))
        result = generate_debt_plan(user_id, amount, income)
        print("\n📊 Debt Plan:")
        print(result)
    else:
        print("❌ Invalid choice. Please type 'chat' or 'plan'.")
