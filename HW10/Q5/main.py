


import tkinter as tk
from tkinter import ttk


def main():
    
    
    window = tk.Tk()
    window.geometry("1000x300")
    window.title("Unit Converter")
    

    frame = tk.Frame(window)
    frame.rowconfigure(0, weight = 1)
    frame.rowconfigure(1, weight = 1)
    frame.rowconfigure(2, weight = 1)


    FONT_LABEL = ("Arial", 20, "italic")
    STICKY = tk.E + tk.W
    PAD_VALUE = 10
    
    title = tk.Label(frame,
                     text = "Unit Converter",
                     font = ("Arial", 30, "bold"))
    title.grid(row = 0,
               column = 1,
               sticky = STICKY,
               padx = PAD_VALUE,
               pady = PAD_VALUE)
    
    ########################################################
    
    def choose_type(event):
        if combo_options.get() == "weight":
            combo_one['value'] = weight_options
            combo_two['value'] = weight_options
            
        if combo_options.get() == "length":
            combo_one['value'] = length_options
            combo_two['value'] = length_options
            
        if combo_options.get() == "volume":
            combo_one['value'] = volume_options
            combo_two['value'] = volume_options
            
        if combo_options.get() == "velocity":
            combo_one['value'] = velocity_options
            combo_two['value'] = velocity_options
        
    
    weight_options = ["Kilogram(kg)",
                      "Milligram(mg)",
                      "Microgram(µg)",
                      "Ton(t)",
                      "Pound(lb)",
                      "Ounce(oz)",
                      "Stone(st)",
                      "Carat(ct)"]
    
    length_options = ["Meter(m)",
                      "Kilometer(km)",
                      "Centimeter(cm)",
                      "Millimeter(mm)",
                      "Micrometer(µm)",
                      "Nanometer(nm)",
                      "Mile(mi)",
                      "Yard(yd)",
                      "Foot(ft)",
                      "Inch(in)"]
    
    volume_options = ["CubicMeter(m³)",
                      "CubicCentimeter(cm³ or cc)",
                      "CubicMillimeter(mm³)",
                      "Liter(L)",
                      "Milliliter(mL)",
                      "CubicInch(in³)",
                      "CubicFoot(ft³)",
                      "CubicYard(yd³)",
                      "Gallon(gal)",
                      "Quart(qt)"]
    
    velocity_options = ["MetersPerSecond(m/s)",
                       "KilometersPerHour(km/h)",
                       "MilesPerHour(mph)",
                       "FeetPerSecond(ft/s)",
                       "Mach(M)",
                       "LightSpeed(c)"]
    
    options = ["","velocity", "volume", "weight", "length"]
    
    entry_one_var = tk.DoubleVar()
    entry_two_var = tk.DoubleVar()
    
    def convert(event):
        
        pass
    
    
    entry_one = tk.Entry(frame,
                         textvariable = entry_one_var)
    entry_one.grid(row = 2,
                   column = 0,
                   sticky = STICKY,
                   padx = PAD_VALUE,
                   pady = PAD_VALUE)
    
    entry_two = tk.Entry(frame,
                         textvariable = entry_two_var)
    entry_two.grid(row = 2,
                   column = 2,
                   sticky = STICKY,
                   padx = PAD_VALUE,
                   pady = PAD_VALUE)
    
    
    combo_options = ttk.Combobox(frame,
                                value = options)
    combo_options.current(0)
    combo_options.bind("<<ComboboxSelected>>", choose_type)
    combo_options.grid(row = 1,
                       column = 1,
                       sticky = STICKY,
                       padx = PAD_VALUE,
                       pady = PAD_VALUE)
    
    
    
    combo_one = ttk.Combobox(frame)
    combo_one.bind("<<ComboboxSelected>>", convert)
    combo_one.grid(row = 1,
                       column = 0,
                       sticky = STICKY,
                       padx = PAD_VALUE,
                       pady = PAD_VALUE)
    
    combo_two = ttk.Combobox(frame)
    combo_one.bind("<<ComboboxSelected>>", convert)
    combo_two.grid(row = 1,
                       column = 2,
                       sticky = STICKY,
                       padx = PAD_VALUE,
                       pady = PAD_VALUE)

     
    
    
    frame.pack()


    window.mainloop()

if __name__ == "__main__":
    main()




