
def checkValid(str):
    
    if len(str) == 0:
        print("You didn't enter something.")
        return False
    
    if not str[0].isalpha():
        print("The first character of the email cannot be number or a special character.")
        return False
    
    
    if str.count('@') == 1:
        at_sign = str.find('@')
    else:
        return False
    
    if str.count('.') == 1:
        dot_sign = str.find('.')
    else:
        return False
    
    if dot_sign - at_sign == 1:
        return False
    
    
    if at_sign > dot_sign:
        print("The dot sign must be after the \'@\'character.")
        return False
    
    check = str.rsplit('.', 1)
    
    if not check[1].islower():
        print("the domain must be lower case!")
        return False
    
    if len(check[1]) > 3:
        print("the length of the domain must be equal or lower than 3.")
        return False
    
    return True
        


flag = True
while(flag):
    email = input("Please enter your email: ")
    
    if checkValid(email):
        print("The entered email is valid.")
        flag = False
    else:
        print("Please try again.")