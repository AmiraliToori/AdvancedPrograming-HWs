
# q1
# from icecream import ic
# length = int(input("Enter the desire size that you want for the list of the numbers: "))

# lst = []

# print("Please enter the desire number that you want to enter.")
# for _ in range(0, length):
#     number = int(input())
#     lst.append(number)

# def recursiveSum(user_list):
#     length = len(user_list)

#     if length == 0:
#         return 0

#     return recursiveSum(user_list[:-1]) + user_list[-1]


# print(f"The sum of elements is :{recursiveSum(lst)}")

##########################################

# q4

#  1 / (1 + 0)  + 1 / (1 + 1) + 1 / (1 + 2) + ...
#  1 / (1 + 0)  + 1 / (1 + 1) + 1 / (1 + 2) + ... + 1 / (1 + n)

# user_input = int(input("Please enter a positive number: "))

# def recursiveSeries(n):

#     if n <= 0:
#         return 1 / (1 + n)
#     else:
#         return 1 / (1 + n) + recursiveSeries(n - 1)


# print(f"The calculation of the series until ({user_input}) is: {recursiveSeries(user_input)}")

#########################################################

# q5

# n, n - 5, n - 10, ..., 0, 10, n - 5, n

# n = 16 : 16, 11, 6, 1, -4, 1, 6, 11, 16

# user_input = int(input("Please enter a number: "))

# def positive_pattern(n):
#     if n == user_input:
#         print(n)
#         return
#     else:
#         print(n)
#         return positive_pattern(n + 5)

# def pattern(n):
#     if n <= 0:
#         positive_pattern(n)
#         return
#     else:
#         print(n)
#         return pattern(n - 5)

# pattern(user_input)

####################################################################

# user_input = int(input("Please enter a number: "))


# def pattern(n):
#     if n <= 0:
#         print(n, end = " ")
#         return

#     print(n, end = " ")
#     pattern(n - 5)
#     print(n, end = " ")

# pattern(user_input)
# print("\n")
################################################################

# q3

# isNatural = True
# while (isNatural):
#     user_input = int(input("Please enter a non negative number: "))
#     if user_input >= 0:
#         isNatural = False

# def number(num):
#     if num <= 0:
#         return 0
#     return num + number(num - 2)

# print(number(user_input))

######################################################################

# q6

# isPositive = True
# while (isPositive):
#     user_input = int(input("Please enter a number: "))
#     if isPositive > 0:
#         isPositive = False

# def binaryNumber(num):


# binaryNumber(user_input)

#####################################################################

# q2

# from icecream import ic

# valid_base = True
# while (valid_base):
#     base = int(input("Please enter a valid number for the base: "))

#     if base > 1:
#         valid_base = False
#     else:
#         print("Enter a valid number for the base: ")


# is_natural = True
# while (is_natural):
#     user_input = int(input("Please enter a non negative number: "))

#     if user_input >= 0:
#         is_natural = False
#     else:
#         print("Please enter a non negative number.")


# def convert_to_base(number, base):
#     if number == 0:
#         return ''
#     else:
#         remainder = number % base
#         return convert_to_base(number // base, base) + get_char(remainder)

# def get_char(digit):
#     if digit < 10:
#         return str(digit)
#     else:
#         return chr(ord('A') + digit - 10)

# result = convert_to_base(user_input, base)
# print("Result:", result)


#####################################################################

# q7
# from icecream import ic
# from itertools import combinations_with_replacement

# length = int(input("Please enter the desire length that you want to choose: "))

# user_input = []

# for _ in range(length):
#     char = input()
#     user_input.append(char)

# def createKey(string, length):

#     comb = combinations_with_replacement(string, length)
#     comb = list(comb)
#     return comb


# user_input = list(user_input)

# for _ in range(length):
#     lists = createKey(user_input, length)

#     for index in range(len(lists)):
#         print(''.join(lists[index]), end = ' , ')

#     length -= 1


####################################################

# from icecream import ic
# from itertools import combinations_with_replacement

# length = int(input("Please enter the desire length that you want to choose: "))

# user_input = []

# for _ in range(length):
#     char = input()
#     user_input.append(char)

# user_input = list(user_input)

# def createKey(string, length):

#     if length == 0:
#         return ''

#     comb = combinations_with_replacement(string, length)
#     comb = list(comb)

#     for index in range(len(comb)):
#         print(''.join(comb[index]), end = ' , ')

#     return createKey(string, length - 1)


# print(createKey(user_input, length))

# lists = createKey(user_input, length)


####################################################
