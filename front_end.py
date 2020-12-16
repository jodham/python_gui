from tkinter import *

window = Tk()
l1 = Label(window, text="title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)
#define entries

title_text = StringVar()
e1 = Entry(window)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window)
e3.grid(row=1, column=1)

ISBN_text = StringVar()
e4 = Entry(window)
e4.grid(row=1, column=3)
#define listbox
list1=Listbox(window,width=35, height=6)
list1.grid(row=2,column=1,rowspan=6,columnspan=2)
#attach scrollbar to the list
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
#attach scrollbar to the list
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
#define buttons
b1=Button(window, text="view all", width=12)
b1.grid(row=2,column=3)

b1=Button(window, text="Search Entry", width=12)
b1.grid(row=2,column=3)

b1=Button(window, text="Add Entry", width=12)
b1.grid(row=3,column=3)

b1=Button(window, text="update selected", width=12)
b1.grid(row=4,column=3)
window.mainloop()
