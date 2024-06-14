
import tkinter as tk
from tkinter import filedialog

from test import test

window = tk.Tk()
window.geometry("700x300")
window.title("Quiz")

frame = tk.Frame(window)

frame.columnconfigure(0, weight = 1)
frame.columnconfigure(1, weight = 1)
frame.columnconfigure(2, weight = 1)

STICKY = tk.E + tk.W
PAD_VALUE = 10
LABEL_FONT = ("Arial", 20, "italic")

count_var = tk.IntVar()
output_file_var = tk.StringVar()

number = 0
flag = False

def choose_file() -> None:
    global file_path
    
    file_path = filedialog.askopenfilename(
                                            title = "Select File",
                                            initialdir = "Q9/",
                                            filetypes = [("Text Files", "*.txt")]
                                            )

def increase_number() -> None:
    global number
    number += 1
    print(number)

def confirmation() -> None:
    
    test.__test__(file_path)
    test.makeTest(count_var.get(),output_file_var.get())

    window2 = tk.Tk()
    
    frame = tk.Frame(window2)
    frame.rowconfigure(0, weight = 1)
    frame.rowconfigure(1, weight = 1)
    frame.rowconfigure(2, weight = 1)
    
    question_label = tk.Label(
                            frame,
                            text = "Question: "+ test.questions[number].question_text,
                            )
    question_label.grid(
                        row = 0,
                        column = 0,
                        sticky = tk.W
                        )
        
    answer1 = tk.Radiobutton(frame, text = test.questions[number].option1, value = 1)
    answer2 = tk.Radiobutton(frame, text = test.questions[number].option2, value = 2)
    answer3 = tk.Radiobutton(frame, text = test.questions[number].option3, value = 3)
    answer4 = tk.Radiobutton(frame, text = test.questions[number].option4, value = 4)
    
    answer1.grid(row = 1, column = 0, sticky = tk.W)
    answer2.grid(row = 2, column = 0, sticky = tk.W)
    answer3.grid(row = 3, column = 0, sticky = tk.W)
    answer4.grid(row = 4, column = 0, sticky = tk.W)
    
    
    next_button = tk.Button(
                            frame,
                            text = "Next",
                            bg = "orange",
                            command = increase_number
                            )
    print(number)
    next_button.grid(row = 5, column = 1, sticky = STICKY)
    
    frame.pack()
    window2.mainloop()
    
    # except:
        # error_win = tk.Tk()
        # error_win.geometry("200x50")
        # error_win.title("Something went wrong!")
        
        # tk.Label(
        #         error_win,
        #         text = "Please try again!"
        #         ).pack()
        
        # tk.Button(
        #             error_win,lambda number: number + 1
        #             text = "OK",
        #             command = error_win.destroy  
        #             ).pack()
        
        # error_win.mainloop()

##################################################################

title_label = tk.Label(
                        window,
                        text = "Test Maker",
                        font = ("Arial", 20, "bold"),
                        )
title_label.place(x = 400, y = 0)
title_label.pack()

###################################################################

choose_bnk_label = tk.Label(
                            frame,
                            text = "Choose Bank Test:",
                            font = LABEL_FONT
                            )
choose_bnk_label.grid(
                        row = 1,
                        column = 0,
                        sticky = STICKY,
                        padx = PAD_VALUE,
                        pady = PAD_VALUE
                        )

choose_bnk_file_btn = tk.Button(
                                frame,
                                text = "Choose",
                                command = choose_file
                                )
choose_bnk_file_btn.grid(
                        row = 1,
                        column = 1,
                        sticky = STICKY,
                        padx = PAD_VALUE,
                        pady = PAD_VALUE
                        )

################################################################

count_question_label = tk.Label(
                                frame,
                                text = "How many question to ask?",
                                font = LABEL_FONT
                                )
count_question_label.grid(
                        row = 2,
                        column = 0,
                        sticky = STICKY,
                        padx = PAD_VALUE,
                        pady = PAD_VALUE
                        )

count_question_entry = tk.Entry(
                                frame,
                                textvariable = count_var,
                                width = 1
                                )
count_question_entry.grid(
                        row = 2,
                        column = 1,
                        sticky = STICKY,
                        padx = PAD_VALUE,
                        pady = PAD_VALUE
                        )

######################################################################

export_file_question_label = tk.Label(
                                frame,
                                text = "Export the name of the test file as:",
                                font = LABEL_FONT
                                )
export_file_question_label.grid(
                        row = 3,
                        column = 0,
                        sticky = STICKY,
                        padx = PAD_VALUE,
                        pady = PAD_VALUE
                        )

export_file_question_entry = tk.Entry(
                                frame,
                                textvariable = output_file_var,
                                width = 1
                                )
export_file_question_entry.grid(
                        row = 3,
                        column = 1,
                        sticky = STICKY,
                        padx = PAD_VALUE,
                        pady = PAD_VALUE
                        )


######################################################################

continue_btn = tk.Button(
                        frame,
                        text = "Continue",
                        command = confirmation,
                        state = "disabled"
                        )
continue_btn.grid(
                row = 4,
                column = 0,
                columnspan = 2,
                sticky = STICKY,
                padx = PAD_VALUE,
                pady = PAD_VALUE
                )

def check_state(*args) -> None:
    if count_var.get() > 0 and len(output_file_var.get()) > 0:
        continue_btn.config(state = "normal")
    else:
        continue_btn.config(state = "disabled")
    

count_var.trace_add("write", check_state)
output_file_var.trace_add("write", check_state)

frame.pack()


window.mainloop()