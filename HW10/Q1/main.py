


import tkinter as tk
import sqlite3

connect = sqlite3.connect("students.db")

c = connect.cursor()

with connect:
    
    c.execute('''CREATE TABLE IF NOT EXISTS Students(
        std_id INTEGER PRIMARY KEY,
        std_name TEXT NOT NULL,
        date_of_birth TEXT NOT NULL,
        total_average_score REAL,
        year_of_enter INTEGER NOT NULL,
        passed_credits INTEGER) ''')
    
def insert_value(std_id: int,
                 std_name: str,
                 date_of_birth: str,
                 total_average_score: float,
                 year_of_enter: int,
                 passed_credits: int) -> None:
    
    with connect:
        c.execute('''INSERT INTO Students VALUES(?,?,?,?,?,?)''',
            (std_id,
            std_name,
            date_of_birth,
            total_average_score,
            year_of_enter,
            passed_credits))



def main():

    window = tk.Tk()
    window.geometry("800x550")
    window.title("Student's Information Entry")
    
    name_var = tk.StringVar()
    id_var = tk.IntVar()
    date_of_birth_var = tk.StringVar()
    total_average_score_var = tk.DoubleVar()
    year_of_enter_var = tk.IntVar()
    passed_credits_var = tk.IntVar()
    
    
    def submit():
        
        std_id = id_var.get()
        std_name = name_var.get()
        date_of_birth = date_of_birth_var.get()
        total_average_score = total_average_score_var.get()
        year_of_enter = year_of_enter_var.get()
        passed_credits = passed_credits_var.get()

        insert_value(std_id,
                     std_name,
                     date_of_birth,
                     total_average_score,
                     year_of_enter,
                     passed_credits)
        
        for widget in label_frame.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, 'end')
        
    
    main_title_label = tk.Label(window,
                                text = "Student Information",
                                font = ("Arial", 40, "bold"))
    main_title_label.pack(padx = 10, pady = 10)
    
    label_frame = tk.Frame(window)
    
    label_frame.columnconfigure(0, weight=1)
    label_frame.columnconfigure(1, weight=1)
    label_frame.columnconfigure(2, weight=1)
    
    LABEL_FONT = ("Arial", 20, "italic")
    ENTRY_FONT = ("Arial", 15)
    PAD_VALUE = 10
    STICKY = tk.W + tk.E
    ###################################################
    
    student_name_label = tk.Label(label_frame,
                                  text = "Name:",
                                  font = LABEL_FONT)
    student_name_label.grid(row = 0,
                            column = 0,
                            sticky = STICKY,
                            padx = PAD_VALUE,
                            pady = PAD_VALUE)
    
    
    student_name_entry = tk.Entry(label_frame,
                                  textvariable = name_var,
                                  font = ENTRY_FONT)
    student_name_entry.grid(row = 0,
                            column = 1,
                            sticky = STICKY,
                            padx = PAD_VALUE,
                            pady = PAD_VALUE)
    
    ####################################33
    student_id_label = tk.Label(label_frame,
                          text = "ID:",
                          font = LABEL_FONT)
    student_id_label.grid(row = 1,
                          column = 0,
                          sticky = STICKY,
                          padx = PAD_VALUE,
                          pady = PAD_VALUE)
    
    student_id_entry = tk.Entry(label_frame,
                                textvariable = id_var,
                                font = ENTRY_FONT)
    student_id_entry.grid(row = 1,
                          column = 1,
                          sticky = STICKY,
                          padx = PAD_VALUE,
                          pady = PAD_VALUE)
    
    #################################
    student_date_of_birth_label = tk.Label(label_frame,
                                    text = "Date of Birth:",
                                    font = LABEL_FONT)
    student_date_of_birth_label.grid(row = 2,
                                column = 0,
                                sticky = STICKY,
                                padx = PAD_VALUE,
                                pady = PAD_VALUE)
    
    student_date_of_birth_entry = tk.Entry(label_frame,
                                           textvariable = date_of_birth_var,
                                           font = ENTRY_FONT)
    student_date_of_birth_entry.grid(row = 2,
                                     column = 1,
                                     sticky = STICKY,
                                     padx = PAD_VALUE,
                                     pady = PAD_VALUE)
    
    ##################################
    student_total_average_score_label = tk.Label(label_frame,
                                                text = "Average Score:",
                                                font = LABEL_FONT)
    student_total_average_score_label.grid(row = 3,
                                    column = 0,
                                    sticky = STICKY,
                                    padx = PAD_VALUE,
                                    pady = PAD_VALUE)
    
    student_total_average_score_entry = tk.Entry(label_frame,
                                                 textvariable = total_average_score_var,
                                                 font = ENTRY_FONT)
    student_total_average_score_entry.grid(row = 3,
                                           column = 1,
                                           sticky = STICKY,
                                           padx = PAD_VALUE,
                                           pady = PAD_VALUE)
    
    
    ############################
    student_enter_year_label = tk.Label(label_frame,
                                  text = "Year of enter: ",
                                  font = LABEL_FONT)
    student_enter_year_label.grid(row = 4,
                            column = 0,
                            sticky = STICKY,
                            padx = PAD_VALUE,
                            pady = PAD_VALUE)
    
    student_enter_year_entry = tk.Entry(label_frame,
                                        textvariable = year_of_enter_var,
                                        font = LABEL_FONT)
    student_enter_year_entry.grid(row = 4,
                                  column = 1,
                                  sticky = STICKY,
                                  padx = PAD_VALUE,
                                  pady = PAD_VALUE)
    
    ##########################
    student_passed_credits_label = tk.Label(label_frame,
                                      text = "Passed credits:",
                                      font = LABEL_FONT)
    student_passed_credits_label.grid(row = 5,
                                column = 0,
                                sticky = STICKY,
                                padx = PAD_VALUE,
                                pady = PAD_VALUE)
    
    student_passed_credits_entry = tk.Entry(label_frame,
                                            textvariable = passed_credits_var,
                                            font = ENTRY_FONT)
    student_passed_credits_entry.grid(row = 5,
                                      column = 1,
                                      sticky = STICKY,
                                      padx = PAD_VALUE,
                                      pady = PAD_VALUE)
    ###################################
    
    
    
    
    submit_button = tk.Button(text = "Submit",
                              font = ("Arial", 15),
                              command = submit,
                              state = "disabled")
    
    def check_status(*args):
        flag_1 = False
        flag_2 = False
        flag_3 = False
        
        if len(name_var.get()) >= 5:
            flag_1 = True
        if len(str(id_var.get())) == 6:
            flag_2 = True
        if len(date_of_birth_var.get()) == 10:
            flag_3 = True
            
        if all([flag_1, flag_2, flag_3]):
            submit_button.config(state = "normal")
        else:
            submit_button.config(state = "disabled")
        
    
    submit_button.pack()
    submit_button.place(x = 350, y = 450)
    label_frame.pack(padx = 10, pady = 10)
    
    name_var.trace_add("write", check_status)
    id_var.trace_add("write", check_status)
    date_of_birth_var.trace_add("write", check_status)
    
    
    window.resizable(False, False)
    window.mainloop()
    


if __name__ == "__main__":
    main()