
import re

user_input = input("Please enter a string:")

alpha_pattern = re.compile(r"[a-zA-Z\s]")
ip_pattern = re.compile(r"[0-9]{1,3}[\.]{1}")


if not alpha_pattern.findall(user_input) and ip_pattern.findall(user_input):
    
    ip_lst = user_input.split('.')
    
    if len(ip_lst) == 4:
        
        if [number for number in ip_lst if int(number) > 255 or int(number) < 0]:
            print("The entered IP is INVALID!")
        else:
            print(f"{user_input} is VALID!")
            
    else:
        print("The entered IP is INVALID!")
        
else:
    print("The input is not even IP.")