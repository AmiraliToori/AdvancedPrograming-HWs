
from math import ceil

from icecream import ic # type: ignore
flag = True
while flag:
    try:
        length = int(input("Please enter a number for length of the list: "))
    except:
        print("Please enter a NUMBER.")
    else:
        if length > 0:
            flag = False
        else:
            print("Please enter a number greater than 0.")


print("Please enter the keys: ")
keys = []
for _ in range(length):
    keys.append(input())

print("Please enter the values: ")
values = []
for _ in range(length):
    values.append(int(input()))
    

dictionary = dict(zip(keys, values))
length = len(dictionary)


def histogram(dictionary, sorted_key):
    for key in sorted_key:
        if dictionary[key] > 0:
            print(f"{key}:", end = '')
            star_number = ceil(dictionary[key] / 5)
            for _ in range(star_number):
                print("*", end = '')
            print("")

sorted_key = sorted(keys)
histogram(dictionary, sorted_key)