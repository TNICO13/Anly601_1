import requests, json      # Used to request information from a website
#from tkinter import *     # Alternate approach to creating the GUI canvas
import tkinter as tk       # Used to pull original tkinter objects
from   tkinter import ttk  # Used for new Theme'd Objects

base_url = "https://www.alphavantage.co/query?function="
query   = "GLOBAL_QUOTE"
symbol  = "IBM"
api_key = "IZHAYZFSN4A3I5OY"

url = base_url + query + "&symbol=" + symbol + "&apikey=" + api_key
print("Request Sent to: \n", url, '\n')
r    = requests.get(url)
data = r.json()

#print Alpha Vantage data dictionary
print("Alpha Vantage Returned Data:\n", data, "\n")
#print "Global Quote" Dictionary Contents
print("Global Quote Contents:\n", data["Global Quote"],"\n")

#Extract Stock Values from Global Quote
symbol = data["Global Quote"]["01. symbol"]#Extract stock symbol
high   = data["Global Quote"]["03. high"]  #Extract highest price
price  = data["Global Quote"]["05. price"] #Extract closing price
day    = data["Global Quote"]["07. latest trading day"] #Trading Day
print(symbol, day, high, price, "\n")

root  = tk.Tk()
root.title(symbol + " Stock Price")
root.geometry('200x200+1000+300') #Set Window Size (WxH) & Location (+X+Y)

stock_label = ttk.Label(root, text = "Stock:").\
                        grid(row=0, column=0, sticky="w")
stock_symbol = tk.StringVar()
stock_symbol.set(symbol)
stock_entry  = ttk.Entry(root, textvariable=stock_symbol, width=10, 
               font="Arial, 18", justify='center').grid(row=0, column=1)

stock_high = ttk.Label(root, text = "Price High:").\
                        grid(row=1, column=0, sticky="w")
stock_high = tk.StringVar()
stock_high.set(price)
stock_entry  = ttk.Entry(root, textvariable=stock_high, width=10,
               font="Arial, 18", justify='center').grid(row=1, column=1)

root.mainloop()
