from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Compression Spring Calculation")
root.geometry("400x600")

# def multiply (x*y)

# Load = Spring Rate * deflection          (L = R * DT) 

rate = Label(text="Spring Rate (R)")
rate.grid(row=0,column=0)

entry = Entry(bd="2")
entry.grid(row=0,column=2)


rate = Label(text="deflection/Distance Traveled (DT)")
rate.grid(row=1,column=0)

entry = Entry(bd="2")
entry.grid(row=1,column=2)




entry = Entry(bd="2")
entry.grid(row=3,column=2)


# var = StringVar()
# com = ttk.Combobox(root,width=15,state='readonly')    #state can write here or
# com.grid(row=3,column=1)
# # com['state'] = 'readonly'                                   #state can write here
# com['value'] = ('Select','Load (L)','Spring Rate (R)','Deflection (DT)')

# com.current(0)     


button = Button(text="Find Value",bg="green",bd="2")
button.grid(row=4,column=1)


root.mainloop()