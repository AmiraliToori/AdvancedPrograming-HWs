# 5. Magic Dates
# The date June 10, 1960, is special because when it is written in the following format, the
# month times the day equals the year:
# 6/10/60
# Design a program that asks the user to enter a month (in numeric form), a day, and a twodigit year. The program should then determine whether the month times the day equals the
# year. If so, it should display a message saying the date is magic. Otherwise, it should display
# a message saying the date is not magic.

while (True):
    try:
        day = int(input("Please enter the day:"))
        month = int(input("Please enter the month(in numeric form): "))
        if (day <= 0 or day > 30 or month > 12 or month <= 0):
            print("Please enter day or month in a valid range, try again.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")
    else:
        print("The execution continues.")


while (True):
    try:
        year = int(input("Please enter the year in 2 digits form:"))
        temp = year
        count = 0
        while (temp != 0):
            temp = temp // 10
            count += 1
            if ((temp == 0 and count > 2) or (temp == 0 and count < 2)):
                print("notice that the year number must be 2 digit.")
        if (count == 2):
            break
    except ValueError:
        print("Please enter a valid number.")
    else:
        print("The execution continues.")

if (year == day * month):
    print("the date is magic.")
else:
    print("the date is not magic")
