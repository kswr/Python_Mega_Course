from tkinter import *

window = Tk()


def kg_to_gr():
    grams = round(float(e1_value.get()) * 1000, 3)
    t1.delete("1.0", END)
    t1.insert(END, grams)


def kg_to_pounds():
    pounds = round(float(e1_value.get()) * 2.20462, 3)
    t2.delete("1.0", END)
    t2.insert(END, pounds)


def kg_to_ounces():
    ounces = round(float(e1_value.get()) * 35.274, 3)
    t3.delete("1.0", END)
    t3.insert(END, ounces)


def convert():
    kg_to_gr()
    kg_to_pounds()
    kg_to_ounces()


var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()

b1 = Button(window, text="Convert", command=convert)
b1.grid(row=0, column=2)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

l1 = Label(window, height=1, width=20, textvariable=var1)
l1.grid(row=0, column=0)
var1.set("Kilograms")

l1 = Label(window, height=1, width=20, textvariable=var2)
l1.grid(row=2, column=0)
var2.set("Grams")

l1 = Label(window, height=1, width=20, textvariable=var3)
l1.grid(row=2, column=1)
var3.set("Pounds")

l1 = Label(window, height=1, width=20, textvariable=var4)
l1.grid(row=2, column=2)
var4.set("Ounces")

window.mainloop()
