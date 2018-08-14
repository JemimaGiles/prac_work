"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("PLease enter your sales: $"))

while sales > 0:
    if sales < 1000:
        bonus = str((sales * 10)/100)
    else:
        bonus = str((sales * 15)/100)

    print("your bonus is: " + bonus)
    sales = float(input("PLease enter your sales: $"))

# remove the repeated lines
