
import tkinter as tk
from tkinter import filedialog
import re

def select_file() -> None:
    global text
    file_path = filedialog.askopenfilename(
                                            title = "Select File",
                                            filetypes = [("Text Files", "*.txt")]
                                            )
    
    text_box.delete("1.0", tk.END)
    
    with open(file_path, "r") as f:
        text = f.read()
        
    pattern = re.compile(entry_var.get())
    
    findings = pattern.findall(text)
    
    for finding in findings:
        text_box.insert(tk.END,f"{finding} ")
    
    
        

window = tk.Tk()
window.geometry("900x500")
window.title("HW13-14-Q2")

frame = tk.Frame(window)
frame.rowconfigure(0, weight = 1)
frame.rowconfigure(1, weight = 1)

entry_var = tk.StringVar()

PAD_VALUE = 10
STICKY = tk.E + tk.W

select_file_btn = tk.Button(
                            frame,
                            text = "SELECT",
                            command = select_file,
                            )
select_file_btn.grid(
                    row = 0,
                    column = 0,
                    sticky = STICKY,
                    padx = PAD_VALUE,
                    pady = PAD_VALUE
                    )


text_entry = tk.Entry(
                    frame,
                    textvariable = entry_var
                    )
text_entry.grid(
                row = 0,
                column = 1,
                sticky = STICKY,
                padx = PAD_VALUE,
                pady = PAD_VALUE
                )

text_box = tk.Text(
            frame
                    )
text_box.grid(
            row = 1,
            column = 1,
            sticky = STICKY,
            padx = PAD_VALUE,
            pady = PAD_VALUE
            )


frame.pack()


window.mainloop()

