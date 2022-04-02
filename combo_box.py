from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("300x200")


# Load = Spring Rate * deflection (L = R * DT) 


var = StringVar()
com = ttk.Combobox(root,width=15,state='readonly')    #state can write here or
com.grid(row=1,column=1)
# com['state'] = 'readonly'                                   #state can write here
com['value'] = ('Select','Load (L)','Spring Rate (R)','Deflection (DT)')

com.current(0)          # this is for value shown in combobox value count from 0,1,2,3 so on 



root.mainloop()