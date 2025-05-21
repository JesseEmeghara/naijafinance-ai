from flask import Flask, request, jsonify
from chat.chat_interface import run_chat  # You’ll need to adapt this for web
from agent.planner import generate_debt_plan
from utils.db import save_user_profile, get_user_id_by_email, add_spending

app = Flask(__name__)

@app.route('/')
def home():
    return "👋 NaijaFinance AI is live!"

@app.route('/create-profile', methods=['POST'])
def create_profile():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    income_range = data.get("income_range")
    goal = data.get("goal")

    if not all([name, email, income_range, goal]):
        return jsonify({"error": "Missing fields"}), 400

    save_user_profile(name, email, income_range, goal)
    return jsonify({"message": "✅ Profile saved!", "email": email})

@app.route('/add-spending', methods=['POST'])
def add_user_spending():
    data = request.json
    email = data.get("email")
    category = data.get("category")
    amount = data.get("amount")
    note = data.get("note", "")

    if not all([email, category, amount]):
        return jsonify({"error": "Missing required fields"}), 400

    user_id = get_user_id_by_email(email)
    add_spending(user_id, category, amount, note)
    return jsonify({"message": "✅ Spending recorded!"})

@app.route('/debt-plan', methods=['POST'])
def get_debt_plan():
    data = request.json
    email = data.get("email")
    total_debt = data.get("debt")
    income = data.get("income")

    if not all([email, total_debt, income]):
        return jsonify({"error": "Missing fields"}), 400

    user_id = get_user_id_by_email(email)
    plan = generate_debt_plan(user_id, total_debt, income)
    return jsonify({"debt_plan": plan})

# Optional: Chat endpoint (must adapt `run_chat()` to return text, not print)
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    email = data.get("email")
    user_id = get_user_id_by_email(email)
    
    message = data.get("message", "")
    response = run_chat(user_id, message)  # You must adapt `run_chat()` to accept and return values
    return jsonify({"response": response})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
