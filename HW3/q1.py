def encrypt(text, key):
    
    table = [[] for _ in range(len(key))]
    
    for count, char in enumerate(text):
        index = count % len(table)
        table[index].append(char)

    for i in range(len(table)):
        if len(table[i]) < len(table[0]):
            table[i].append(' ')

    for i in range(len(table)):
        table[i].append(key[i])
    
    sorted_key = sorted(key)
    
    encrypted_text = []
    
    for char in sorted_key:
        for i in range(len(table)):
            if char == table[i][-1]:
                table[i].pop()
                encrypted_text.append(''.join(table[i]))
                table[i] = ['']
    
    print("The encrypted text is: ")
    for char in encrypted_text:
        print (''.join(char), end = '')
    
    print('\n')

def decrypt(text, key):
    
    text = list(text)
    while len(text) % len(key) != 0:
        text.append(' ')
        
    length = len(text) / len(key)
    table = [[] for _ in range(len(key))]
    
    j = 0
    for count, char in enumerate(text):
        table[j].append(char)
        if (count + 1) % length == 0:
            j += 1
    
    sorted_key = sorted(key)
    for i in range(len(table)):
        table[i].append(sorted_key[i])
               
    decrypted_text = []
    for char in key:
        for i in range(len(table)):
            if char == table[i][-1]:
                table[i].pop()
                decrypted_text.append(table[i])
                table[i] = ['']
    
    # list[0][0], list[1][0], list[2][0], list[3][0]
    # list[0][1], list[1][1], list[2][1], list[3][1]
    # list[0][2], list[1][2], list[2][2], list[3][2]
    #.........
    
    for row in range(len(decrypted_text[i])): # until 7
        for column in range(len(decrypted_text)): # until 3
            print(decrypted_text[column][row],end = '')
            
            

choice = int(input("choose.( for encrypt enter 1 and decrypt enter 0): "))
             
if(choice):
    main_text = input("Please enter the text to get encrypt: ")
    key = input("Please enter the key: ")
    encrypt(main_text, key)
else:
    encrypted_text = input("Please enter the encrypted text to get decrypt: ")
    key = input("Please enter the key: ")
    decrypt(encrypted_text, key)