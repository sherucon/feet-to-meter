from tkinter import *
from tkinter import ttk             #importing required packages

def feetMeter():
    value=float(feet.get())     #operations for actual conversion
    meters.set(str(value*0.305))

root = Tk()            #declaring app
root.title('Feet to Meter Converter')           #renaming app window

mainframe = ttk.Frame(root,padding='12 12 12 12')             #initializing mainframe
mainframe.grid(column=0,row=0,sticky=(N,E,W,S))
root.columnconfigure(0)
root.rowconfigure(0)

ttk.Label(mainframe, text="feet").grid(column=2,row=0,sticky=(W,E))         #display "feet"
ttk.Label(mainframe, text="is equal to").grid(column=0,row=1,sticky=(E))    #display "is equal to"
ttk.Label(mainframe, text="meters").grid(column=2,row=1,sticky=(W))         #display "meters"

meters=StringVar()
ttk.Label(mainframe, width=7, textvariable=meters).grid(column=1,row=1,sticky=(W,E))             #display result

feet=StringVar()
ttk.Entry(mainframe, width=7, textvariable=feet).grid(column=1,row=0,sticky=(W,E))             #taking input in text field

calculate_button=ttk.Button(mainframe, text="calculate", command=feetMeter)          #making calculate trigger
calculate_button.grid(column=2,row=2,sticky=(W,E))


root.mainloop()        #looping app