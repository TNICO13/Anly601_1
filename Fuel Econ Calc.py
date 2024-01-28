import requests  #Used to request information from a website
import tkinter as tk       # Used to pull original tkinter objects
from   tkinter import ttk  # Used for new Theme'd Objects
# from tkinter import *     # Alternate approach to creating the GUI canvas
import tkinter as tk  # Used to pull original tkinter objects
from tkinter import ttk  # Used for new Theme'd Objects
import ttkthemes

def Calculate():
    Miles_Driven = float(Miles_Driven_Label.get())
    Fuel_Consumption = float(Fuel_Consumption_Label.get())
    MPG = round(float(Miles_Driven / Fuel_Consumption), 2)
    MPG_Label.set(MPG)

Miles_Driven = float(12)
Fuel_Consumption = float(3)
MPG = float(Miles_Driven / Fuel_Consumption)


root  = tk.Tk()
root.configure(bg='white')
root.title("Fuel Economy Calculator")
root.geometry('380x200+1000+300') #Set Window Size (WxH) & Location (+X+Y)
style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", foreground="maroon", background="white", font="Arial, 15")
style.configure("TEntry", fieldbackground='maroon', foreground="white")
style.configure("TLabel", background='white')


Miles_Driven_Label = ttk.Label(root, text = "Miles Driven:").grid(row=0, column=0, sticky="w")
Miles_Driven_Label = tk.StringVar()
Miles_Driven_Label.set(Miles_Driven)
entry  = ttk.Entry(root, textvariable=Miles_Driven_Label, width=10,font="Arial, 18", justify='right').grid(row=0, column=2)


Fuel_Consumption_Label = ttk.Label(root, text = "Fuel Consumption:").grid(row=1, column=0, sticky="w")
Fuel_Consumption_Label = tk.StringVar()
Fuel_Consumption_Label.set(Fuel_Consumption)
entry  = ttk.Entry(root, textvariable=Fuel_Consumption_Label, width=10, font="Arial, 18", justify='right').grid(row=1, column=2)

frame_break = ttk.Frame(root, height=2, relief="sunken", borderwidth=1)
frame_break.grid(row=3, column=0, sticky="ew", pady=5)

frame_break = ttk.Frame(root, height=2, relief="sunken", borderwidth=1)
frame_break.grid(row=3, column=1, sticky="ew", pady=5)

frame_break = ttk.Frame(root, height=2, relief="sunken", borderwidth=1)
frame_break.grid(row=3, column=2, sticky="ew", pady=5)

spacer_frame = ttk.Frame(root, width=20, height=10, style="TLabel")  # Width is the space width
spacer_frame.grid(row=4, column=1)

MPG_Label = ttk.Label(root, text = "MPG:", anchor='e').grid(row=2, column=1)
MPG_Label = tk.StringVar()
MPG_Label.set(MPG)
entry  = ttk.Entry(root, textvariable=MPG_Label, width=10, font="Arial, 18", justify='right').grid(row=2, column=2)

calculate_button = ttk.Button(root, text="Calculate", command=Calculate).grid(row=5, column=1)


root.mainloop()