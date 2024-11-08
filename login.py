from tkinter import*
from tkinter import messagebox
import time
from itertools import cycle
from PIL import ImageTk,Image,ImageFilter
import os
import pymysql
import random
def admin():
    win.destroy()
    os.system('adminarea.py')

def log():
    id=a.get()
    pw=b.get()
    if(id=='' or pw==''):
        messagebox.showinfo("Error","Empty Detail(s)")
    else:
        con=pymysql.connect(host='localhost',user='root',password='',db='library')
        c=con.cursor()
        c.execute("select * from admin where id='"+id+"' and password='"+pw+"'")
        result=c.fetchall()
        count=c.rowcount
        if(count>0):
            admin()
        else:
            messagebox.showinfo("Error","Incorrect ID or Password")

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


def exit():
    win.destroy()

def info():
    inf=Tk()
    inf.title("Welcome")
    #inf.overrideredirect(TRUE)
    inf.attributes('-toolwindow',TRUE)
    #inf.minsize(1350, 720)
    inf.state('zoomed')
    #inf.attributes('-fullscreen',TRUE)
    #inf.attributes('-alpha',0.9)
    #inf.config(bg="black")
    head=Frame(inf,height=100,width=600)
    head.pack(fill=BOTH)
    body=Frame(inf)
    body.pack(fill=BOTH,expand=TRUE)
    letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    column=[]
    row=[]
    for i in range(0,17):
        column.insert(i,i)
    for i in range(0,9):
        row.insert(i,i)
    colors=['#f44336','#E91E63','#9C27B0','#673AB7','#3F51B5','#2196F3','#03A9F4','#00BCD4','#009688','#4CAF50','#8BC34A','#CDDC39','#FFEB3B','#FFC107','#FF9800','#FF5722','#795548','#9E9E9E','#607D8B']
    def change():
        body.config(bg=random.choice(colors))
        let=Button(body,text=random.choice(letters),font=('Castellar',30,'bold'),width=2,relief=RIDGE)
        let.grid(row=random.choice(row),column=random.choice(column),padx=5,pady=5)
        let.config(bg=random.choice(colors))
        body.after(2500, change)

    change()
    rules = ['Welcome to most advanced LIBRARY MANAGEMENT SYSTEM',
             'Login with Admin ID and Password provided to you and always remember them. In case you forget them, contact us to get them',
             'You can perform many tasks from ADMIN AREA',
             'You can press ESCAPE button anytime to close the application',
             'A student can issue a book for maximum of 14 days. If he/she return book after 14 days, fine of Rs 2 per day will be imposed',
             'A student can issue maximum 3 books at a time. To issue another book(s), first return any book(s)',
             'A student can only issue 3 different books. He/She can not issue same book twice or thrice at a time ',
             'You can even us Bar Code Scanner to input ISBN number and Book Name directly while performing books related operations (This feature is disabled by default)',
             'Contact us at abc@xyz.com or (+91)9876543211 for 24x7 support',
             'Thanks for using this system. Hope you will enjoy it.']
    ruless=cycle(rules)
    def changer():
        rls=Button(head,text=next(ruless),font=('Century Gothic',10,'bold'),width=170,bg="white")
        rls.grid(row=0,column=0)
        body.after(5000,changer)
    changer()

    inf.mainloop()

pic=Image.open('login.jpg')
#blurred=pic.filter(ImageFilter.BoxBlur(20))
render=ImageTk.PhotoImage(pic)
img=Label(win,image=render)
img.place(x=0,y=0,relwidth=1,relheight=1)


header=Frame(win,height=100,width=1000,bg='black',relief="ridge",bd=10,padx=30,pady=30)
header.pack(side=TOP)

lb1=Label(header,text="LIBRARY MANAGEMENT SYSTEM",font=("harrington",45,"bold"),width=38,fg="lime",bg="black")
lb1.grid(row=0,column=0)

left=Frame(win,height=100,width=100,bg="black",relief="sunken")
left.pack(side=LEFT,anchor=N,padx=4)

info=Button(left,text="Intro",fg="white",bg="black",font=("harrington",20,"bold"),width=4,command=info)
info.grid(row=0,column=0)

right=Frame(win,height=100,width=100,bg="black",relief="sunken")
right.pack(side=RIGHT,anchor=N,padx=4)

out=Button(right,text="Exit",fg="red",bg="black",font=("harrington",20,"bold"),width=4,command=exit)
out.grid(row=0,column=0)

lb1=Label(header,text="LIBRARY MANAGEMENT SYSTEM",font=("harrington",45,"bold"),width=38,fg="lime",bg="black")
lb1.grid(row=0,column=0)


body=Frame(win,height=400,width=400,bg="black",relief="sunken",bd=10,padx=40,pady=40)
body.pack(pady=40)

lb2=Label(body,text="Admin ID ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb2.grid(row=0,column=0,sticky=W)

a=StringVar()
tb1=Entry(body,textvariable=a,bg="black",fg="white")
tb1.grid(row=0,column=1)

lb3=Label(body,text="Password ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb3.grid(row=1,column=0,sticky=W)

b=StringVar()
tb2=Entry(body,textvariable=b,bg="black",fg="white",show="*")
tb2.grid(row=1,column=1)

btn=Button(body,text="Login",font=("harrington",20,"bold"),relief="groove",fg="yellow",bg="black",command=log)
btn.grid(row=2,column=0,columnspan=2,pady=10)

win.mainloop()
