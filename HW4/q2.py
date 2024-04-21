valid_base = True
while (valid_base):
    try:
        base = int(input("Please enter a valid number for the base: "))
    except:
        print("Please enter a NUMBER!")
    else:
        if base > 1:
            valid_base = False
        else:
            print("Enter a valid number for the base!")


is_natural = True
while (is_natural):
    try:
        user_input = int(input("Please enter a non negative number: "))
    except:
        print("Please enter a NUMBER!")
    else:
        if user_input >= 0:
            is_natural = False
        else:
            print("Please enter a non negative number.")


def convert_to_base(number, base):
    if number == 0:
        return ''
    else:
        remainder = number % base
        return convert_to_base(number // base, base) + get_char(remainder)


def get_char(digit):
    if digit < 10:
        return str(digit)
    else:
        return chr(ord('A') + digit - 10)


result = convert_to_base(user_input, base)
print("Result:", result)
