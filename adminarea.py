from tkinter import*
from PIL import ImageTk,Image,ImageFilter
from tkinter import messagebox
import pymysql
import time

import os

def main():
    win.destroy()
    os.system('login.py')

def clock():
    ctime=time.localtime()
    ftime=time.strftime('%H:%M:%S', ctime)
    fdate=time.strftime('%a, %d %b %Y', ctime)
    tm.config(text=ftime)
    dt.config(text=fdate)
    win.after(100,clock)

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

def stu_det():
    win.destroy()
    os.system('student_details.py')

def add_book():
    win.destroy()
    os.system('add_book.py')

def add_stu():
    win.destroy()
    os.system('add_student.py')

def del_stu():
    win.destroy()
    os.system('delete_student.py')

def issue_b():
    win.destroy()
    os.system('issue_book.py')

def return_b():
    win.destroy()
    os.system('return_book.py')

def alls():
    win.destroy()
    os.system('all_students.py')

def allb():
    win.destroy()
    os.system('all_books.py')


pic=Image.open('adminarea.jpg')
#blurred=pic.filter(ImageFilter.BoxBlur(20))
render=ImageTk.PhotoImage(pic)
img=Label(win,image=render)
img.place(x=0,y=0,relwidth=1,relheight=1)


header=Frame(win,height=100,width=1000,bg='black',relief="ridge",bd=10,padx=30,pady=30)
header.pack(side=TOP)

left=Frame(win,height=100,width=100,bg="black",relief="sunken")
left.pack(side=LEFT,anchor=N,padx=4)

tm=Label(left,text="",font=("small fonts",17,"bold"),width=13,bg='black',fg='white')
tm.grid(row=0,column=0)
dt=Label(left,text="",font=("Brush Script MT",17,"bold"),width=13,bg='black',fg='white')
dt.grid(row=1,column=0)
clock()

right=Frame(win,height=100,width=100,bg="black",relief="sunken")
right.pack(side=RIGHT,anchor=N,padx=4)

out=Button(right,text="Logout",fg="red",bg="black",font=("harrington",20,"bold"),width=13,command=main)
out.grid(row=0,column=0)
lb1=Label(header,text="LIBRARY MANAGEMENT SYSTEM",font=("harrington",45,"bold"),width=38,fg="lime",bg="black")
lb1.grid(row=0,column=0)

body=Frame(win,height=400,width=400,bg="black",relief="sunken",bd=10,padx=40,pady=40)
body.pack(pady=40)

btn1=Button(body,text="Student Details",font=("harrington",17,"bold"),relief="groove",fg="cyan",bg="black",width=20,command=stu_det)
btn1.grid(row=0,column=0,padx=10,pady=10)
btn2=Button(body,text="Add Student",font=("harrington",17,"bold"),relief="groove",fg="cyan",bg="black",width=20,command=add_stu)
btn2.grid(row=0,column=1,pady=10)
#btn3=Button(body,text="Delete Student",font=("harrington",17,"bold"),relief="groove",fg="cyan",bg="black",width=20,command=del_stu)
#btn3.grid(row=1,column=0)
btn4=Button(body,text="Issue Book",font=("harrington",17,"bold"),relief="groove",fg="cyan",bg="black",width=20,command=issue_b)
btn4.grid(row=1,column=0)
btn5=Button(body,text="Return Book",font=("harrington",17,"bold"),relief="groove",fg="cyan",bg="black",width=20,command=return_b)
btn5.grid(row=1,column=1)
btn6=Button(body,text="All Students Detail",font=("harrington",17,"bold"),relief="groove",fg="cyan",bg="black",width=20,command=alls)
btn6.grid(row=2,column=0,pady=10)
btn7=Button(body,text="All Books Detail",font=("harrington",17,"bold"),relief="groove",fg="cyan",bg="black",width=20,command=allb)
btn7.grid(row=2,column=1)
btn8=Button(body,text="Add / Update / Delete Book",font=("harrington",17,"bold"),relief="groove",fg="cyan",bg="black",width=25,command=add_book)
btn8.grid(row=3,column=0,columnspan=2)


win.mainloop()
