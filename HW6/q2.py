
from icecream import ic # type: ignore

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

lst = []
for _ in range(lst_length):
    lst.append((input()))
       
    
def greatest_common_prefix(lst):
    common = 0
    flag = True
    while flag:
        first_word = lst[0]
        sample = first_word[:common]
        check_lst = []
        for word in lst:
            check_lst.append(word.startswith(sample))
        if all(check_lst):
            common += 1
        else:
            flag = False
    
    return first_word[:common - 1]


print(f"The most common prefix in the list is : {greatest_common_prefix(lst)}")