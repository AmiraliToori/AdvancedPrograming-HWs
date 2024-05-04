

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
    lst.append(int(input()))
    

def repeat_detector(lst):
    repeat_lst = []
    for index in range(lst_length - 2):
        a = lst[index]
        b = lst[index + 1]
        c = lst[index + 2]
        if a == b == c:
            if a not in repeat_lst:
               repeat_lst.append(lst[index])
    return repeat_lst

repeat_lst = repeat_detector(lst)
print("The numbers which is in list sequentially more than 3 times are :", end = ' ')
for char in repeat_lst:
    print(char, end = ' ')
