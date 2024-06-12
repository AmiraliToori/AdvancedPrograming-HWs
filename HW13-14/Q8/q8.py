

import tkinter as tk


window = tk.Tk()
window.geometry("600x600")
window.title("Calculator")

BACKGROUND_COLOR = "#363346"

window.configure(background = BACKGROUND_COLOR)

frame = tk.Frame(
        window,
                )

frame.columnconfigure(0, weight = 1)
frame.columnconfigure(1, weight = 1)
frame.columnconfigure(2, weight = 1)
frame.columnconfigure(3, weight = 1)
frame.columnconfigure(4, weight = 1)

STICKY = tk.E + tk.W
NUMPAD_BG = "#888598"
RED_BG = "#c58ea8"
NUMPAD_FONT = ('Arial', 42)

TEXT_BOX_BG = "#9ba698"
TEXT_BOX_FONT = ('Arial', 35, 'bold')

PAD_VALUE = 10

queue = []

text_box = tk.Text(
                    window,
                    bg = TEXT_BOX_BG,
                    fg = "black",
                    width = 21,
                    height = 3,
                    font = TEXT_BOX_FONT,
                    padx = PAD_VALUE,
                    pady = PAD_VALUE
                    )

##############################################

button_memory_add = tk.Button(
                    frame,
                    text = "M+",
                    command = None,
                    bg = 'black',
                    fg = 'white',
                    font = NUMPAD_FONT
                    )
button_memory_add.grid(
            row = 0,
            column = 3,
            sticky = STICKY
            )

####################################################

button_memory_subtract = tk.Button(
                    frame,
                    text = "M-",
                    command = None,
                    bg = 'black',
                    fg = 'white',
                    font = NUMPAD_FONT
                    )
button_memory_subtract.grid(
            row = 0,
            column = 2,
            sticky = STICKY
            )

#####################################################

button_memory_recall = tk.Button(
                    frame,
                    text = "MRC",
                    command = None,
                    bg = 'black',
                    fg = 'white',
                    font = NUMPAD_FONT
                    )
button_memory_recall.grid(
            row = 0,
            column = 1,
            sticky = STICKY
            )

################################################

def off_calculator() -> None:
    window.destroy()

button_off = tk.Button(
                    frame,
                    text = "OFF",
                    command = off_calculator,
                    bg = 'black',
                    fg = 'white',
                    font = NUMPAD_FONT
                    )
button_off.grid(
            row = 0,
            column = 0,
            sticky = STICKY
            )

################################################

button_all_clear = tk.Button(
                    frame,
                    text = "AC",
                    command = None,
                    bg = RED_BG,
                    fg = 'white',
                    font = NUMPAD_FONT
                    )
button_all_clear.grid(
            row = 4,
            column = 0,
            sticky = STICKY
            )

################################################

def clear() -> None:
    text_box.delete("0.0", tk.END)

button_clear = tk.Button(
                    frame,
                    text = "C",
                    command = clear,
                    bg = RED_BG,
                    fg = 'white',
                    font = NUMPAD_FONT
                    )
button_clear.grid(
            row = 3,
            column = 0,
            sticky = STICKY
            )


#######################################################

button_sqrt = tk.Button(
                    frame,
                    text = "√",
                    command = None,
                    bg = 'black',
                    fg = 'white',
                    font = NUMPAD_FONT
                    )
button_sqrt.grid(
            row = 2,
            column = 0,
            sticky = STICKY
            )

############################################

button_percent = tk.Button(
                    frame,
                    text = "%",
                    command = None,
                    bg = 'black',
                    fg = 'white',
                    font = NUMPAD_FONT
                    )
button_percent.grid(
            row = 1,
            column = 0,
            sticky = STICKY
            )

####################################################

button_division = tk.Button(
                    frame,
                    text = "÷",
                    command = None,
                    bg = 'black',
                    fg = 'white',
                    font = NUMPAD_FONT
                    )
button_division.grid(
            row = 0,
            column = 4,
            sticky = STICKY
            )

####################################################

button_cross = tk.Button(
                    frame,
                    text = "×",
                    command = None,
                    bg = 'black',
                    fg = 'white',
                    font = NUMPAD_FONT
                    )
button_cross.grid(
            row = 1,
            column = 4,
            sticky = STICKY
            )


####################################################

button_minus = tk.Button(
                    frame,
                    text = "−",
                    command = None,
                    bg = 'black',
                    fg = 'white',
                    font = NUMPAD_FONT
                    )
button_minus.grid(
            row = 2,
            column = 4,
            sticky = STICKY
            )

##################################################

def addition() -> None:
    queue.append(text_box.get())
    

button_addition = tk.Button(
                    frame,
                    text = "+",
                    command = None,
                    bg = 'black',
                    fg = 'white',
                    font = NUMPAD_FONT,
                    height = 2
                    )
button_addition.grid(
            row = 3,
            column = 4,
            rowspan = 2,
            sticky = STICKY
            )


##################################################

button_equal = tk.Button(
                    frame,
                    text = "=",
                    command = None,
                    bg = 'black',
                    fg = 'white',
                    font = NUMPAD_FONT
                    )
button_equal.grid(
            row = 4,
            column = 3,
            sticky = STICKY
            )


###########################################

def insert_float() -> None:
    text_box.insert(tk.END, ".")

button_float = tk.Button(
                    frame,
                    text = ".",
                    command = insert_float,
                    bg = NUMPAD_BG,
                    font = NUMPAD_FONT
                    )
button_float.grid(
            row = 4,
            column = 2,
            sticky = STICKY
            )

###########################################

def insert_0() -> None:
    text_box.insert(tk.END, "0")

button_0 = tk.Button(
                    frame,
                    text = "0",
                    command = insert_0,
                    bg = NUMPAD_BG,
                    font = NUMPAD_FONT
                    )
button_0.grid(
            row = 4,
            column = 1,
            sticky = STICKY
            )


##########################################

def insert_1() -> None:
    text_box.insert(tk.END, "1")

button_1 = tk.Button(
                    frame,
                    text = "1",
                    command = insert_1,
                    bg = NUMPAD_BG,
                    font = NUMPAD_FONT
                    )
button_1.grid(
            row = 3,
            column = 1,
            sticky = STICKY
            )

##########################################

def insert_2() -> None:
    text_box.insert(tk.END, "2")

button_2 = tk.Button(
                    frame,
                    text = "2",
                    command = insert_2,
                    bg = NUMPAD_BG,
                    font = NUMPAD_FONT
                    )
button_2.grid(
            row = 3,
            column = 2,
            sticky = STICKY
            )

###########################################

def insert_3() -> None:
    text_box.insert(tk.END, "3")

button_3 = tk.Button(
                    frame,
                    text = "3",
                    command = insert_3,
                    bg = NUMPAD_BG,
                    font = NUMPAD_FONT
                    )
button_3.grid(
            row = 3,
            column = 3,
            sticky = STICKY
            )

############################################

def insert_4() -> None:
    text_box.insert(tk.END, "4")

button_4 = tk.Button(
                    frame,
                    text = "4",
                    command = insert_4,
                    bg = NUMPAD_BG,
                    font = NUMPAD_FONT
                    )
button_4.grid(
            row = 2,
            column = 1,
            sticky = STICKY
            )


#############################################

def insert_5() -> None:
    text_box.insert(tk.END, "5")

button_5 = tk.Button(
                    frame,
                    text = "5",
                    command = insert_5,
                    bg = NUMPAD_BG,
                    font = NUMPAD_FONT
                    )
button_5.grid(
            row = 2,
            column = 2,
            sticky = STICKY
            )

##############################################

def insert_6() -> None:
    text_box.insert(tk.END, "6")

button_6 = tk.Button(
                    frame,
                    text = "6",
                    command = insert_6,
                    bg = NUMPAD_BG,
                    font = NUMPAD_FONT
                    )
button_6.grid(
            row = 2,
            column = 3,
            sticky = STICKY
            )

##############################################

def insert_7() -> None:
    text_box.insert(tk.END, "7")

button_7 = tk.Button(
                    frame,
                    text = "7",
                    command = insert_7,
                    bg = NUMPAD_BG,
                    font = NUMPAD_FONT
                    )
button_7.grid(
            row = 1,
            column = 1,
            sticky = STICKY
            )

##############################################

def insert_8() -> None:
    text_box.insert(tk.END, "8")

button_8 = tk.Button(
                    frame,
                    text = "8",
                    command = insert_8,
                    bg = NUMPAD_BG,
                    font = NUMPAD_FONT
                    )
button_8.grid(
            row = 1,
            column = 2,
            sticky = STICKY
            )

###############################################

def insert_9() -> None:
    text_box.insert(tk.END, "9")

button_9 = tk.Button(
                    frame,
                    text = "9",
                    command = insert_9,
                    bg = NUMPAD_BG,
                    font = NUMPAD_FONT
                    )
button_9.grid(
            row = 1,
            column = 3,
            sticky = STICKY
            )

##################################################

text_box.pack()
frame.pack()


window.resizable(False, False)
window.overrideredirect(True)
window.mainloop()
