
import matplotlib.pyplot as plt
import re

file_path = "text.txt"

with open(file_path, "r") as f:
    text = f.read()
    
pattern = re.compile(r"[\-]{0,1}[0-9]+[\.]{1}[\d]{6,}")

temp = pattern.findall(text)

times_lst = [int(float(value)) for value in temp]

dictionary = {str(number):times_lst.count(number) for number in times_lst}

seconds = list(dictionary.keys())
numbers = list(dictionary.values())


fig, ax = plt.subplots(figsize = (20, 10))
ax.plot(seconds, numbers, marker = "o", linewidth = 2)
ax.set_xlabel("Second", fontsize = 15)
ax.set_ylabel("Number of packets", fontsize = 15)
ax.set_title("Number of packets which record per second")
ax.tick_params(axis = "x", rotation = 90, labelsize = 8)
ax.grid(True, axis = 'both', linestyle = "--")

for count, value in enumerate(numbers):
    ax.text(count, value, str(value), ha = "right", va = "bottom")

plt.show()