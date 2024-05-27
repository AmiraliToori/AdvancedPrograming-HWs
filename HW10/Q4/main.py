
import tkinter as tk


def main():
    
    def convert(base: int, decimal: int) -> str:
        lst = []
        remainder = 1
        while remainder != 0:
            remainder = decimal % base
            decimal = decimal // base
            lst.append(str(remainder))
        return ''.join(reversed(lst))
    
            
    
    window = tk.Tk()
    window.geometry("600x100")
    window.title("Converter")
    
    ##########################################################
    frame = tk.Frame(window)
    
    frame.columnconfigure(0, weight = 1)
    frame.columnconfigure(1, weight = 1)
    
    input_var = tk.StringVar()
        
    LABEL_FONT = ("Arial", 20, "bold")
    PAD_VALUE = 10
    STICKY = tk.W + tk.E
    
    ############################################################
    input_label = tk.Label(frame,
                           text = "Binary Input",
                           font = LABEL_FONT)
    input_label.grid(row = 0,
                     column = 0,
                     sticky = STICKY,
                     padx = PAD_VALUE,
                     pady = PAD_VALUE)
    
    input_entry = tk.Entry(frame,
                           textvariable = input_var,
                           font = LABEL_FONT)
    input_entry.grid(row = 0,
                     column = 1,
                     sticky = STICKY,
                     padx = PAD_VALUE,
                     pady = PAD_VALUE)
    frame.pack()
    #####################################################
    
    
    def calculate():
        binary = input_var.get()
        
        decimal = int(binary, 2)
        

        if decimal >= 4:
            base_4 = convert(4, decimal)
        else:
            base_4 = -1
            
        if decimal >= 6:
            base_6 = convert(6, decimal)
        else:
            base_6 = -1
        
        if decimal >= 8:
            octan = convert(8, decimal)
        else:
            octan = -1
            
        for widget in frame.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, 'end')    
            
        result_window = tk.Tk()
        result_window.geometry("600x75")
        result_window.title("Convert Result")
        
        frame_result = tk.Frame(result_window)
        frame_result.rowconfigure(0, weight = 1)
        
        LABEL_FONT = ("Arial", 15, "bold")
        PAD_VALUE = 10
        STICKY = tk.W + tk.E
        
        decimal_label = tk.Label(frame_result,
                                 text = f"Decimal:{decimal}",
                                 font = LABEL_FONT)
        decimal_label.grid(row = 0,
                           column = 0,
                           sticky = STICKY,
                           padx = PAD_VALUE)
        
        four_label = tk.Label(frame_result,
                                 text = f"Base 4:{base_4}",
                                 font = LABEL_FONT)
        four_label.grid(row = 0,
                           column = 1,
                           sticky = STICKY,
                           padx = PAD_VALUE)
        
        six_label = tk.Label(frame_result,
                                 text = f"Base 6:{base_6}",
                                 font = LABEL_FONT)
        six_label.grid(row = 0,
                           column = 2,
                           sticky = STICKY,
                           padx = PAD_VALUE)
        
        octan_label = tk.Label(frame_result,
                                 text = f"Octan:{octan}",
                                 font = LABEL_FONT)
        frame_result.pack()
        
        octan_label.grid(row = 0,
                           column = 3,
                           sticky = STICKY,
                           padx = PAD_VALUE)
        
        ok_btn = tk.Button(result_window,
                           text = "OK",
                           font = LABEL_FONT,
                           command = lambda: result_window.destroy()).pack()
        
        result_window.mainloop()
    
    
    ######################################################
    calculate_btn = tk.Button(window,
                              text = "Calculate",
                              font = ("Arial", 15),
                              bg = 'lightgreen',
                              command = calculate,
                              state = "disabled").pack()
     
    
    window.mainloop()





if __name__ == "__main__":
    main()