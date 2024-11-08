from tkinter import*
from PIL import ImageTk,Image,ImageFilter
import os

def main():
    win.destroy()
    os.system('login.py')


win=Tk()
#win.overrideredirect(FALSE)
win.attributes('-fullscreen',TRUE)
#win.attributes('-disabled',TRUE)
#win.attributes('-toolwindow',TRUE)
#win.attributes('-topmost',TRUE)
win.attributes('-alpha',0.9)
#win.attributes('-transparentcolor','pink')
win.config(bg="black")
#win.minsize(400,400)
#win.minsize(400,400)
#win.geometry("400x400")
#win.focus_force()
#win.resizable(FALSE)
def quit(event):
    win.destroy()
win.bind('<Escape>',quit)

pic=Image.open('login.jpg')
#blurred=pic.filter(ImageFilter.BoxBlur(20))
render=ImageTk.PhotoImage(pic)
img=Label(win,image=render)
img.place(x=0,y=0,relwidth=1,relheight=1)


header=Frame(win,height=100,width=1000,bg='black',relief="ridge",bd=10,padx=30,pady=30)
header.pack(side=TOP)

right=Frame(win,height=100,width=100,bg="black",relief="sunken")
right.pack(side=RIGHT,anchor=N,padx=4)

out=Button(right,text="Logout",fg="red",bg="black",font=("harrington",20,"bold"),command=main)
out.grid(row=0,column=0)
lb1=Label(header,text="LIBRARY MANAGEMENT SYSTEM",font=("harrington",45,"bold"),width=38,fg="lime",bg="black")
lb1.grid(row=0,column=0)

body=Frame(win,height=400,width=400,bg="black",relief="sunken",bd=10,padx=40,pady=40)
body.pack(pady=40)

lb2=Label(body,text="Enter Roll No to pull record",fg="orange",bg="black",font=("harrington",25,"bold"))
lb2.grid(row=0,column=0,pady=10,padx=10,columnspan=2)


lb3=Label(body,text="Roll No:",fg="lime",bg="black",font=("harrington",20,"bold"))
lb3.grid(row=1,column=0,pady=10,padx=10)

a=StringVar()
tb1=Entry(body,textvariable=a,bg="black",fg="white")
tb1.grid(row=1,column=1,ipady=7,ipadx=20)


btn=Button(body,text="Submit",font=("harrington",20,"bold"),relief="groove",fg="yellow",bg="black")
btn.grid(row=2,column=0,columnspan=2,pady=10,padx=10)

can=Canvas(body,height=10,width=450,bd=0,relief="flat")
oval=can.create_line(0, 5, 452, 5,fill="green",width=13)
can.grid(row=3,column=0,columnspan=2)

btn1=Button(body,text="Add Student",font=("harrington",17,"bold"),relief="groove",fg="cyan",bg="black")
btn1.grid(row=4,column=0,padx=10,pady=10)
btn2=Button(body,text="Delete Student",font=("harrington",17,"bold"),relief="groove",fg="cyan",bg="black")
btn2.grid(row=4,column=1)
btn3=Button(body,text="Add Book",font=("harrington",17,"bold"),relief="groove",fg="cyan",bg="black")
btn3.grid(row=5,column=0)
btn4=Button(body,text="Issue Book",font=("harrington",17,"bold"),relief="groove",fg="cyan",bg="black")
btn4.grid(row=5,column=1)
btn5=Button(body,text="Return Book",font=("harrington",17,"bold"),relief="groove",fg="cyan",bg="black")
btn5.grid(row=6,column=0,columnspan=2,padx=10,pady=10)

win.mainloop()
