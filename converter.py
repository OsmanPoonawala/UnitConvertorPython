import tkinter as tk
from tkinter import *
from tkinter import ttk


root = tk.Tk()
root.title('Unit Conversion Tool')
screenW = root.winfo_screenwidth()/2 - 175
screenH = root.winfo_screenheight()/2 - 250
screenResolution = "345x500+" + str(screenW) + "+" + str(screenH)
root.geometry(screenResolution)
root.resizable(width=False, height=False)
root.configure(bg='#cccccc')

typeConversion = ['Length', 'Area', 'Mass', 'Temperature']

conversionOptions = [['Kilometer', 'Meter', 'Centimeter', 'Milimeter',
                      'Mile', 'Inch', 'Foot'],
                     ['Sq Kilometer', 'Sq Meter', 'Sq Mile',
                      'Sq Foot', 'Sq Inch', 'Acre'],
                     ['Tonne', 'Kilogram', 'Gram', 'Miligram', 'Pound'],
                     ['Celsius', 'Fahrenheit', 'Kalvin']]

lengthConversions = {
    "Kilometer": {"Kilometer": 1, "Meter": 1000, "Centimeter": 100000,
                  "Milimeter": 1000000, "Mile": 1/1.609, "Inch": 39370, "Foot": 3281},
    "Meter": {"Kilometer": 1/1000, "Meter": 1, "Centimeter": 100,
              "Milimeter": 1000, "Mile": 1/1609, "Inch": 39.37, "Foot": 3.281},
    "Centimeter": {"Kilometer": 1/100000, "Meter": 1/100, "Centimeter": 1,
                   "Milimeter": 10, "Mile": 1/160934, "Inch": 1/2.54, "Foot": 1/30.48},
    "Milimeter": {"Kilometer": 1/1000000, "Meter": 1/1000, "Centimeter": 1/10,
                  "Milimeter": 1, "Mile": 1/1609340, "Inch": 1/25.4, "Foot": 1/305},
    "Mile": {"Kilometer": 1.609, "Meter": 1609, "Centimeter": 160934,
             "Milimeter": 1609340, "Mile": 1, "Inch": 63360, "Foot": 5280},
    "Inch": {"Kilometer": 1/39370, "Meter": 1/39.37, "Centimeter": 2.54,
             "Milimeter": 25.4, "Mile": 1/63360, "Inch": 1, "Foot": 1/12},
    "Foot": {"Kilometer": 1/3281, "Meter": 1/3.281, "Centimeter": 30.48,
             "Milimeter": 304.8, "Mile": 1/5280, "Inch": 12, "Foot": 1}
}

areaConversions = {
    "Sq Kilometer": {"Sq Kilometer": 1, "Sq Meter": 1000000, "Sq Mile": 1/2.59,
                     "Sq Foot": 10760000, "Sq Inch": 1550000000, "Acre": 247},
    "Sq Meter": {"Sq Kilometer": 1/1000000, "Sq Meter": 1, "Sq Mile": 1/2590000,
                 "Sq Foot": 10.764, "Sq Inch": 1550, "Acre": 1/4047},
    "Sq Mile": {"Sq Kilometer": 2.59, "Sq Meter": 2590000, "Sq Mile": 1,
                "Sq Foot": 27880000, "Sq Inch": 4014000000, "Acre": 640},
    "Sq Foot": {"Sq Kilometer": 1/10760000, "Sq Meter": 1/10.764, "Sq Mile": 1/27880000,
                "Sq Foot": 1, "Sq Inch": 144, "Acre": 1/43560},
    "Sq Inch": {"Sq Kilometer": 1/1550000000, "Sq Meter": 1/1550, "Sq Mile": 1/4014000000,
                "Sq Foot": 1/144, "Sq Inch": 1, "Acre": 1/6273000},
    "Acre": {"Sq Kilometer": 1/247, "Sq Meter": 4047, "Sq Mile": 1/640,
             "Sq Foot": 43560, "Sq Inch": 6273000, "Acre": 1}
}

massConversion = {
    "Tonne": {"Tonne": 1, "Kilogram": 1000,
              "Gram": 1000000, "Miligram": 100000000, "Pound": 2205},
    "Kilogram": {"Tonne": 1/1000, "Kilogram": 1,
                 "Gram": 1000, "Miligram": 1000000, "Pound": 2.205},
    "Gram": {"Tonne": 1/1000000, "Kilogram": 1/1000,
             "Gram": 1, "Miligram": 1000, "Pound": 1/454},
    "Miligram": {"Tonne": 1/1000000000, "Kilogram": 1/1000000,
                 "Gram": 1/1000, "Miligram": 1, "Pound": 1/453592},
    "Pound": {"Tonne": 1/2205, "Kilogram": 1/2.205,
              "Gram": 454, "Miligram": 453592, "Pound": 1}
}


def clearOptions(eventObject):
    firstDrop.set('')
    secondDrop.set('')


typeLabel = Label(root, text='Please select type of conversion', bg='#cccccc')
typeLabel.grid(row=0, column=1, columnspan=2)
typeDrop = ttk.Combobox(root, width=40, value=(typeConversion))
typeDrop.set(typeConversion[0])
typeDrop.grid(row=1, column=1, columnspan=2)
typeDrop.bind("<<ComboboxSelected>>", clearOptions)


def callback(eventObject):
    abc = eventObject.widget.get()
    typeSelected = typeDrop.get()
    index = typeConversion.index(typeSelected)
    firstDrop.config(values=conversionOptions[index])
    secondDrop.config(values=conversionOptions[index])


def calculateConversion(conversionType, from_unit_type, to_unit_type, value):
    val = float(value)
    if conversionType == 'Length':
        from_type_units = lengthConversions[from_unit_type][to_unit_type]
        new_value = val * float(from_type_units)
    if conversionType == 'Area':
        from_type_units = areaConversions[from_unit_type][to_unit_type]
        new_value = val * float(from_type_units)
    if conversionType == 'Mass':
        from_type_units = massConversion[from_unit_type][to_unit_type]
        new_value = val * float(from_type_units)
    if conversionType == 'Temperature':
        new_value = convertTemperature(from_unit_type, to_unit_type, val)

    outLabel.configure(text=new_value)


def convertTemperature(from_unit_type, to_unit_type, value):
    if from_unit_type == 'Celsius':
        if to_unit_type == 'Celsius':
            return value
        if to_unit_type == 'Fahrenheit':
            ret = (value * (9/5)) + 32
            return ret
        if to_unit_type == 'Kalvin':
            ret = value + 273.15
            return ret
    if from_unit_type == 'Fahrenheit':
        if to_unit_type == 'Celsius':
            ret = (value - 32) * (5/9)
            return ret
        if to_unit_type == 'Fahrenheit':
            return value
        if to_unit_type == 'Kalvin':
            ret = ((value - 32) * (5/9)) + 273.15
            return ret
    if from_unit_type == 'Kalvin':
        if to_unit_type == 'Celsius':
            ret = value - 273.15
            return ret
        if to_unit_type == 'Fahrenheit':
            ret = (value - 273.15) * (9/5) + 32
            return ret
        if to_unit_type == 'Kalvin':
            return value


firstDrop = ttk.Combobox(root, width=18)
firstDrop.grid(row=2, column=1, columnspan=1)
firstDrop.bind('<Button-1>', callback)

secondDrop = ttk.Combobox(root, width=18)
secondDrop.grid(row=2, column=2, columnspan=1)
secondDrop.bind('<Button-1>', callback)

inputLabel = Label(root, text='Please enter value to covert: ', bg='#cccccc')
inputLabel.grid(row=3, column=1, columnspan=2)

valueEntry = Entry(root)
valueEntry.grid(row=4, column=1, columnspan=1)

submitButton = Button(root, text="Submit", command=lambda: calculateConversion(
    typeDrop.get(), firstDrop.get(), secondDrop.get(), valueEntry.get()))
submitButton.grid(row=4, column=2)

outLabel = Label(root, text='', bg='#cccccc')
outLabel.grid(row=5, column=1, columnspan=2)

root.mainloop()
