
isNatural = True
while (isNatural):
    try:
        user_input = int(input("Please enter a positive number: "))
    except:
        print("Please enter a NUMBER!")
    else:
        if user_input >= 0:
            isNatural = False
        else:
            print("Please enter a positive number: ")


def recursiveSeries(n):

    if n <= 0:
        return 1 / (1 + n)
    else:
        return 1 / (1 + n) + recursiveSeries(n - 1)


print(
    f"The calculation of the series until ({user_input}) is: {recursiveSeries(user_input)}")
