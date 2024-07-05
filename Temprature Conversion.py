import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def convert_temperature():
    try:
        value = float(entry_value.get())
        unit = combo_unit.get()
        
        if unit == 'C':
            fahrenheit = celsius_to_fahrenheit(value)
            kelvin = celsius_to_kelvin(value)
            label_result.config(text=f"{value}°C is {fahrenheit:.2f}°F and {kelvin:.2f}K")
        elif unit == 'F':
            celsius = fahrenheit_to_celsius(value)
            kelvin = fahrenheit_to_kelvin(value)
            label_result.config(text=f"{value}°F is {celsius:.2f}°C and {kelvin:.2f}K")
        elif unit == 'K':
            celsius = kelvin_to_celsius(value)
            fahrenheit = kelvin_to_fahrenheit(value)
            label_result.config(text=f"{value}K is {celsius:.2f}°C and {fahrenheit:.2f}°F")
        else:
            label_result.config(text="Invalid unit. Please select C, F, or K.")
    except ValueError:
        label_result.config(text="Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Temperature Conversion")

# Set the size of the main window
root.geometry("400x250")

# Create and style the frame
frame = ttk.Frame(root, padding="20")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create and place the widgets
label_value = ttk.Label(frame, text="Enter the temperature value:", font=("Helvetica", 12))
label_value.grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)

entry_value = ttk.Entry(frame, font=("Helvetica", 12))
entry_value.grid(column=1, row=0, padx=10, pady=10, sticky=(tk.W, tk.E))

label_unit = ttk.Label(frame, text="Select the unit of measurement:", font=("Helvetica", 12))
label_unit.grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)

combo_unit = ttk.Combobox(frame, values=["C", "F", "K"], font=("Helvetica", 12))
combo_unit.grid(column=1, row=1, padx=10, pady=10, sticky=(tk.W, tk.E))
combo_unit.set("C")  # Default value

button_convert = ttk.Button(frame, text="Convert", command=convert_temperature, style="TButton")
button_convert.grid(column=0, row=2, columnspan=2, padx=10, pady=20)

label_result = ttk.Label(frame, text="", font=("Helvetica", 12))
label_result.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Configure column and row weights
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.rowconfigure(3, weight=1)

# Style the button
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=6)

# Start the main event loop
root.mainloop()
