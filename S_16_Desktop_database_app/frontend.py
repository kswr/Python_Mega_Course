"""
A program that stores book information:
Title, Author, Year, ISBN

User can:

View all records
Search all entry
Add entry
Update entry
Delete entry
Close app
"""

from tkinter import *
import backend


# def get_selected_row(event):
#     global selected_tuple
#     if list1.size() > 0:
#         index = list1.curselection()[0]
#         selected_tuple = list1.get(index)
#         e1.delete(0, END)
#         e1.insert(END, selected_tuple[1])
#         e2.delete(0, END)
#         e2.insert(END, selected_tuple[2])
#         e3.delete(0, END)
#         e3.insert(END, selected_tuple[3])
#         e4.delete(0, END)
#         e4.insert(END, selected_tuple[4])


def get_selected_row(event):
    global selected_tuple
    try:
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()):
        list1.insert(END, row)


def insert_command():
    if (title_text.get() != "") & (author_text.get() != ""):
        backend.insert(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get())
    view_command()


def delete_command():
    backend.delete(selected_tuple[0])
    view_command()


# def update_command():
#     backend.update(selected_tuple[0],selected_tuple[1],selected_tuple[2],selected_tuple[3], selected_tuple[4])

def update_command():
    backend.update(selected_tuple[0], e1.get(), e2.get(), e3.get(), e4.get())
    view_command()


window = Tk()

window.wm_title("Book Store")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

ISBN_text = StringVar()
e4 = Entry(window, textvariable=ISBN_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# list1.bind('<<ListboxSelect>>', get_selected_row if list1.size() > 0 else False)
list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(column=3, row=2)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(column=3, row=3)

b3 = Button(window, text="Add entry", width=12, command=insert_command)
b3.grid(column=3, row=4)

b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(column=3, row=5)

b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(column=3, row=6)

b6 = Button(window, text="Close", width=12)
b6.grid(column=3, row=7)

window.mainloop()
