
from icecream import ic
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
    for count, char in enumerate(my_text):
        if char in lower_to_upper_dict:
            txt[count] = lower_to_upper_dict[char]
        elif char in upper_to_lower_dict:
            txt[count] = upper_to_lower_dict[char]            
    txt = ''.join(txt)
    return txt

def decryptText(my_text):
    my_text = list(my_text)
    txt = my_text.copy()
    for count, char in enumerate(my_text):
        if char in lower_to_upper_dict:
            txt[count] = lower_to_upper_dict[char]
        elif char in upper_to_lower_dict:
            txt[count] = upper_to_lower_dict[char]
    txt = ''.join(txt)
    return txt

encrypted_text = encryptText(my_text)
print(f"The encrypted text is : {encrypted_text}")
print(f"The decrypted text is : {decryptText(encrypted_text)}")








