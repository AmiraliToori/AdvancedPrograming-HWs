# 9.

# def adjecency(user_list):
#       count = 0
#       i = 0
#       j = 1
#       while(j < len(user_list)):
#             if (user_list[i] == user_list[j]):
#                   count += 1
#                   if (count != 1):
#                         return False
#             if(j == len(user_list) - 1 and count == 1):
#                   return True
#             i += 1
#             j += 1

# list_size = int(input("Please enter the desire size of the list: "))
# user_list = [int(input(">>>")) for _ in range(list_size)]

# print(adjecency(user_list))


def adjecency(user_list):
    i = 1
    count2 = 0
    count4 = 0
    while (i < len(user_list)):
        if (user_list[i - 1] == 2 and user_list[i] == 2):
            count2 += 1
        elif (user_list[i - 1] == 4 and user_list[i] == 4):
            count4 += 1
        i += 1

    if (count2 >= 1 and count4 >= 1):
        return False
    elif (count2 != 0 or count4 != 0):
        return True
    else:
        return False

    list_size = int(input("Please enter the desire size of the list: "))
    user_list = [int(input(">>>")) for _ in range(list_size)]

print(adjecency(user_list))
