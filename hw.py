from tkinter import *

root = Tk()
root.title('Simple and Compound Interest Calculator')
root.geometry('400x400')
frame = Frame(bg='#0413f9', height=350, width=380)
frame.pack()

pLabel = Label(frame, text='Principal amount: ')
pEntry = Entry(frame)
tLabel = Label(frame, text='Time Period: ')
tEntry = Entry(frame)
rLabel = Label(frame, text='Rate of Interest: ')
rEntry = Entry(frame)
sInterst = Label()
cInterest = Label()


def calculate():
    principal = int(pEntry.get())
    time = int(tEntry.get())
    rate = int(rEntry.get())
    si = principal * time * rate / 100
    ci = (principal * (1 + rate/100)**time) - principal
    sInterst.config(text='Simple Interest is ' + str(si))
    cInterest.config(text='Compound Interst is ' + str(ci))


calculation = Button(frame, text='Calculate SI and CI', command=calculate)

pLabel.place(x=20, y=20)
pEntry.place(x=150, y=20)
tLabel.place(x=20, y=80)
tEntry.place(x=150, y=80)
rLabel.place(x=20, y=140)
rEntry.place(x=150, y=140)
calculation.place(x=150, y=200)
sInterst.place(x=75, y=250)
cInterest.place(x=75, y=300)
root.mainloop()
