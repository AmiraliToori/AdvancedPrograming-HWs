import re

user_input = input("Please enter your string:")

user_input = user_input.split()

pattern = re.compile(r"^([a-zA-Z]{2}).*([a-zA-Z]{2})$")

results = [pattern.findall(value) for value in user_input]


for index ,tuple in enumerate(results):
    
    temp = tuple[0][1]
    
    if tuple[0][0] == temp[::-1]:
        print(user_input[index])