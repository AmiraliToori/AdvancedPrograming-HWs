# q1
# from icecream import ic


flag = True
while flag:
    try:
        length = int(
            input("Enter the desire size that you want for the list of the numbers: "))
    except:
        print("Please enter a NUMBER!")
    else:
        flag = False

lst = []

print("Please enter the desire number that you want to enter.")
for _ in range(0, length):
    number = int(input())
    lst.append(number)


def recursiveSum(user_list):
    length = len(user_list)

    if length == 0:
        return 0

    return recursiveSum(user_list[:-1]) + user_list[-1]


print(f"The sum of elements is :{recursiveSum(lst)}")
