import re

user_input = input("please enter the text: ")

pattern = re.compile(r"\w*[aeiouy]{4}\w*")

print(pattern.findall(user_input))