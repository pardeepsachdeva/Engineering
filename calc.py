from tkinter import *


root=Tk()

root.geometry("600x500")
root.maxsize(600,500)
root.minsize(600,500) 


e = entry = Entry(bg="#ffead5",fg="Black", font="Archivo",bd=10,width=42) #height="50")
e.place(x=90,y=10)


def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0,END)

def button_sum ():
    first_number = e.get()
    global f_num 
    f_num = int(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    e.insert(0,f_num + int(second_number))





button_9 = Button(text="9",width=10,height=5,bg="#bdbcba",command=lambda: button_click(9))  #.....9
button_9.place(x=90,y=60)

button_8 = Button(text="8",width=10,height=5,bg="#bdbcba",command=lambda: button_click(8))  #.....8
button_8.place(x=180,y=60)

button_7 = Button(text="7",width=10,height=5,bg="#bdbcba",command=lambda: button_click(7))  #.....7
button_7.place(x=270,y=60)

button_6 = Button(text="6",width=10,height=5,bg="#bdbcba",command=lambda: button_click(6))  #........6
button_6.place(x=90,y=160)

button_5 = Button(text="5",width=10,height=5,bg="#bdbcba",command=lambda: button_click(5)) #........5
button_5.place(x=180,y=160)

button_4 = Button(text="4",width=10,height=5,bg="#bdbcba",command=lambda: button_click(4)) #........4
button_4.place(x=270,y=160)

button_3 = Button(text="3",width=10,height=5,bg="#bdbcba",command=lambda: button_click(3)) #........3
button_3.place(x=90,y=260)

button_2 = Button(text="2",width=10,height=5,bg="#bdbcba",command=lambda: button_click(2)) #........2
button_2.place(x=180,y=260)

button_1 = Button(text="1",width=10,height=5,bg="#bdbcba",command=lambda: button_click(1)) #........1
button_1.place(x=270,y=260)

button_0 = Button(text="0",width=10,height=5,bg="#bdbcba",command=lambda: button_click(0)) #........0
button_0.place(x=90,y=360)



# ..........................................................................


button_equal = Button(text="=",width=23,height=5,bg="#c9d8f8",command=button_equal) #........=
button_equal.place(x=180,y=360)

button = Button(text="DIV (/)",width=10,height=5,bg="#fbeab0")  #...../
button.place(x=360,y=60)

button = Button(text="MUL (X)",width=10,height=5,bg="#fbeab0")  #.....*
button.place(x=360,y=260)


button_sum = Button(text="SUM (+)",width=10,height=11,bg="#fbeab0",command=button_sum) #........+
button_sum.place(x=450,y=270)

button = Button(text="PER (%)",width=10,height=5,bg="#fbeab0") #........%
button.place(x=360,y=160)

button = Button(text="SUN (-)",width=10,height=5,bg="#fbeab0") #........-
button.place(x=360,y=360)

button = Button(text="CLEAR",width=10,height=6,bg="#c9545a",command=button_clear) #........CLEAR
button.place(x=450,y=160)

button_DEL = Button(text="DEL",width=10,height=5,bg="#fcc0c3")  #.....DEL
button_DEL.place(x=450,y=60)

# ........................................................................


# button = Button(text="SUN (-)",width=10,height=5)
# button.place(x=540,y=260)



root.mainloop()