

flag = True
while flag:
    try:
        lst_length = int(input("Please enter a number for length of the list: "))
    except:
        print("Please enter a NUMBER!")  
    else:
        if lst_length > 0:
            flag = False
        else:
            print("Please enter a number greater than 0.")

print("Please enter the elements for the list: ")
lst = []
for _ in range(lst_length):
    lst.append(int(input()))


flag = True
while flag:
    try:
        number = int(input("Please enter a number for the sum:"))
    except:
        print("Please enter a NUMBER!")  
    else:
        flag = False


def equal_pairs(lst, sum):
    equal_list = []
    for i in range(lst_length):
        for j in range(lst_length):
            if lst[i] + lst[j] == number and ([lst[i], lst[j]]) not in equal_list:
                equal_list.append([lst[i], lst[j]])
    return equal_list

print(equal_pairs(lst, number))