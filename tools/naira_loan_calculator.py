def calculate_loan_interest(principal, annual_rate, months):
    monthly_rate = annual_rate / 12 / 100
    total_payment = principal * ((1 + monthly_rate) ** months)
    interest = total_payment - principal
    return {
        "principal": principal,
        "interest": round(interest, 2),
        "total_payment": round(total_payment, 2),
        "months": months
    }

if __name__ == "__main__":
    principal = float(input("Loan amount (₦): "))
    rate = float(input("Annual interest rate (%): "))
    months = int(input("Repayment period (months): "))

    result = calculate_loan_interest(principal, rate, months)
    print("\n📈 Loan Breakdown:")
    for k, v in result.items():
        print(f"{k.capitalize()}: ₦{v:,.2f}")
