
# from icecream import ic
import os


with open("/home/glados/Documents/AmirAli Toori/Lessons/Python/HWs/AdvancedPrograming-HWs/HW5/Q1/text.txt", "r") as f:
    lower = f.readline()
    upper = f.readline()

file_path = "/home/glados/Documents/AmirAli Toori/Lessons/Python/HWs/AdvancedPrograming-HWs/HW5/Q1/mytext.txt"

if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        my_text = f.write(input("Please enter the desire string that you want: "))
    
else:
    with open(file_path, "w") as f:
        my_text = f.write(input("Please enter the desire string that you want: "))

with open(file_path, "r") as f:
    my_text = f.read()
    
    
lower = list(lower)
upper = list(upper)

lower_to_upper_dict = dict(zip(lower, upper))
upper_to_lower_dict = dict(zip(upper, lower))


my_text = my_text.split(' ')
my_text = ''.join(my_text)
my_text = list(my_text)

def encryptText(my_text):
    txt = my_text.copy()
    for key in lower_to_upper_dict:
        for char in my_text:
            if char == key:
                index = txt.index(char)
                txt[index] = lower_to_upper_dict[key]
                
    for key in upper_to_lower_dict:
        for char in my_text:
            if char == key:
                index = txt.index(char)
                txt[index] = upper_to_lower_dict[key]
    txt = ''.join(txt)
    return txt

def decryptText(my_text):
    my_text = list(my_text)
    txt = my_text.copy()
    for key in lower_to_upper_dict:
        for char in my_text:
            if char == key:
                index = txt.index(char)
                txt[index] = lower_to_upper_dict[key]
                
    for key in upper_to_lower_dict:
        for char in my_text:
            if char == key:
                index = txt.index(char)
                txt[index] = upper_to_lower_dict[key]
    txt = ''.join(txt)
    return txt

print(f"The encrypted text is : {encryptText(my_text)}")
print(f"The decrypted text is : {decryptText(encryptText(my_text))}")








