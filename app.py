from tkinter import *
from tkinter import ttk

def feetMeter():
    value=float(feet.get())
    meters.set(str(value*0.305))

root = Tk()
root.title('Feet to Meter Converter')

mainframe = ttk.Frame(root,padding='12 12 12 12')
mainframe.grid(column=0,row=0,sticky=(N,E,W,S))
root.columnconfigure(0)
root.rowconfigure(0)

ttk.Label(mainframe, text="feet").grid(column=2,row=0,sticky=(W,E))
ttk.Label(mainframe, text="is equal to").grid(column=0,row=1,sticky=(E))
ttk.Label(mainframe, text="meters").grid(column=2,row=1,sticky=(W))

meters=StringVar()
ttk.Label(mainframe, width=7, textvariable=meters).grid(column=1,row=1,sticky=(W,E))

feet=StringVar()
ttk.Entry(mainframe, width=7, textvariable=feet).grid(column=1,row=0,sticky=(W,E))

calculate_button=ttk.Button(mainframe, text="calculate", command=feetMeter)
calculate_button.grid(column=2,row=2,sticky=(W,E))


root.mainloop()