from tkinter import *

root = Tk()
root.title("Calculator")

display_bar = Label(root, text = "", width = 15, borderwidth=15, relief = SUNKEN, bg = "black", fg = "cyan", font = ("Times New Roman", 30))
display_bar.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)
root.config(bg = "black")

#Button picture
equal_button = PhotoImage(file = "greenequal1.png")
num_button = PhotoImage(file = "blacknum1.png")
clear_button = PhotoImage(file = "redclear1.png")

expression = ""

def button_click(number):
    global expression
    expression += number
    display_bar.config(text=expression)

def button_clear():
    global expression
    expression = ""
    display_bar.config(text=expression)

def button_equal():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
        except:
            result = "Error"
            expression = ""
        display_bar.config(text = result)


button_1 = Button(root, text = "1" ,  image = num_button , bg = "black", borderwidth = 0, font = ("Times new roman",40,"bold"),
                  foreground = "white", compound = CENTER , command = lambda : button_click("1"))
button_2= Button(root, text = "2" ,  image = num_button , bg = "black", borderwidth = 0, font = ("Times new roman",40,"bold"),
                  foreground = "white",compound = CENTER , command = lambda : button_click("2"))
button_3 = Button(root, text = "3" ,  image = num_button , bg = "black", borderwidth = 0, font = ("Times new roman",40,"bold"),
                  foreground = "white",compound = CENTER , command = lambda : button_click("3"))
button_4 = Button(root, text = "4" ,  image = num_button , bg = "black", borderwidth = 0, font = ("Times new roman",40,"bold"),
                  foreground = "white",compound = CENTER , command = lambda : button_click("4"))
button_5 = Button(root, text = "5" ,  image = num_button , bg = "black", borderwidth = 0, font = ("Times new roman",40,"bold"),
                  foreground = "white",compound = CENTER , command = lambda : button_click("5"))
button_6 = Button(root, text = "6" ,  image = num_button , bg = "black", borderwidth = 0, font = ("Times new roman",40,"bold"),
                  foreground = "white",compound = CENTER , command = lambda : button_click("6"))
button_7 = Button(root, text = "7" ,  image = num_button , borderwidth = 0, font = ("Times new roman",40,"bold"),
                  foreground="white", bg = "black",
                  compound = CENTER , command = lambda : button_click("7"))
button_8 = Button(root, text = "8" ,  image = num_button , borderwidth = 0, font = ("Times new roman",40,"bold"),
                  foreground="white", bg = "black",
                  compound = CENTER , command = lambda : button_click("8"))
button_9 = Button(root, text = "9" ,  image = num_button , borderwidth = 0, font = ("Times new roman",40,"bold"),
                  foreground="white", bg = "black",
                  compound = CENTER , command = lambda : button_click("9"))
button_0 = Button(root, text = "0" ,  image = num_button , borderwidth = 0, font = ("Times new roman",40,"bold"),
                  foreground="white", bg = "black",
                  compound = CENTER , command = lambda : button_click("0"))


button_add = Button(root, text = "+", font = ("Times new roman",40,"bold") ,command = lambda: button_click("+"), borderwidth = 0,
                    image = num_button, bg = "black", fg = "green", compound = CENTER)
button_sub = Button(root, text = "-", font = ("Times new roman",45,"bold") ,  borderwidth = 0, command = lambda: button_click("-"),
                    image = num_button, bg = "black", fg = "green", compound = CENTER)
button_mul = Button(root, text = "×", font = ("Times new roman",40,"bold") ,  borderwidth = 0, command = lambda: button_click("*"),
                    image = num_button, bg = "black", fg = "green", compound = CENTER)
button_div = Button(root, text = "/", font = ("Times new roman",40,"bold") ,  borderwidth = 0, command = lambda: button_click("/"),
                    image = num_button, bg = "black", fg = "green", compound = CENTER)
button_decimal = Button(root, text = ".", font = ("Times new roman",40,"bold") ,  borderwidth = 0, command = lambda: button_click("."),
                    image = num_button, bg = "black", fg = "white", compound = CENTER)
button_per = Button(root, text = "%", font = ("Times new roman",35,"bold") ,  borderwidth = 0,  command = lambda: button_click("%"),
                    image = num_button, bg = "black", fg = "green", compound = CENTER)
button_brack = Button(root, text = "()", font = ("Times new roman",35,"bold") ,  borderwidth = 0,  command = lambda: button_click("()"),
                    image = num_button, bg = "black", fg = "green", compound = CENTER)
button_minusbrack = Button(root, text = "+/-", font = ("Times new roman",40,"bold") , fg = "white", borderwidth = 0,  command = lambda: button_click("(-"),
                    image = num_button, bg = "black", compound = CENTER)

button_equal = Button(root, text = "=", font = ("Times new roman",40,"bold") , borderwidth = 0, image = equal_button,
                      command = button_equal, bg = "black", compound = CENTER)
button_clear = Button(root, text = "C", font = ("Times new roman",40) , command = button_clear,
                      borderwidth = 0, bg = "black", image = clear_button, compound = CENTER)




button_1.grid(row = 4, column = 0)
button_2.grid(row = 4, column = 1)
button_3.grid(row = 4, column = 2)
button_4.grid(row = 3, column = 0)
button_5.grid(row = 3, column = 1)
button_6.grid(row = 3, column = 2)
button_7.grid(row = 2, column = 0)
button_8.grid(row = 2, column = 1)
button_9.grid(row = 2, column = 2)
button_0.grid(row = 5, column = 1)

button_add.grid(row = 4, column = 3)
button_sub.grid(row = 3, column = 3)
button_mul.grid(row = 2, column = 3)
button_div.grid(row = 1, column = 3)
button_decimal.grid(row = 5, column = 2)
button_per.grid(row = 1, column = 2)
button_brack.grid(row = 1, column = 1)
button_minusbrack.grid(row = 5, column = 0)


button_clear.grid(row = 1, column = 0)
button_equal.grid(row = 5, column = 3)


root.mainloop()

