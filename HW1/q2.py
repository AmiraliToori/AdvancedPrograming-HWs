# 2.Ingredient Adjuster
# A cookie recipe calls for the following ingredients:
# • 1.5 cups of sugar
# • 1 cup of butter
# • 2.75 cups of flour
# The recipe produces 48 cookies with this amount of the ingredients. Write a program that
# asks the user how many cookies he or she wants to make, then displays the number of cups
# of each ingredient needed for the specified number of cookies.

# while (True):
#     cookies_number = int(
#         input("Please enter the number of cookies that you want to make:"))
#     if (cookies_number < 0):
#         print("Negative number is invalid!")
#     else:
#         break

# suger_per_cookie = 1.5 / 48
# butter_per_cookie = 1 / 48
# flour_per_cookie = 2.75 / 48

# suger_needed = suger_per_cookie * cookies_number
# butter_needed = butter_per_cookie * cookies_number
# flour_needed = flour_per_cookie * cookies_number

# print(f"The Ingredient for {cookies_number:^}\n"
#       "Ingredient:\n"
#       f"{suger_needed:^.2f} cups of sugar\n"
#       f"{butter_needed:^.2f} cups of butter\n"
#       f"{flour_needed:^.2f} cups of flour"
#       )


while (True):
    try:
        cookies_number = int(
            input("Please enter the number of cookies that you want to make:"))
        if (cookies_number < 0):
            print("Negative number is invalid!")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")
    else:
        print("The execution continues")

suger_per_cookie = 1.5 / 48
butter_per_cookie = 1 / 48
flour_per_cookie = 2.75 / 48

suger_needed = suger_per_cookie * cookies_number
butter_needed = butter_per_cookie * cookies_number
flour_needed = flour_per_cookie * cookies_number

print(f"The Ingredient for {cookies_number:^}\n"
      "Ingredient:\n"
      f"{suger_needed:^.2f} cups of sugar\n"
      f"{butter_needed:^.2f} cups of butter\n"
      f"{flour_needed:^.2f} cups of flour"
      )