

import tkinter as tk




def main():
    
    window = tk.Tk()
    
    window.geometry("800x600")
    window.title("BMI Calculator")
    
    def reset():
        
        for widget in frame.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, 'end')
                
        for widget in window.winfo_children():
            if isinstance(widget, tk.Text):
                widget.delete('1.0', 'end')
                
        for widget in window.winfo_children():
            if isinstance(widget, tk.Radiobutton):
                sex_var.set(None)
    
        
    def bmi_calculator():
        height = height_var.get()
        weight = weight_var.get()
        
        
        
        body_mass_index = round(weight / height**2, 2)
        
        body_mass_index_text = tk.Text(window,
                                height = 5,
                                width = 30)
        body_mass_index_text.insert(tk.END, body_mass_index)
        body_mass_index_text.place(x = 400, y = 550)
        body_mass_index_text.pack()
    
    
    
    title = tk.Label(window,
                     text = "BMI Indicator program",
                     font = ("Arial", 30, "bold")).pack()
    
    frame = tk.Frame(window)
    
    frame.columnconfigure(0, weight = 1)
    frame.columnconfigure(1, weight = 1)
    frame.columnconfigure(2, weight = 1)
    
    height_var = tk.DoubleVar()
    weight_var = tk.DoubleVar()
    age_var = tk.IntVar()
    sex_var = tk.BooleanVar()
    
    
    
    LABEL_FONT = ("Arial", 20, "bold")
    ENTRY_FONT = ("Arial", 20)
    PAD_VALUE = 20
    STICKY = tk.W + tk.E
    
    height_label = tk.Label(frame,
                            text = "Height:",
                            font = LABEL_FONT)
    height_label.grid(row = 0,
                      column = 0,
                      sticky = STICKY,
                      padx = PAD_VALUE,
                      pady = PAD_VALUE)
    
    height_entry = tk.Entry(frame,
                            textvariable = height_var,
                            font = ENTRY_FONT)
    height_entry.grid(row = 0,
                      column = 1,
                      sticky = STICKY,
                      padx = PAD_VALUE,
                      pady = PAD_VALUE)
    
    ###################################
    
    weight_label = tk.Label(frame,
                            text = "Weight:",
                            font = LABEL_FONT)
    weight_label.grid(row = 1,
                      column = 0,
                      sticky = STICKY,
                      padx = PAD_VALUE,
                      pady = PAD_VALUE)
    
    weight_entry = tk.Entry(frame,
                            textvariable = weight_var,
                            font = ENTRY_FONT)
    weight_entry.grid(row = 1,
                      column = 1,
                      sticky = STICKY,
                      padx = PAD_VALUE,
                      pady = PAD_VALUE)
    
    ###########################################
    
    age_label = tk.Label(frame,
                         text = "Age:",
                         font = LABEL_FONT)
    age_label.grid(row = 2,
                   column = 0,
                   sticky = STICKY,
                   padx = PAD_VALUE,
                   pady = PAD_VALUE)
    
    age_entry = tk.Entry(frame,
                         textvariable = age_var,
                         font = ENTRY_FONT)
    age_entry.grid(row = 2,
                   column = 1,
                   sticky = STICKY,
                   padx = PAD_VALUE,
                   pady = PAD_VALUE)
    
    #################################################
    
    sex_label = tk.Label(frame,
                         text = "Sex:",
                         font = LABEL_FONT)
    sex_label.grid(row = 3,
             column = 0,
             sticky = STICKY,
             padx = PAD_VALUE,
             pady = PAD_VALUE)
    
    
    
    sex_male_option = tk.Radiobutton(frame,
                                    text = "Male",
                                    variable = sex_var,
                                    value = "male")
    sex_male_option.grid(row = 3,
                         column = 1,
                         sticky = STICKY)
    
    sex_female_option = tk.Radiobutton(frame,
                                    text = "Female",
                                    variable = sex_var,
                                    value = "female")
    sex_female_option.grid(row = 3,
                         column = 2,
                         sticky = STICKY)
    
    
    frame.pack()
    #################################################
    
    enter_btn = tk.Button(window,
                          text = "ENTER",
                          font = ("Arial", 15, "bold"),
                          command = bmi_calculator)
    enter_btn.place()
    enter_btn.pack()
    
    reset_btn = tk.Button(window,
                          text = "RESET",
                          font = ("Arial", 15, "bold"),
                          bg = "red",
                          command = reset)
    reset_btn.place(x = 370, y = 500)
    reset_btn.pack()
    
    
    window.mainloop()
    pass





if __name__ ==  "__main__":
    main()