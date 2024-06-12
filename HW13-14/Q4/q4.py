
import tkinter as tk



window = tk.Tk()
window.geometry("650x70")
window.title("HW13-14-Q4")

frame = tk.Frame(window)
frame.rowconfigure(0, weight = 1)

FONT = ("Arial", 10, "bold")
STICKY = tk.E + tk.W
PAD_VALUE = 10

url_var = tk.StringVar()

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
                    command = None
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