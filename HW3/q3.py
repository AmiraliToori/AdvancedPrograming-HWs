def interchange(str1):
    i = 0
    j = 3
    flag =  True
    temp = []
    ls1 = list(str1)
    ls2 = list(str1)
    while(flag):
        
        if(ls1[i] == 'a' and ls1[j] == 'b') or (ls1[i] == 'b' and ls1[j] == 'a'):
            
            if ls1[i] == 'a' and ls1[j] == 'b':
                ls2[i] = 'b'
                ls2[j] = 'a'
            else:
                ls2[i] = 'a'
                ls2[j] = 'b'
            
        i += 1
        j += 1
        if j == len(str1):
            flag = False

    
    str1 = ''.join(ls2)
                
    return str1

str1 = input("Please enter your string: ")

print(interchange(str1))