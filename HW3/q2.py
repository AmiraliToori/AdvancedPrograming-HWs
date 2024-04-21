# if all s1 in s2 then -1
# if all s2 in s1 then 1
# otherwise 0

def contain(s1, s2):
    for char in s1:
        if char not in s2:
            break
    else:
        return -1
    
    for char in s2:
        if char not in s1:
            break
    else:
        return 1
    
    return 0
    
    

str1 = input("Please enter the string number 1: ")
str2 = input("Please enter the string number 2: ")

print(contain(str1, str2))