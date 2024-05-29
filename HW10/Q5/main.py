


import tkinter as tk
from tkinter import ttk
from icecream import ic

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
    weight_dict = {count:option for count, option in enumerate(weight_options)}
    
    
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
    length_dict = {count:option for count, option in enumerate(length_options)}
    
    
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
    volume_dict = {count:option for count, option in enumerate(iterable=volume_options)}
    
    
    velocity_options = ["MetersPerSecond(m/s)",
                       "KilometersPerHour(km/h)",
                       "MilesPerHour(mph)",
                       "FeetPerSecond(ft/s)",
                       "Mach(M)",
                       "LightSpeed(c)"]
    velocity_dict = {count:option for count, option in enumerate(iterable=velocity_options)}
    
    
    options = ["","velocity", "volume", "weight", "length"]
    
    entry_one_var = tk.DoubleVar()
    entry_two_var = tk.DoubleVar()
    
    def delete_entry():
        entry_two.delete(0, 'end')
    
    
    def convert_velocity():
        a = combo_one.get()
        b = combo_two.get()
        entry_one = entry_one_var.get()
        
        delete_entry()
        
        if a == velocity_dict[0] and b == velocity_dict[1]:
            entry_two.insert(0, round(entry_one * 3.6, 4))
            
        if a == velocity_dict[0] and b == velocity_dict[2]:
            entry_two.insert(0, round(entry_one * 2.23694, 4))
        
        if a == velocity_dict[0] and b == velocity_dict[3]:
            entry_two.insert(0, round(entry_one * 328084, 2))
        
        if a == velocity_dict[0] and b == velocity_dict[4]:
            entry_two.insert(0, round(entry_one / 343, 4))
        
        if a == velocity_dict[0] and b == velocity_dict[5]:
            entry_two.insert(0, entry_one * 3.3356e-9)
        
        
        if a == velocity_dict[1] and b == velocity_dict[0]:
            entry_two.insert(0, round(entry_one / 3.6, 4))
        
        if a == velocity_dict[1] and b == velocity_dict[2]:
            entry_two.insert(0, round(entry_one / 1.609, 4))
        
        if a == velocity_dict[1] and b == velocity_dict[3]:
            entry_two.insert(0, round(entry_one / 1.097, 4))
        
        if a == velocity_dict[1] and b == velocity_dict[4]:
            entry_two.insert(0, round(entry_one / 1235, 4))
        
        if a == velocity_dict[1] and b == velocity_dict[5]:
            entry_two.insert(0, entry_one / 1.079e+9)
            
        
        if a == velocity_dict[2] and b == velocity_dict[0]:
            entry_two.insert(0, round(entry_one / 2.237, 4))
        
        if a == velocity_dict[2] and b == velocity_dict[1]:
            entry_two.insert(0, round(entry_one * 1.60934, 4))
        
        if a == velocity_dict[2] and b == velocity_dict[3]:
            entry_two.insert(0, round(entry_one * 1.467, 4))
            
        if a == velocity_dict[2] and b == velocity_dict[4]:
            entry_two.insert(0, round(entry_one / 767, 4))
            
        if a == velocity_dict[2] and b == velocity_dict[5]:
            entry_two.insert(0, entry_one * 5.36819e-10)


        if a == velocity_dict[3] and b == velocity_dict[0]:
            entry_two.insert(0, round(entry_one / 3.281, 4))
            
        if a == velocity_dict[3] and b == velocity_dict[1]:
            entry_two.insert(0, round(entry_one * 1.097, 4))
            
        if a == velocity_dict[3] and b == velocity_dict[2]:
            entry_two.insert(0, round(entry_one / 1.467, 4))
            
        if a == velocity_dict[3] and b == velocity_dict[4]:
            entry_two.insert(0, round(entry_one / 1125, 4))
            
        if a == velocity_dict[3] and b == velocity_dict[5]:
            entry_two.insert(0, entry_one / 9.836e+8)


        if a == velocity_dict[4] and b == velocity_dict[0]:
            entry_two.insert(0, round(entry_one * 343, 4))
            
        if a == velocity_dict[4] and b == velocity_dict[1]:
            entry_two.insert(0, round(entry_one * 1235, 4))
            
        if a == velocity_dict[4] and b == velocity_dict[2]:
            entry_two.insert(0, round(entry_one * 767, 4))
            
        if a == velocity_dict[4] and b == velocity_dict[3]:
            entry_two.insert(0, round(entry_one * 1125, 4))
            
        if a == velocity_dict[4] and b == velocity_dict[5]:
            entry_two.insert(0, entry_one / 880991)


        if a == velocity_dict[5] and b == velocity_dict[0]:
            entry_two.insert(0, entry_one / 3.3356e-9)
            
        if a == velocity_dict[5] and b == velocity_dict[1]:
            entry_two.insert(0, entry_one / 1.079e-9)
            
        if a == velocity_dict[5] and b == velocity_dict[2]:
            entry_two.insert(0, entry_one / 5.36819e-10)
            
        if a == velocity_dict[5] and b == velocity_dict[3]:
            entry_two.insert(0, entry_one / 9.836e-10)
            
        if a == velocity_dict[5] and b == velocity_dict[4]:
            entry_two.insert(0, entry_one * 880991)
        
    def convert_weight():
        a = combo_one.get()
        b = combo_two.get()
        entry_one = entry_one_var.get()

        delete_entry()

        # Kilogram to other units
        if a == weight_dict[0] and b == weight_dict[1]:
            entry_two.insert(0, entry_one * 1e6)
            
        if a == weight_dict[0] and b == weight_dict[2]:
            entry_two.insert(0, entry_one * 1e9)
            
        if a == weight_dict[0] and b == weight_dict[3]:
            entry_two.insert(0, entry_one / 1000)
            
        if a == weight_dict[0] and b == weight_dict[4]:
            entry_two.insert(0, entry_one * 2.20462)
            
        if a == weight_dict[0] and b == weight_dict[5]:
            entry_two.insert(0, entry_one * 35.274)
            
        if a == weight_dict[0] and b == weight_dict[6]:
            entry_two.insert(0, entry_one / 6.35)
            
        if a == weight_dict[0] and b == weight_dict[7]:
            entry_two.insert(0, entry_one * 5000)

        # Milligram to other units
        if a == weight_dict[1] and b == weight_dict[0]:
            entry_two.insert(0, entry_one / 1e6)
            
        if a == weight_dict[1] and b == weight_dict[2]:
            entry_two.insert(0, entry_one * 1000)
            
        if a == weight_dict[1] and b == weight_dict[3]:
            entry_two.insert(0, entry_one / 1e9)
            
        if a == weight_dict[1] and b == weight_dict[4]:
            entry_two.insert(0, entry_one / 453592)
            
        if a == weight_dict[1] and b == weight_dict[5]:
            entry_two.insert(0, entry_one / 28350)
            
        if a == weight_dict[1] and b == weight_dict[6]:
            entry_two.insert(0, entry_one / 6.35e6)
            
        if a == weight_dict[1] and b == weight_dict[7]:
            entry_two.insert(0, entry_one / 200)

        # Microgram to other units
        if a == weight_dict[2] and b == weight_dict[0]:
            entry_two.insert(0, entry_one / 1e9)
            
        if a == weight_dict[2] and b == weight_dict[1]:
            entry_two.insert(0, entry_one / 1000)
            
        if a == weight_dict[2] and b == weight_dict[3]:
            entry_two.insert(0, entry_one / 1e12)
            
        if a == weight_dict[2] and b == weight_dict[4]:
            entry_two.insert(0, entry_one / 4.536e8)
            
        if a == weight_dict[2] and b == weight_dict[5]:
            entry_two.insert(0, entry_one / 2.835e7)
            
        if a == weight_dict[2] and b == weight_dict[6]:
            entry_two.insert(0, entry_one / 6.35e9)
            
        if a == weight_dict[2] and b == weight_dict[7]:
            entry_two.insert(0, entry_one / 200000)

        # Ton to other units
        if a == weight_dict[3] and b == weight_dict[0]:
            entry_two.insert(0, entry_one * 1000)
            
        if a == weight_dict[3] and b == weight_dict[1]:
            entry_two.insert(0, entry_one * 1e9)
            
        if a == weight_dict[3] and b == weight_dict[2]:
            entry_two.insert(0, entry_one * 1e12)
            
        if a == weight_dict[3] and b == weight_dict[4]:
            entry_two.insert(0, entry_one * 2204.62)
            
        if a == weight_dict[3] and b == weight_dict[5]:
            entry_two.insert(0, entry_one * 35274)
            
        if a == weight_dict[3] and b == weight_dict[6]:
            entry_two.insert(0, entry_one * 157.473)
            
        if a == weight_dict[3] and b == weight_dict[7]:
            entry_two.insert(0, entry_one * 5e6)

        # Pound to other units
        if a == weight_dict[4] and b == weight_dict[0]:
            entry_two.insert(0, entry_one / 2.20462)
            
        if a == weight_dict[4] and b == weight_dict[1]:
            entry_two.insert(0, entry_one * 453592)
            
        if a == weight_dict[4] and b == weight_dict[2]:
            entry_two.insert(0, entry_one * 4.536e8)
            
        if a == weight_dict[4] and b == weight_dict[3]:
            entry_two.insert(0, entry_one / 2204.62)
            
        if a == weight_dict[4] and b == weight_dict[5]:
            entry_two.insert(0, entry_one * 16)
            
        if a == weight_dict[4] and b == weight_dict[6]:
            entry_two.insert(0, entry_one / 14)
            
        if a == weight_dict[4] and b == weight_dict[7]:
            entry_two.insert(0, entry_one * 2267.96)

        # Ounce to other units
        if a == weight_dict[5] and b == weight_dict[0]:
            entry_two.insert(0, entry_one / 35.274)
            
        if a == weight_dict[5] and b == weight_dict[1]:
            entry_two.insert(0, entry_one * 28350)
            
        if a == weight_dict[5] and b == weight_dict[2]:
            entry_two.insert(0, entry_one * 2.835e7)
            
        if a == weight_dict[5] and b == weight_dict[3]:
            entry_two.insert(0, entry_one / 35274)
            
        if a == weight_dict[5] and b == weight_dict[4]:
            entry_two.insert(0, entry_one / 16)
            
        if a == weight_dict[5] and b == weight_dict[6]:
            entry_two.insert(0, entry_one / 224)
            
        if a == weight_dict[5] and b == weight_dict[7]:
            entry_two.insert(0, entry_one * 141.748)

        # Stone to other units
        if a == weight_dict[6] and b == weight_dict[0]:
            entry_two.insert(0, entry_one * 6.35)
            
        if a == weight_dict[6] and b == weight_dict[1]:
            entry_two.insert(0, entry_one * 6.35e6)
            
        if a == weight_dict[6] and b == weight_dict[2]:
            entry_two.insert(0, entry_one * 6.35e9)
            
        if a == weight_dict[6] and b == weight_dict[3]:
            entry_two.insert(0, entry_one / 157.473)
            
        if a == weight_dict[6] and b == weight_dict[4]:
            entry_two.insert(0, entry_one * 14)
            
        if a == weight_dict[6] and b == weight_dict[5]:
            entry_two.insert(0, entry_one * 224)
            
        if a == weight_dict[6] and b == weight_dict[7]:
            entry_two.insert(0, entry_one * 31751.5)

        # Carat to other units
        if a == weight_dict[7] and b == weight_dict[0]:
            entry_two.insert(0, entry_one / 5000)
            
        if a == weight_dict[7] and b == weight_dict[1]:
            entry_two.insert(0, entry_one * 200)
            
        if a == weight_dict[7] and b == weight_dict[2]:
            entry_two.insert(0, entry_one * 200000)
            
        if a == weight_dict[7] and b == weight_dict[3]:
            entry_two.insert(0, entry_one / 5e6)
            
        if a == weight_dict[7] and b == weight_dict[4]:
            entry_two.insert(0, entry_one / 2267.96)
            
        if a == weight_dict[7] and b == weight_dict[5]:
            entry_two.insert(0, entry_one / 141.748)
            
        if a == weight_dict[7] and b == weight_dict[6]:
            entry_two.insert(0, entry_one / 31751.5)
    
    
    def convert_volume():
        a = combo_one.get()
        b = combo_two.get()
        entry_one = entry_one_var.get()

        delete_entry()

        # Cubic Meter to other units
        if a == volume_dict[0] and b == volume_dict[1]:
            entry_two.insert(0, entry_one * 1e6)
            
        if a == volume_dict[0] and b == volume_dict[2]:
            entry_two.insert(0, entry_one * 1e9)
            
        if a == volume_dict[0] and b == volume_dict[3]:
            entry_two.insert(0, entry_one * 1000)
            
        if a == volume_dict[0] and b == volume_dict[4]:
            entry_two.insert(0, entry_one * 1e6)
            
        if a == volume_dict[0] and b == volume_dict[5]:
            entry_two.insert(0, entry_one * 61023.7)
            
        if a == volume_dict[0] and b == volume_dict[6]:
            entry_two.insert(0, entry_one * 35.3147)
            
        if a == volume_dict[0] and b == volume_dict[7]:
            entry_two.insert(0, entry_one * 1.30795)
            
        if a == volume_dict[0] and b == volume_dict[8]:
            entry_two.insert(0, entry_one * 264.172)
            
        if a == volume_dict[0] and b == volume_dict[9]:
            entry_two.insert(0, entry_one * 1056.69)

        # Cubic Centimeter to other units
        if a == volume_dict[1] and b == volume_dict[0]:
            entry_two.insert(0, entry_one / 1e6)
            
        if a == volume_dict[1] and b == volume_dict[2]:
            entry_two.insert(0, entry_one * 1000)
            
        if a == volume_dict[1] and b == volume_dict[3]:
            entry_two.insert(0, entry_one / 1000)
            
        if a == volume_dict[1] and b == volume_dict[4]:
            entry_two.insert(0, entry_one)
            
        if a == volume_dict[1] and b == volume_dict[5]:
            entry_two.insert(0, entry_one / 16.387)
            
        if a == volume_dict[1] and b == volume_dict[6]:
            entry_two.insert(0, entry_one / 28316.8)
            
        if a == volume_dict[1] and b == volume_dict[7]:
            entry_two.insert(0, entry_one / 764555)
            
        if a == volume_dict[1] and b == volume_dict[8]:
            entry_two.insert(0, entry_one / 3785.41)
            
        if a == volume_dict[1] and b == volume_dict[9]:
            entry_two.insert(0, entry_one / 946.353)

        # Cubic Millimeter to other units
        if a == volume_dict[2] and b == volume_dict[0]:
            entry_two.insert(0, entry_one / 1e9)
            
        if a == volume_dict[2] and b == volume_dict[1]:
            entry_two.insert(0, entry_one / 1000)
            
        if a == volume_dict[2] and b == volume_dict[3]:
            entry_two.insert(0, entry_one / 1e6)
            
        if a == volume_dict[2] and b == volume_dict[4]:
            entry_two.insert(0, entry_one / 1000)
            
        if a == volume_dict[2] and b == volume_dict[5]:
            entry_two.insert(0, entry_one / 16387.1)
            
        if a == volume_dict[2] and b == volume_dict[6]:
            entry_two.insert(0, entry_one / 2.832e7)
            
        if a == volume_dict[2] and b == volume_dict[7]:
            entry_two.insert(0, entry_one / 7.64555e8)
            
        if a == volume_dict[2] and b == volume_dict[8]:
            entry_two.insert(0, entry_one / 3.78541e6)
            
        if a == volume_dict[2] and b == volume_dict[9]:
            entry_two.insert(0, entry_one / 9.46353e5)

        # Liter to other units
        if a == volume_dict[3] and b == volume_dict[0]:
            entry_two.insert(0, entry_one / 1000)
            
        if a == volume_dict[3] and b == volume_dict[1]:
            entry_two.insert(0, entry_one * 1000)
            
        if a == volume_dict[3] and b == volume_dict[2]:
            entry_two.insert(0, entry_one * 1e6)
            
        if a == volume_dict[3] and b == volume_dict[4]:
            entry_two.insert(0, entry_one * 1000)
            
        if a == volume_dict[3] and b == volume_dict[5]:
            entry_two.insert(0, entry_one * 61.0237)
            
        if a == volume_dict[3] and b == volume_dict[6]:
            entry_two.insert(0, entry_one / 28.3168)
            
        if a == volume_dict[3] and b == volume_dict[7]:
            entry_two.insert(0, entry_one / 764.555)
            
        if a == volume_dict[3] and b == volume_dict[8]:
            entry_two.insert(0, entry_one / 3.78541)
            
        if a == volume_dict[3] and b == volume_dict[9]:
            entry_two.insert(0, entry_one / 0.946353)

        # Milliliter to other units
        if a == volume_dict[4] and b == volume_dict[0]:
            entry_two.insert(0, entry_one / 1e6)
            
        if a == volume_dict[4] and b == volume_dict[1]:
            entry_two.insert(0, entry_one)
            
        if a == volume_dict[4] and b == volume_dict[2]:
            entry_two.insert(0, entry_one * 1000)
            
        if a == volume_dict[4] and b == volume_dict[3]:
            entry_two.insert(0, entry_one / 1000)
            
        if a == volume_dict[4] and b == volume_dict[5]:
            entry_two.insert(0, entry_one / 16.387)
            
        if a == volume_dict[4] and b == volume_dict[6]:
            entry_two.insert(0, entry_one / 28316.8)
            
        if a == volume_dict[4] and b == volume_dict[7]:
            entry_two.insert(0, entry_one / 764555)
            
        if a == volume_dict[4] and b == volume_dict[8]:
            entry_two.insert(0, entry_one / 3785.41)
            
        if a == volume_dict[4] and b == volume_dict[9]:
            entry_two.insert(0, entry_one / 946.353)

        # Cubic Inch to other units
        if a == volume_dict[5] and b == volume_dict[0]:
            entry_two.insert(0, entry_one / 61023.7)
            
        if a == volume_dict[5] and b == volume_dict[1]:
            entry_two.insert(0, entry_one * 16.3871)
            
        if a == volume_dict[5] and b == volume_dict[2]:
            entry_two.insert(0, entry_one * 16387.1)
            
        if a == volume_dict[5] and b == volume_dict[3]:
            entry_two.insert(0, entry_one / 61.0237)
            
        if a == volume_dict[5] and b == volume_dict[4]:
            entry_two.insert(0, entry_one * 16.3871)
            
        if a == volume_dict[5] and b == volume_dict[6]:
            entry_two.insert(0, entry_one / 1728)
            
        if a == volume_dict[5] and b == volume_dict[7]:
            entry_two.insert(0, entry_one / 46656)
            
        if a == volume_dict[5] and b == volume_dict[8]:
            entry_two.insert(0, entry_one / 231)
            
        if a == volume_dict[5] and b == volume_dict[9]:
            entry_two.insert(0, entry_one / 57.75)

        # Cubic Foot to other units
        if a == volume_dict[6] and b == volume_dict[0]:
            entry_two.insert(0, entry_one / 35.3147)
            
        if a == volume_dict[6] and b == volume_dict[1]:
            entry_two.insert(0, entry_one * 28316.8)
            
        if a == volume_dict[6] and b == volume_dict[2]:
            entry_two.insert(0, entry_one * 2.832e7)
            
        if a == volume_dict[6] and b == volume_dict[3]:
            entry_two.insert(0, entry_one * 28.3168)
            
        if a == volume_dict[6] and b == volume_dict[4]:
            entry_two.insert(0, entry_one * 28316.8)
            
        if a == volume_dict[6] and b == volume_dict[5]:
            entry_two.insert(0, entry_one * 1728)
            
        if a == volume_dict[6] and b == volume_dict[7]:
            entry_two.insert(0, entry_one / 27)
            
        if a == volume_dict[6] and b == volume_dict[8]:
            entry_two.insert(0, entry_one * 7.48052)
            
        if a == volume_dict[6] and b == volume_dict[9]:
            entry_two.insert(0, entry_one * 29.9221)

        # Cubic Yard to other units
        if a == volume_dict[7] and b == volume_dict[0]:
            entry_two.insert(0, entry_one / 1.30795)
            
        if a == volume_dict[7] and b == volume_dict[1]:
            entry_two.insert(0, entry_one * 764555)
            
        if a == volume_dict[7] and b == volume_dict[2]:
            entry_two.insert(0, entry_one * 7.64555e8)
            
        if a == volume_dict[7] and b == volume_dict[3]:
            entry_two.insert(0, entry_one * 764.555)
            
        if a == volume_dict[7] and b == volume_dict[4]:
            entry_two.insert(0, entry_one * 764555)
            
        if a == volume_dict[7] and b == volume_dict[5]:
            entry_two.insert(0, entry_one * 46656)
            
        if a == volume_dict[7] and b == volume_dict[6]:
            entry_two.insert(0, entry_one * 27)
            
        if a == volume_dict[7] and b == volume_dict[8]:
            entry_two.insert(0, entry_one * 201.974)
            
        if a == volume_dict[7] and b == volume_dict[9]:
            entry_two.insert(0, entry_one * 807.896)

        # Gallon to other units
        if a == volume_dict[8] and b == volume_dict[0]:
            entry_two.insert(0, entry_one / 264.172)
            
        if a == volume_dict[8] and b == volume_dict[1]:
            entry_two.insert(0, entry_one * 3785.41)
            
        if a == volume_dict[8] and b == volume_dict[2]:
            entry_two.insert(0, entry_one * 3.78541e6)
            
        if a == volume_dict[8] and b == volume_dict[3]:
            entry_two.insert(0, entry_one * 3.78541)
            
        if a == volume_dict[8] and b == volume_dict[4]:
            entry_two.insert(0, entry_one * 3785.41)
            
        if a == volume_dict[8] and b == volume_dict[5]:
            entry_two.insert(0, entry_one * 231)
            
        if a == volume_dict[8] and b == volume_dict[6]:
            entry_two.insert(0, entry_one / 7.48052)
            
        if a == volume_dict[8] and b == volume_dict[7]:
            entry_two.insert(0, entry_one / 201.974)
            
        if a == volume_dict[8] and b == volume_dict[9]:
            entry_two.insert(0, entry_one * 4)

        # Quart to other units
        if a == volume_dict[9] and b == volume_dict[0]:
            entry_two.insert(0, entry_one / 1056.69)
            
        if a == volume_dict[9] and b == volume_dict[1]:
            entry_two.insert(0, entry_one * 946.353)
            
        if a == volume_dict[9] and b == volume_dict[2]:
            entry_two.insert(0, entry_one * 946353)
            
        if a == volume_dict[9] and b == volume_dict[3]:
            entry_two.insert(0, entry_one / 1.05669)
            
        if a == volume_dict[9] and b == volume_dict[4]:
            entry_two.insert(0, entry_one * 946.353)
            
        if a == volume_dict[9] and b == volume_dict[5]:
            entry_two.insert(0, entry_one * 57.75)
            
        if a == volume_dict[9] and b == volume_dict[6]:
            entry_two.insert(0, entry_one / 29.9221)
            
        if a == volume_dict[9] and b == volume_dict[7]:
            entry_two.insert(0, entry_one / 807.896)
            
        if a == volume_dict[9] and b == volume_dict[8]:
            entry_two.insert(0, entry_one / 4)
        
    
    def convert_length():
        a = combo_one.get()
        b = combo_two.get()
        entry_one = entry_one_var.get()

        delete_entry()

        # Meter to other units
        if a == length_dict[0] and b == length_dict[1]:
            entry_two.insert(0, entry_one / 1000)
            
        if a == length_dict[0] and b == length_dict[2]:
            entry_two.insert(0, entry_one * 100)
            
        if a == length_dict[0] and b == length_dict[3]:
            entry_two.insert(0, entry_one * 1000)
            
        if a == length_dict[0] and b == length_dict[4]:
            entry_two.insert(0, entry_one * 1e6)
            
        if a == length_dict[0] and b == length_dict[5]:
            entry_two.insert(0, entry_one * 1e9)
            
        if a == length_dict[0] and b == length_dict[6]:
            entry_two.insert(0, entry_one / 1609.34)
            
        if a == length_dict[0] and b == length_dict[7]:
            entry_two.insert(0, entry_one * 1.09361)
            
        if a == length_dict[0] and b == length_dict[8]:
            entry_two.insert(0, entry_one * 3.28084)
            
        if a == length_dict[0] and b == length_dict[9]:
            entry_two.insert(0, entry_one * 39.3701)

        # Kilometer to other units
        if a == length_dict[1] and b == length_dict[0]:
            entry_two.insert(0, entry_one * 1000)
            
        if a == length_dict[1] and b == length_dict[2]:
            entry_two.insert(0, entry_one * 1e5)
            
        if a == length_dict[1] and b == length_dict[3]:
            entry_two.insert(0, entry_one * 1e6)
            
        if a == length_dict[1] and b == length_dict[4]:
            entry_two.insert(0, entry_one * 1e9)
            
        if a == length_dict[1] and b == length_dict[5]:
            entry_two.insert(0, entry_one * 1e12)
            
        if a == length_dict[1] and b == length_dict[6]:
            entry_two.insert(0, entry_one / 1.60934)
            
        if a == length_dict[1] and b == length_dict[7]:
            entry_two.insert(0, entry_one * 1093.61)
            
        if a == length_dict[1] and b == length_dict[8]:
            entry_two.insert(0, entry_one * 3280.84)
            
        if a == length_dict[1] and b == length_dict[9]:
            entry_two.insert(0, entry_one * 39370.1)

        # Centimeter to other units
        if a == length_dict[2] and b == length_dict[0]:
            entry_two.insert(0, entry_one / 100)
            
        if a == length_dict[2] and b == length_dict[1]:
            entry_two.insert(0, entry_one / 1e5)
            
        if a == length_dict[2] and b == length_dict[3]:
            entry_two.insert(0, entry_one * 10)
            
        if a == length_dict[2] and b == length_dict[4]:
            entry_two.insert(0, entry_one * 1e4)
            
        if a == length_dict[2] and b == length_dict[5]:
            entry_two.insert(0, entry_one * 1e7)
            
        if a == length_dict[2] and b == length_dict[6]:
            entry_two.insert(0, entry_one / 160934)
            
        if a == length_dict[2] and b == length_dict[7]:
            entry_two.insert(0, entry_one / 91.44)
            
        if a == length_dict[2] and b == length_dict[8]:
            entry_two.insert(0, entry_one / 30.48)
            
        if a == length_dict[2] and b == length_dict[9]:
            entry_two.insert(0, entry_one / 2.54)

        # Millimeter to other units
        if a == length_dict[3] and b == length_dict[0]:
            entry_two.insert(0, entry_one / 1000)
            
        if a == length_dict[3] and b == length_dict[1]:
            entry_two.insert(0, entry_one / 1e6)
            
        if a == length_dict[3] and b == length_dict[2]:
            entry_two.insert(0, entry_one / 10)
            
        if a == length_dict[3] and b == length_dict[4]:
            entry_two.insert(0, entry_one * 1000)
            
        if a == length_dict[3] and b == length_dict[5]:
            entry_two.insert(0, entry_one * 1e6)
            
        if a == length_dict[3] and b == length_dict[6]:
            entry_two.insert(0, entry_one / 1.609e6)
            
        if a == length_dict[3] and b == length_dict[7]:
            entry_two.insert(0, entry_one / 914.4)
            
        if a == length_dict[3] and b == length_dict[8]:
            entry_two.insert(0, entry_one / 304.8)
            
        if a == length_dict[3] and b == length_dict[9]:
            entry_two.insert(0, entry_one / 25.4)

        # Micrometer to other units
        if a == length_dict[4] and b == length_dict[0]:
            entry_two.insert(0, entry_one / 1e6)
            
        if a == length_dict[4] and b == length_dict[1]:
            entry_two.insert(0, entry_one / 1e9)
            
        if a == length_dict[4] and b == length_dict[2]:
            entry_two.insert(0, entry_one / 1e4)
            
        if a == length_dict[4] and b == length_dict[3]:
            entry_two.insert(0, entry_one / 1000)
            
        if a == length_dict[4] and b == length_dict[5]:
            entry_two.insert(0, entry_one * 1000)
            
        if a == length_dict[4] and b == length_dict[6]:
            entry_two.insert(0, entry_one / 1.609e9)
            
        if a == length_dict[4] and b == length_dict[7]:
            entry_two.insert(0, entry_one / 914400)
            
        if a == length_dict[4] and b == length_dict[8]:
            entry_two.insert(0, entry_one / 304800)
            
        if a == length_dict[4] and b == length_dict[9]:
            entry_two.insert(0, entry_one / 25400)

        # Nanometer to other units
        if a == length_dict[5] and b == length_dict[0]:
            entry_two.insert(0, entry_one / 1e9)
            
        if a == length_dict[5] and b == length_dict[1]:
            entry_two.insert(0, entry_one / 1e12)
            
        if a == length_dict[5] and b == length_dict[2]:
            entry_two.insert(0, entry_one / 1e7)
            
        if a == length_dict[5] and b == length_dict[3]:
            entry_two.insert(0, entry_one / 1e6)
            
        if a == length_dict[5] and b == length_dict[4]:
            entry_two.insert(0, entry_one / 1000)
            
        if a == length_dict[5] and b == length_dict[6]:
            entry_two.insert(0, entry_one / 1.609e12)
            
        if a == length_dict[5] and b == length_dict[7]:
            entry_two.insert(0, entry_one / 9.144e8)
            
        if a == length_dict[5] and b == length_dict[8]:
            entry_two.insert(0, entry_one / 3.048e8)
            
        if a == length_dict[5] and b == length_dict[9]:
            entry_two.insert(0, entry_one / 2.54e7)

        # Mile to other units
        if a == length_dict[6] and b == length_dict[0]:
            entry_two.insert(0, entry_one * 1609.34)
            
        if a == length_dict[6] and b == length_dict[1]:
            entry_two.insert(0, entry_one * 1.60934)
            
        if a == length_dict[6] and b == length_dict[2]:
            entry_two.insert(0, entry_one * 160934)
            
        if a == length_dict[6] and b == length_dict[3]:
            entry_two.insert(0, entry_one * 1.609e6)
            
        if a == length_dict[6] and b == length_dict[4]:
            entry_two.insert(0, entry_one * 1.609e9)
            
        if a == length_dict[6] and b == length_dict[5]:
            entry_two.insert(0, entry_one * 1.609e12)
            
        if a == length_dict[6] and b == length_dict[7]:
            entry_two.insert(0, entry_one * 1760)
            
        if a == length_dict[6] and b == length_dict[8]:
            entry_two.insert(0, entry_one * 5280)
            
        if a == length_dict[6] and b == length_dict[9]:
            entry_two.insert(0, entry_one * 63360)

        # Yard to other units
        if a == length_dict[7] and b == length_dict[0]:
            entry_two.insert(0, entry_one / 1.09361)
            
        if a == length_dict[7] and b == length_dict[1]:
            entry_two.insert(0, entry_one / 1093.61)
            
        if a == length_dict[7] and b == length_dict[2]:
            entry_two.insert(0, entry_one * 91.44)
            
        if a == length_dict[7] and b == length_dict[3]:
            entry_two.insert(0, entry_one * 914.4)
            
        if a == length_dict[7] and b == length_dict[4]:
            entry_two.insert(0, entry_one * 914400)
            
        if a == length_dict[7] and b == length_dict[5]:
            entry_two.insert(0, entry_one * 9.144e8)
            
        if a == length_dict[7] and b == length_dict[6]:
            entry_two.insert(0, entry_one / 1760)
            
        if a == length_dict[7] and b == length_dict[8]:
            entry_two.insert(0, entry_one * 3)
            
        if a == length_dict[7] and b == length_dict[9]:
            entry_two.insert(0, entry_one * 36)

        # Foot to other units
        if a == length_dict[8] and b == length_dict[0]:
            entry_two.insert(0, entry_one / 3.28084)
            
        if a == length_dict[8] and b == length_dict[1]:
            entry_two.insert(0, entry_one / 3280.84)
            
        if a == length_dict[8] and b == length_dict[2]:
            entry_two.insert(0, entry_one * 30.48)
            
        if a == length_dict[8] and b == length_dict[3]:
            entry_two.insert(0, entry_one * 304.8)
            
        if a == length_dict[8] and b == length_dict[4]:
            entry_two.insert(0, entry_one * 304800)
            
        if a == length_dict[8] and b == length_dict[5]:
            entry_two.insert(0, entry_one * 3.048e8)
            
        if a == length_dict[8] and b == length_dict[6]:
            entry_two.insert(0, entry_one / 5280)
            
        if a == length_dict[8] and b == length_dict[7]:
            entry_two.insert(0, entry_one / 3)
            
        if a == length_dict[8] and b == length_dict[9]:
            entry_two.insert(0, entry_one * 12)

        # Inch to other units
        if a == length_dict[9] and b == length_dict[0]:
            entry_two.insert(0, entry_one / 39.3701)
            
        if a == length_dict[9] and b == length_dict[1]:
            entry_two.insert(0, entry_one / 39370.1)
            
        if a == length_dict[9] and b == length_dict[2]:
            entry_two.insert(0, entry_one * 2.54)
            
        if a == length_dict[9] and b == length_dict[3]:
            entry_two.insert(0, entry_one * 25.4)
            
        if a == length_dict[9] and b == length_dict[4]:
            entry_two.insert(0, entry_one * 25400)
            
        if a == length_dict[9] and b == length_dict[5]:
            entry_two.insert(0, entry_one * 2.54e7)
            
        if a == length_dict[9] and b == length_dict[6]:
            entry_two.insert(0, entry_one / 63360)
            
        if a == length_dict[9] and b == length_dict[7]:
            entry_two.insert(0, entry_one / 36)
            
        if a == length_dict[9] and b == length_dict[8]:
            entry_two.insert(0, entry_one / 12)
    
    
    
    def convert(event):
        if combo_options.get() == "weight":
            convert_weight()
        elif combo_options.get() == "velocity":
            convert_velocity()
        elif combo_options.get() == "volume":
            convert_volume()
        else: # length option
            convert_length()
        
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




