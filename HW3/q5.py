from random import choices

def checkAnswer(input, answer):
    black_candle = 0 # the place and color is correct
    white_candle = 0 # only the color is correct
    
    for i in range(len(answer)):
        for j in range(len(answer)):
            if i == j and input[i] == answer[j]:
                black_candle += 1
    
    for i in range(len(answer)):
        if answer[i] in input:
            white_candle += 1
            
    white_candle = white_candle - black_candle
    return black_candle, white_candle
                

CHOICE = ('W', 'R', 'G', 'B', 'P', 'D', 'Y', 'O')
ANSWER_LENGTH = 4

answer = choices(CHOICE ,k = ANSWER_LENGTH)
answer = ''.join(answer)
    
print(answer)

flag = True
count = 0

while(flag):
    
    user_input = input("Please enter the answer: ")
    
    for count, char in enumerate(user_input):
        if char not in CHOICE:
            print("THE INPUT IS WRONG!")
            flag = False
            break
    
    if len(user_input) != ANSWER_LENGTH:
        print("THE INPUT IS WRONG!")
        continue
    
    if user_input.islower():
        user_input = user_input.upper()
    
    candle_count = checkAnswer(user_input, answer)
    count += 1
    
    print(f"The number of black candles: {candle_count[0]}")
    print(f"The number of white candles: {candle_count[1]}")
    
    if candle_count[0] == 4:
        print("The answer is correct!")
        flag = False
    
    elif count == 2:
        print("GAME OVER!")
        flag = False