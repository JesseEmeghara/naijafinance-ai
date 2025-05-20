def generate_debt_plan(debt_amount, monthly_income):
    # Basic logic (to be replaced with AI or custom models)
    percent_allocated = 0.25
    repayment = monthly_income * percent_allocated
    months = int(debt_amount // repayment) + 1

    return f"""
    Total Debt: ₦{debt_amount:,.2f}
    Monthly Income: ₦{monthly_income:,.2f}
    Recommended Repayment: ₦{repayment:,.2f}/month
    Estimated Payoff Time: {months} months
    """
