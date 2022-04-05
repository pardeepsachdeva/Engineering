from tkinter import *


root =Tk()
root.geometry("300x200")

def demo():
    pass

# Menu 
my_menu = Menu(root)            
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File",menu=file_menu)


eng_menu = Menu(my_menu)
my_menu.add_cascade(label="Engineering",menu=eng_menu)
#menu option
eng_menu.add_cascade(label="Area",command=demo)
eng_menu.add_separator()                                  #separate two menu option
eng_menu.add_cascade(label="Volume",command=demo)


root.mainloop()