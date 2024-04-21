# def maxSameSubstring(s1, s2):
    
#     ls1 = list(s1)
#     ls2 = list(s2)
    
#     if len(s2) < len(s1):
#         ls1 = list(s2)
#         ls2 = list(s1)
        
#     temp = []
#     max_count = 0
    
#     for i in range(len(ls1)):
#         for j in range(len(ls2)):
            
#             if ls1[i] == ls2[j]:
#                 temp.append(ls1[i])
#                 count = len(temp)
#                 i += 1
                
#                 if i < len(ls1) - 1   and   j < len(s2) - 1:
#                     if ls1[i + 1] != ls2[j + 1]:
#                         if count > max_count:
#                             max_count = count
#                             count = 0
#                         temp = []
#                 else:
#                     if ls1[i] == ls2[j]:
#                         if count > max_count:
#                             max_count = count
#                             count = 0
#                         temp = []
    
#     return max_count
            


# str1 = input("Please enter your string number one: ")
# str2 = input("Please enter your string number two: ")

# print(maxSameSubstring(str1, str2))

######################################################################

def subString(str):
    sub_str = []
    for i in range(len(str)):
        for j in range(i + 1, len(str) + 1):
            if str[i:j] not in sub_str:
                sub_str.append(str[i:j])
    return sub_str


str1 = input("Please enter the string number 1: ")
str2 = input("Please enter the string number 2: ")



max_sub = 0
for i, sub1 in enumerate(subString(str1)):
    for j, sub2 in enumerate(subString(str2)):
        if sub1 == sub2:
            if len(sub1) > max_sub:
                max_sub = len(sub1)


print(f"The length of the same substring for \"{str1}\" and \"{str2}\" is: {max_sub}")




