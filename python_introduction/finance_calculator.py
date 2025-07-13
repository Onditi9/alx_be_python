# Personal Finance Calculator

#User Input for Financial Details
monthly_income = float(input("Enter your monthly income: "))
print()

monthly_expenses = float(input("Enter your total monthly expenses: "))
print()

#Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Projected Annual Savings @ 5% rate 
projected_savings = monthly_savings* 12 + (monthly_savings * 12 * 0.05)

#Display result
print(f"Your monthly savings are: KES{monthly_savings}")
print()
print(f"Projected savings after one year, with interest, is: KES{projected_savings}")