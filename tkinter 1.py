from tkinter import *

root = Tk()

e1 = Entry(root, width=50, fg="blue", bg="white", borderwidth=5)
e1.pack()

def myclick():
    textoutput = "Hello" + e1.get()

    myLabel1 = Label(root, text="Tkinter program beginning")

    myLabel1.pack()

myLabel2 = Button(root, text="CLICK", command=myclick)
myLabel2.pack()

root.mainloop()

