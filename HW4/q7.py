# from icecream import ic
from itertools import combinations_with_replacement

is_valid = True
while is_valid:
    try:
        length = int(
            input("Please enter the desire length that you want to choose: "))
    except:
        print("Please enter a NUMBER!")
    else:
        if length > 0:
            is_valid = False
        else:
            print("Please enter a positive number for the size of the list!")

user_input = []

for _ in range(length):
    char = input()
    user_input.append(char)

user_input = list(user_input)


def createKey(string, length):

    if length == 0:
        return

    comb = combinations_with_replacement(string, length)
    comb = list(comb)

    for index in range(len(comb)):
        print(''.join(comb[index]), end=' , ')

    return createKey(string, length - 1)


createKey(user_input, length)
