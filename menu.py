from tkinter import *


root =Tk()
root.geometry("400x300")
root.title("Engimeerimg Calculation")


# ....................AREA.................................
def sec_win1():                                                   #second window for area
    win1 = Tk()
    win1.title("Area")
    win1.geometry("250x200")

    label_formula= Label(win1,text="Area  =",font="bold").grid(row=0,column=1)
    label_formula = Label(win1,text="length X width",font="bold").grid(row=0,column=2)

    label2 = Label(win1,text="Lenght").grid(row=1,column=1)
    entry2 = Entry(win1).grid(row=1,column=2)

    label2 = Label(win1,text="Width").grid(row=2,column=1)
    entry2 = Entry(win1).grid(row=2,column=2)

    button2 = Button(win1,text="Find Area",bg="#beefd4",font="Bold").grid(row=4,column=1)
    entry2 = Entry(win1,bg="#beefd4",bd=3).grid(row=4,column=2)
  


# .......................Volume................................
def third_win2():                                                   #third window for Volume
    win2 = Tk()
    win2.title("Volume")
    win2.geometry("300x200")

    label_formula= Label(win2,text="volume  =",font="bold").grid(row=0,column=1)
    label_formula = Label(win2,text="length X width X height",font="bold").grid(row=0,column=2)

    label2 = Label(win2,text="Lenght").grid(row=1,column=1)
    entry2 = Entry(win2).grid(row=1,column=2)

    label2 = Label(win2,text="Width").grid(row=2,column=1)
    entry2 = Entry(win2).grid(row=2,column=2)

    label2 = Label(win2,text="Hight").grid(row=3,column=1)
    entry2 = Entry(win2).grid(row=3,column=2)

    button2 = Button(win2,text="Find Volume",bg="#beefd4",font="Bold").grid(row=5,column=1)
    entry2 = Entry(win2,bg="#beefd4",bd=3).grid(row=5,column=2)


# ...........................Menu ..............................
my_menu = Menu(root)            
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File",menu=file_menu)


eng_menu = Menu(my_menu)
my_menu.add_cascade(label="Engineering",menu=eng_menu)
#menu option
eng_menu.add_cascade(label="Area",command=sec_win1)
eng_menu.add_separator()                                  #separate two menu option
eng_menu.add_cascade(label="Volume",command=third_win2)






root.mainloop()