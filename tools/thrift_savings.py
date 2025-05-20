def calculate_thrift_plan(goal_amount, duration_days):
    daily_contribution = goal_amount / duration_days
    return round(daily_contribution, 2)

if __name__ == "__main__":
    goal = float(input("Savings goal (₦): "))
    days = int(input("Duration (days): "))
    daily = calculate_thrift_plan(goal, days)
    print(f"\n💰 You should save ₦{daily:,.2f} daily to reach ₦{goal:,.2f} in {days} days.")
