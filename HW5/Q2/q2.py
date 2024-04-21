
import numpy as np
from icecream import ic

file_path = "/home/glados/Documents/AmirAli Toori/Lessons/Python/HWs/AdvancedPrograming-HWs/HW5/Q2/doc.txt"

def macDetection(array):
    row, column = np.shape(array)
    
    check_list = []
    for r in range(1, row):
            mac_address = array[r, 1]
            first_half = mac_address[0:8]
            if first_half not in check_list:
                check_list.append(first_half)
    
    for item in check_list:
        for r in range(1, row):
            mac_address = array[r, 1]
            if item == mac_address[0:8]:
                print(f"{item} --> {mac_address}")
        print('-----------------------------------------')

def InternetProtocol(array, string):
    length = len(string)
    row, column = np.shape(array)
    
    
    for r in range(1, row):
        ip = array[r, 0]
        if ip[:length] == string:
            print(f"{string} --> {ip}")
    print("**************************************************")

def sameMAC(array):
    
    check_list = []
    repeat_list = []
    row, column = np.shape(array)
    
    for r in range(1, row):
        if array[r, 1] not in check_list:
            check_list.append(array[r, 1])
        elif array[r, 1] in check_list:
            repeat_list.append(array[r, 1])
    
    for r in range(1, row):
            if array[r, 0 + 1] in repeat_list:
                print(array[r, 0])


try:
    with open(file_path, 'r') as f:
        lines = len(f.readlines())
        f.seek(0)
        
        justOnce = True
        token_list = []
        for _ in range(lines):
            line = f.readline()
            token = line.split()
            
            if justOnce:
                token[0] = token[0] + token[1]
                token.remove(token[1])
                token[1] = token[1] + token[2]
                token.remove(token[2])
                justOnce = False
            
            ic(token)
            token_list.append(token)
            
except:
    raise IOError("The file does not exist.")
else:
    token_array = np.array(token_list, dtype = object)
    
    start_string = input("Please enter the start string for IP: ")
    InternetProtocol(token_array, start_string)
    
    print("Which IP addresses correspond to same MAC addresses: ")
    sameMAC(token_array)
    
    print("The mac addresses which belong to a same manufacture: ")
    macDetection(token_array)
    
    
    
    