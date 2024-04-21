# 4.Compound Interest
# When a bank account pays compound interest, it pays interest not only on the principal
# amount that was deposited into the account, but also on the interest that has accumulated
# over time. Suppose you want to deposit some money into a savings account, and let the
# account earn compound interest for a certain number of years. The formula for calculating
# the balance of the account after a specified number of years is:

# A = P (1 + r/n)**nt

# The terms in the formula are:
# A is the amount of money in the account after the specified number of years.
# P is the principal amount that was originally deposited into the account.
# r is the annual interest rate.
# n is the number of times per year that the interest is compounded.
# t is the specified number of years.
# Write a program that makes the calculation for you. The program should ask the user to
# input the following:
# • The amount of principal originally deposited into the account
# • The annual interest rate paid by the account
# • The number of times per year that the interest is compounded (For example, if interest
# is compounded monthly, enter 12. If interest is compounded quarterly, enter 4.)
# • The number of years the account will be left to earn interest

# Once the input data has been entered, the program should calculate and display the amount
# of money that will be in the account after the specified number of years.
# NOTE: The user should enter the interest rate as a percentage. For example, 2 percent
# would be entered as 2, not as .02. The program will then have to divide the input by
# 100 to move the decimal point to the correct position

while (True):
    principal = float(input(
        "Please enter the initial amount that you want to deposit into the account:"))  # p
    if (principal <= 0):
        print("The depoist amount is invalid! please try again.")
    else:
        break
while (True):
    annual_interest = float(
        input("Please determine the annual interest rate: "))  # r
    if (annual_interest < 0):
        print("Please enter a valid number!")
    else:
        break

annual_interest /= 100

while (True):
    type_of_interest = float(input(
        "Please determine to how the number of times per year that interest is compound: "))  # n
    if (type_of_interest <= 0):
        print("Please enter a positive number!")
    else:
        break
while (True):
    year_left = float(
        input("Enter the number of years the account will be left: "))  # t
    if (year_left < 0):
        print("Please enter a positive valid number!")
    else:
        break

print(f"you will receive {principal * ( 1 + annual_interest / type_of_interest)**(type_of_interest * year_left):.2f}"
      f" after {year_left} years"
      )
