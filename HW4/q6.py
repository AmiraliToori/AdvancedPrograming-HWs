def generateBinaryNumbers(n, current_number='', ones=0, zeroes=0):

    if len(current_number) == n:

        if ones >= zeroes:
            print(current_number, end=' ')
        return

    generateBinaryNumbers(n, current_number + '1', ones + 1, zeroes)
    if ones > zeroes:
        generateBinaryNumbers(n, current_number + '0', ones, zeroes + 1)


is_valid = True
while is_valid:
    try:
        user_input = int(input("Enter the value of n: "))
    except:
        print("Please enter a NUMBER!")
    else:
        if user_input > 0:
            is_valid = False
        else:
            print("The entered number is not valid!")

generateBinaryNumbers(user_input, '1', 1, 0)
