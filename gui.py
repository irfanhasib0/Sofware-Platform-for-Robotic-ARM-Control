import Tkinter
from Tkinter import *
import tkMessageBox
import sys,os
#root = Tkinter.Tk()

t=0
def fun(event):
   global t
   #tkMessageBox.showinfo( "Hello Python", "Hello World")
   t=1
def func(event):
   global t
   #os.system("cmd")
   t=2

root = Tk()
frame = Frame(root,height="500",width="800")
frame.pack()
run=Button(root,text ="run",bg="#555",fg="#fff",height="1",width="3")
run.place(x=300, y=50)
run.bind('<Button-1>', func)
stop=Button(root,text ="stop", command = func,fg="#fff",bg="#000",height="1",width="3")
stop.place(x=300, y=100)
stop.bind('<Button-1>',fun)
text = Text(root,height="1",width="25")
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")
text.place(x=50,y=50)
frame.after(10)
def task():
    print("hello %d"%t)
    root.after(2, task)  # reschedule event in 2 seconds

root.after(2000, task)
root.mainloop()
root.mainloop()
#,height="300",width="200"
