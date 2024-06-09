
import re

user_input = input("Please enter the string: ")

pattern = re.compile(r"[0-9]{10}")

answers = pattern.findall(user_input)

if answers:
    print(f"The {user_input} is a valid ID.")
else:
    print(f"The {user_input} is not valid.")