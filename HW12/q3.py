import re

user_input = input("Please enter a string:")

pattern = re.compile(r"\b[aeiouy]+[^aeiouy]*[aeiouy]+\b")

results = pattern.findall(user_input)

for value in results:
    if value:
        print(value)