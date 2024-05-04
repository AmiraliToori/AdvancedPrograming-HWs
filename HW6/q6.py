

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

text_input = input("Please enter your string: ")

def get_value(dictionary, text):
    score = 0
    key_lst = dictionary.keys()
    lower_text = text.lower()
    upper_text = text.upper()
    for key in key_lst:
        count = 0
        if key in lower_text:
            count = lower_text.count(key)
        if key in upper_text:
            count = upper_text.count(key)
        ic(key)
        ic(count)
        for _ in range(count):
            score += dictionary[key]
            ic(dictionary[key])
    
    return score

print(get_value(dictionary, text_input))

