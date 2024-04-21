# 1. Tip, Tax, and Total
# Write a program that calculates the total amount of a meal purchased at a restaurant. The
# program should ask the user to enter the charge for the food, then calculate the amounts
# of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.


# while (True):
#     charge = float(input("Enter the charge of the meal: "))
#     if (charge <= 0):
#         print("The input must be positive.")
#     else:
#         break

# tip_charge = charge * (18 / 100)
# tax_charge = charge * (7 / 100)
# total = charge + tip_charge + tax_charge
# print(f"Tip:{tip_charge:.2f}\n"
#       f"Tax:{tax_charge:.2f}\n"
#       f"Total:{total:.2f}")


while (True):
    try:
        charge = float(input("Enter the charge of the meal: "))
        if (charge <= 0):
            print("The input must be positive.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")
    else:
        print("The execution continues.")

tip_charge = charge * (18 / 100)
tax_charge = charge * (7 / 100)
total = charge + tip_charge + tax_charge
print(f"Tip:{tip_charge:.2f}\n"
      f"Tax:{tax_charge:.2f}\n"
      f"Total:{total:.2f}")
      