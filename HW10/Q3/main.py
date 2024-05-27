

import tkinter as tk


def main():
    
    window = tk.Tk()
    window.geometry("800x250")
    window.title("Loan Calculator")
    
    amount_var = tk.DoubleVar()
    interest_rate_var = tk.DoubleVar()
    installment_count_var = tk.IntVar()
    
    def calculate():
        
        amount = amount_var.get()
        interest_rate = interest_rate_var.get()
        installment_count = installment_count_var.get()
        
        amount_of_per_installment = round(((amount * interest_rate * 0.01) + amount) / installment_count, 2)
        
        result_window = tk.Tk()
        result_window.geometry("700x80")
        
        LABEL_FONT = ("Arial", 15)
        
        installment_label = tk.Label(result_window,
                          text = f"Amount of that you need to pay for every installment is {amount_of_per_installment}",
                          font = LABEL_FONT).pack()
        
        ok_btn = tk.Button(result_window,
                           text = "OK",
                           font = LABEL_FONT,
                           command = lambda: result_window.destroy()).pack()
        result_window.mainloop()
        
    def reset():
        for widget in frame.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, 'end')
        calculate_btn["state"] = "disabled"
        reset_btn["state"] = "disabled"
    
    frame = tk.Frame(window)
    
    frame.columnconfigure(0, weight = 1)
    frame.columnconfigure(1, weight = 1)
    frame.columnconfigure(2, weight = 1)
    
    
    LABEL_FONT = ("Arial", 20 ,"bold")
    PAD_VALUE = 10
    STICKY = tk.W + tk.E
    
    amount_label = tk.Label(frame,
                            text = "Amount:",
                            font = LABEL_FONT)
    amount_label.grid(row = 0,
                      column = 0,
                      sticky = STICKY,
                      padx = PAD_VALUE,
                      pady = PAD_VALUE)
    
    amount_entry = tk.Entry(frame,
                            textvariable = amount_var,
                            font = LABEL_FONT)
    amount_entry.grid(row = 0,
                    column = 1,
                    sticky = STICKY,
                    padx = PAD_VALUE,
                    pady = PAD_VALUE)
    ###########################################
    
    interest_rate_label = tk.Label(frame,
                                   text = "Interest Rate:",
                                   font = LABEL_FONT)
    interest_rate_label.grid(row = 1,
                            column = 0,
                            sticky = STICKY,
                            padx = PAD_VALUE,
                            pady = PAD_VALUE)
    
    interest_rate_entry = tk.Entry(frame,
                                   textvariable = interest_rate_var,
                                   font = LABEL_FONT)
    interest_rate_entry.grid(row = 1,
                             column = 1,
                             sticky = STICKY,
                             padx = PAD_VALUE,
                             pady = PAD_VALUE)
    
    ####################################################
    
    installment_count_label = tk.Label(frame,
                                text = "Number of loan Installment:",
                                font = LABEL_FONT)
    installment_count_label.grid(row = 2,
                                 column = 0,
                                 sticky = STICKY)
    
    installment_count_entry = tk.Entry(frame,
                                       textvariable = installment_count_var,
                                       font = LABEL_FONT)
    installment_count_entry.grid(row = 2,
                                 column = 1,
                                 sticky = STICKY,
                                 padx = PAD_VALUE,
                                 pady = PAD_VALUE)
    
    ####################################################
    
    calculate_btn = tk.Button(frame,
                              text = "Calculate",
                              font = ("Arial", 15),
                              bg = 'green',
                              command = calculate,
                              state = "disabled")
    calculate_btn.grid(row = 3,
                       column = 0,
                       sticky = STICKY,
                       padx = PAD_VALUE,
                       pady = PAD_VALUE)
    
    reset_btn = tk.Button(frame,
                              text = "Reset",
                              font = ("Arial", 15),
                              bg = 'Red',
                              command = reset,
                              state = "disabled")
    reset_btn.grid(row = 3,
                       column = 1,
                       sticky = STICKY,
                       padx = PAD_VALUE,
                       pady = PAD_VALUE)
    
    
    def check(*args):
        if amount_var.get() > 0 and interest_rate_var.get() > 0 and installment_count_var.get() > 0:
            calculate_btn.config(state = "normal")
            reset_btn.config(state = "normal")

    
    amount_var.trace_add("write", check)
    interest_rate_var.trace_add("write", check)
    installment_count_var.trace_add("write", check)
    
    frame.pack()
    
    
    
    
    
    
    
    
    
    window.mainloop()






if __name__ == "__main__":
    main()