from tkinter import *

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


button = Button(text="Load Value (L)",bg="green",bd="2")
button.grid(row=3,column=1)

entry = Entry(bd="2")
entry.grid(row=3,column=2)



root.mainloop()