from tkinter import *

root = Tk()

root.geometry("600x500")
root.title("Calculator")

def addition():
    s = int(e1.get())+int(e2.get())
    result.set(s)

result=StringVar()
head = Label(text="Aditional Operator", pady=5 )
head.pack()

n1 = Label(text="Enter First Number", background="yellow", pady=5, padx=30)
n1.grid(row=3, column=2)
n1.pack()
e1= Entry()
e1.pack()




n2 = Label(text="Enter Second Number", background="yellow", pady=7, padx=32)
n2.pack()
e2= Entry()
e2.pack()


btn = Button(text="ADD", command=addition , background="blue")
btn.pack()

prin = Label(textvariable=result)
prin.pack()

root.mainloop()