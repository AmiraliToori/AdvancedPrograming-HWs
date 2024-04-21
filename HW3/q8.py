def createRepeat(string):
    char = []
    char_repeat = []
    char_repeat_count = []
    
    for index in string:
        char.append(index)
        
        if index not in char_repeat:
            char_repeat.append(index)
    
    for index in char_repeat:
        char_repeat_count.append(char.count(index))
        
    return char_repeat, char_repeat_count


def transform(s1, s2):
    
    s1 = createRepeat(s1)
    s2 = createRepeat(s2)
    
    list1 = list(zip(s1[0], s1[1]))
    list2 = list(zip(s2[0], s2[1]))
    
    dict1 = dict(list1)
    dict2 = dict(list2)

    if dict1 == dict2:
        return True
    return False

    
        
isSame = True
while(isSame):
    str1 = input("Please enter the string number 1: ")
    str2 = input("Please enter the string number 2: ")

    str1 = str1.lower()
    str2 = str2.lower()

    ls1 = str1.split()
    ls2 = str2.split()

    str1 = ''.join(ls1)
    str2 = ''.join(ls2)
    
    if len(str1) == len(str2):
        isSame = False
    else:
        print("the count of the two entered strings must be the same, try again!")

print(f"does we can get to the same results by changing the combination of \"{str1}\" and \"{str2}\" words? {transform(str1, str2)}")