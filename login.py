from tkinter import *
import time


root = Tk()
root.geometry("700x500")

def calculate():

    samosa=e1.get()
    pizza=e2.get()
    burger=e3.get()
    fried_rice=e4.get()
    total= (int(samosa)*20)+(int(pizza)*850)+(int(burger)*200)+(int(fried_rice)*120)
    lbl12 = Label(root, text=total, font="times 15 bold")
    lbl12.place(x=100, y=300)




#styling the label widget


#----------------menu section--------
lbl1 = Label(root, text="Menu", font="times 30 bold")
lbl1.place(x=580, y=50)

lbl2 = Label(root, text="samosa   ksh. 20", font="times 15 bold")
lbl2.place(x=480, y=110)

lbl3 = Label(root, text="pizza    ksh. 850", font="times 15 bold")
lbl3.place(x=480, y=134)

lbl4 = Label(root, text="burger   ksh.200", font="times 15 bold")
lbl4.place(x=480, y=156)

lbl10 = Label(root, text="fried rice ksh.120", font="times 15 bold")
lbl10.place(x=480, y=179)

lbl5 = Label(root, text="Select item to purchase", font="times 15 bold")
lbl5.place(x=50, y=30)

lbl11 = Label(root, text="Jodham Restaurant", font="times 15 bold")
lbl11.place(x=200, y=3)

lbl6 = Label(root, text="samosa", font="times 15 bold")
lbl6.place(x=60, y=60)

lbl7 = Label(root, text="pizza", font="times 15 bold")
lbl7.place(x=250, y=60)

lbl8 = Label(root, text="burger", font="times 15 bold")
lbl8.place(x=60, y=150)

lbl9 = Label(root, text="fried rice", font="times 15 bold")
lbl9.place(x=250, y=150)

e1= Entry(root)
e1.place(x=60, y=100)

e2= Entry(root)
e2.place(x=250, y=100)

e3= Entry(root)
e3.place(x=60, y=180)

e4= Entry(root)
e4.place(x=250, y=180)

btn1 =Button(root,text="Total", font="times 15 bold", command=calculate)
btn1.place(x=130,y=240)

root.mainloop()

