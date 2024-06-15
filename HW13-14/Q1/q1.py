
import re

file_path = "text.txt"

with open(file_path, "r") as f:
    text = f.read()

pattern = re.compile(r"[0-9]{1,3}\.+[0-9]{1,3}\.+[0-9]{1,3}\.+[0-9]{1,3}")

ip_address_lst = set(pattern.findall(text))

ip_address_file_path = "Q1/IP.txt"

file = open(ip_address_file_path, "x") 
    
with open(ip_address_file_path, "a") as f:
    for ip in ip_address_lst:
        f.write(f"{ip} ")