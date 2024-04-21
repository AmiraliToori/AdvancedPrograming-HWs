isNatural = True
while (isNatural):
    try:
        user_input = int(input("Please enter a non negative number: "))
    except:
        print("Please enter a NUMBER!")
    else:
        if user_input >= 0:
            isNatural = False
        else:
            print("Please enter a non negative number: ")


def number(num):
    if num <= 0:
        return 0
    return num + number(num - 2)


print(number(user_input))
