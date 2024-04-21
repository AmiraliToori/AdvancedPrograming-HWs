# q5

# n, n - 5, n - 10, ..., 0, 10, n - 5, n

# n = 16 : 16, 11, 6, 1, -4, 1, 6, 11, 16

# user_input = int(input("Please enter a number: "))

# def positive_pattern(n):
#     if n == user_input:
#         print(n, end = ' \n')
#         return
#     else:
#         print(n, end = ' ')
#         return positive_pattern(n + 5)

# def pattern(n):
#     if n <= 0:
#         positive_pattern(n)
#         return
#     else:
#         print(n, end = ' ')
#         return pattern(n - 5)

# pattern(user_input)

#######################################################
is_valid = True
while (is_valid):
    try:
        user_input = int(input("Please enter a number: "))
    except:
        print("Please enter a NUMBER!")
    else:
        is_valid = False


def pattern(n):
    if n <= 0:
        print(n, end=" ")
        return

    print(n, end=" ")
    pattern(n - 5)
    print(n, end=" ")


pattern(user_input)
print("\n")
