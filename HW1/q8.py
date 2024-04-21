def sumDigits(n, r):
    sum_of_digit = 0
    flag = True
    for i in range(0, len(n)):

        if (n[i].isdigit()):
            digit = int(n[i])

        elif (n[i].isalpha()):
            digit = ord(n[i].upper()) - ord('A') + 10

        elif (n[i] == '.'):
            if (flag):
                i += 1
                flag = False
                continue
            else:
                raise ValueError("The entered number is invalid!")

        elif (n[0] == "-"):
            i += 1
            continue

        else:
            raise ValueError("Please enter a valid number!")

        if digit >= r:
            raise ValueError(
                "entered number cannot be equal or greater than the determined base!")

        sum_of_digit += digit

    print(sum_of_digit)
    return sum_of_digit


def convert(n, r):
    convert_list = []
    while (True):
        if (n // r == 0):
            convert_list.append(n % r)
            break
        if (n % r >= 10):
            convert_list.append(chr((n % r) + 55))
        else:
            convert_list.append(n % r)
        n = n // r
    return convert_list


number = input("Please enter your number:")
r = int(input("Please enter the desire base for your number:"))


total = sumDigits(number, r)
answer = convert(total, r)
for i in range(len(answer) - 1,  -1, -1):
    print(answer[i], end="")
print()
