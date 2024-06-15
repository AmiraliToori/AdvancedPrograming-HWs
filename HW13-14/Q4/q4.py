
import tkinter as tk
import pandas as pd
import numpy as np
import re
import seaborn as sns
import matplotlib.pyplot as plt

window = tk.Tk()
window.geometry("650x70")
window.title("HW13-14-Q4")


frame = tk.Frame(window)
frame.rowconfigure(0, weight = 1)

FONT = ("Arial", 10, "bold")
STICKY = tk.E + tk.W
PAD_VALUE = 10

url_var = tk.StringVar()


def search()-> None:
    df = pd.read_html(url_var.get(), match = r"Climate data")
    
    climate_table = df[0]
        
    climate_table.drop([len(climate_table) - 1, len(climate_table) - 2], axis = 'index', inplace = True)
    
    climate_table.drop(climate_table.columns[0], axis = 'columns', inplace = True)
    
    
    column = climate_table.shape[1]
    pattern = re.compile(r"\s{1}[(].*")
    
    climate_table = np.array(climate_table)
    
    print(climate_table)

    for row in range(climate_table.shape[0]):
        for column in range(climate_table.shape[1]):
            
            print(pattern.findall(climate_table[row, column]))
                  
            if pattern.findall(climate_table[row, column]):
                climate_table[row, column] = float(pattern.sub("", climate_table[row, column]))
            else:
                climate_table[row, column] = float(climate_table[row, column])
    
    climate_table = pd.DataFrame(climate_table)
    
    # climate_table.to_csv("Q4/table.csv")
    # print(climate_table)
    # page = requests.get(url_var.get())
    # soup = BeautifulSoup(page.text, "html.parser")
    # table = soup.find(class_ = "wikitable")
    # # print(table)
    
    # body = table.find("tbody")
    # # print(body)
    # rows = body.find_all("tr")[2:]
    # for row in rows:
    #     data = row.find_all("td")
    #     # print(row)
    #     for text in data:
    #         print(text.get_text())
    
    
    
    
    
url_label = tk.Label(
                    frame,
                    text = "URL:",
                    font = FONT
)
url_label.grid(
                row = 0,
                column = 0,
                sticky = STICKY,
                padx = 10,
                pady = 10
)

entry = tk.Entry(
                frame,
                textvariable = url_var,
                width = 50
)
entry.grid(
            row = 0,
            column = 1,
            sticky = STICKY,
            padx = PAD_VALUE,
            pady = PAD_VALUE 
)

button = tk.Button(
                    frame,
                    text = "Submit",
                    command = search
)
button.grid(
            row = 0,
            column = 2,
            sticky = STICKY,
            padx = PAD_VALUE,
            pady = PAD_VALUE
)

frame.pack()

window.mainloop()