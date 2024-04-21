def compress(input):
    
    repeated_char = []
    
    for i in range(128):
        char = chr(i)
        if input.count(char) > 1:
            repeated_char.append(char)
    
    input = list(input)
    
    for i in range(len(repeated_char)):
        count = 0
        for j in range(len(input)):
            if repeated_char[i] == input[j]:
                count += 1
                if count > 1:
                    input[j] = ''
                    

    input = ''.join(input)
    return input
            

my_input = input("Please enter your string: ")

print(compress(my_input))