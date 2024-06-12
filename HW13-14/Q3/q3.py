
import matplotlib.pyplot as plt
import re
import numpy as np

file_path = "text.txt"

with open(file_path, "r") as f:
    text = f.read()
    
pattern = re.compile(r"[0-9]+[\.]{1}[\d]{6,}")

temp = pattern.findall(text)

times_lst = [int(float(value)) for value in temp]


fig, ax = plt.subplots(figsize = (10, 6))

ax.hist(times_lst)
ax.set_xlabel("Second")
ax.set_ylabel("Number of packets")
ax.set_title("Number of packets which record per second")
ax.set_xticks([x * 10**8 for x in np.arange(0, 2.8, 0.1)])
ax.grid(True, axis = 'y')

plt.show()