# 10. mountain , index: time a[0] = 5   5: meter in mountain, write a function that calculate the maximum
# hour that mountainer ascend.

def mountain(height):
    max_list = []
    max_temp = 0
    time = 1
    while (time < len(height)):
        if (height[time - 1] < height[time]):
            max_temp += 1
        else:
            max_list.append(max_temp)
            max_temp = 0

        if (time == len(height) - 1):
            max_list.append(max_temp)

        time += 1
    return max(max_list)


    list_size = int(input("Please enter the desire size of the list: "))
    user_list = [int(input(">>>")) for _ in range(list_size)]

print(mountain(user_list))
