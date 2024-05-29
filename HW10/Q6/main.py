

import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
from icecream import ic

df = pd.read_excel('file.xlsx')
names = df['names'].tolist()
years = [ year for year in range(1900, 2030, 10)]

values_lists = df.values.tolist()
array = np.array(values_lists)


def plot():
    plt.figure().clear()
    row, column = np.shape(array)
    names_plot = []
    values = []
    temp_lst = []

    for name in names:
        if name in names_input.get():
            
            for r in range(row):
                if name == array[r, 0]:
                    names_plot.append(array[r, 0])
                
                    for c in range(1, column):
                        temp_lst.append(array[r, c])
                    values.append(temp_lst)
                    temp_lst = []
    
   
    fig = plt.Figure(figsize = (13, 6), 
                 dpi = 100) 
   
    ax = fig.add_subplot(111) 
    
    
    for value in values:
        dictionary = {'rank' : [int(x) for x in value],
                      'year' : years}
        ic(dictionary)
        data_frame = pd.DataFrame(dictionary)
        ic(data_frame)
        
        ax.plot(data_frame['year'], data_frame['rank'])
    
    for x in range(1900, 2030, 10):
        ax.axvline(x, color = 'black')
        
    ax.set_xlim(1900, 2030)
    ax.set_ylim(0, 1000)
    
    ax.invert_yaxis()
    
    ax.set_xticks(data_frame['year'])
    ax.set_xticklabels(data_frame['year'].tolist(), ha = 'left', va = 'bottom')
    ax.tick_params(length = 10, pad = 1)
    
    ax.set_yticks([])
    
    ax.margins(x = 0, y = 0)
    
    canvas = FigureCanvasTkAgg(fig, 
                               master = window)   
    canvas.draw() 
   
    canvas.get_tk_widget().pack() 
   
    toolbar = NavigationToolbar2Tk(canvas, 
                                   window) 
    toolbar.update() 
  
    canvas.get_tk_widget().pack()
    
    
window = tk.Tk()
window.geometry("1280x720")
window.title("Q7")

names_input = tk.StringVar()


entry = tk.Entry(window, 
                 textvariable = names_input,
                 font = ('Arial', 15))
entry.pack()
entry.place(x = 0, y = 0)


button = tk.Button(window,
                   text = "Plot",
                   command = plot,
                   font = ('Arial', 12, 'bold'))
button.pack()
button.place(x = 0, y= 30)





    















#################################################################
window.mainloop()

