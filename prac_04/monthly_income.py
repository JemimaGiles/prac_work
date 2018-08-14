"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""
# answers , 2 for loops,

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    monthly_income = int(input("How many months? "))

    for month in range(1, monthly_income + 1):
        income = float(input("Enter income for month{:2}: ".format(monthly_income)))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, monthly_income + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()