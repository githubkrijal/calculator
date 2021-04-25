from tkinter import *

root = Tk()

text = Text(root)
text.insert(INSERT, "Hello, world!\n")
text.insert(END, "This is a phrase.\n")
text.insert(END, "Bye bye...")
text.pack(expand=1, fill=BOTH)

# adding a tag to a part of text specifying the indices
text.tag_add("start", "1.8", "1.13")
text.tag_config("start", background="black", foreground="yellow")

root.mainloop()







"""        
def button_clear():
    display_bar.delete(0, END)

def button_add():
    first_number = display_bar.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    display_bar.delete(0, END)

def button_sub():
    first_number = display_bar.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    display_bar.delete(0, END)


def button_mul():
    first_number = display_bar.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    display_bar.delete(0, END)


def button_div():
    first_number = display_bar.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    display_bar.delete(0, END)


def button_per():
    first_number = display_bar.get()
    global f_num
    global math
    math = "percentage"
    f_num = int(first_number)
    display_bar.delete(0, END)


def button_dot():
    first_number = display_bar.get()
    global f_num
    f_num = float(first_number)
    display_bar.delete(0, END)

def button_brack():
    return

def button_minusbrack():
    return

def button_equal():
    second_number = display_bar.get()
    display_bar.delete(0, END)

    if math == "addition":
        display_bar.insert(0, f_num + int(second_number))

    if math == "subtraction":
        display_bar.insert(0, f_num - int(second_number))


    if math == "multiplication":
        display_bar.insert(0, f_num * int(second_number))

    if math == "division":
       display_bar.insert(0, f_num / int(second_number))

    if math == "percentage":
        display_bar.insert(0, f_num % int(second_number))

    if math == "dot":
        display_bar.insert(0, f_num . float(second_number))

    if math == "bracket":
        display_bar.insert(0, f_num - int(second_number))

    if math == "addition":
        display_bar.insert(0, f_num + int(second_number))
"""





