from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image,ImageFilter
import os
import pymysql
import datetime

issuedate=datetime.datetime.now().date()
returndate=issuedate+datetime.timedelta(days=14)
id=str(issuedate)
rd=str(returndate)

def admin():
    win.destroy()
    os.system('adminarea.py')

def check():
    isbn=c.get()
    if(isbn==''):
        messagebox.showinfo("Error","Empty Field(s)")
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='', db='library')
            cr = con.cursor()
            cr.execute("select available from books where isbn='"+isbn+"'")
            result=cr.fetchall()
            count=cr.rowcount
            if(count>0):
                for row in result:
                    if(row[0]>0):
                        limit()
                    else:
                        messagebox.showinfo("Message", "No Books Left for Issue")

        except:
            con.rollback()
            messagebox.showinfo("Error", "Oops,Some Error Occurred in Query1!!!")
        con.close()

def limit():
    rn=a.get()
    if (rn == ''):
        messagebox.showinfo("Error", "Empty Field(s)")
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='', db='library')
            cr = con.cursor()
            cr.execute("select * from issuebook where rollno='"+rn+"'")
            count=cr.rowcount
            if(count==3):
                messagebox.showinfo("Message","Can Not Issue More Books!!! Already 3 Books Issued")
                a.set('')
                b.set('')
                c.set('')
            else:
                issue_book()

        except:
            con.rollback()
            messagebox.showinfo("Error", "Oops,Some Error Occurred in Query2!!! Can't Check Book Issue Limit")
        con.close()



def issue_book():
    rn=a.get()
    bn=b.get()
    isbn=c.get()
    if (isbn == '' or bn=='' or rn==''):
        messagebox.showinfo("Error", "Empty Field(s)")
    else:
        try:

            con=pymysql.connect(host='localhost',user='root',password='',db='library')
            cr=con.cursor()
            cr.execute("insert into issuebook(rollno,book_name,isbn,issue_date,return_date) values('"+rn+"','"+bn+"','"+isbn+"','"+id+"','"+rd+"')")
            con.commit()
            messagebox.showinfo("Message", "Book Issued")
            update()
        except:
            con.rollback()
            messagebox.showinfo("Message","Can Not Issue Same Book Again You Already Issued Before")
            b.set('')
            c.set('')
        con.close()

def update():
    try:
        isbn=c.get()
        con=pymysql.connect(host='localhost',user='root',password='',db='library')
        cr=con.cursor()
        cr.execute("UPDATE books SET issued=issued+1,available=available-1 where isbn='"+isbn+"' ")
        con.commit()
        #messagebox.showinfo("Message", "Books Data Updated")
        a.set('')
        b.set('')
        c.set('')

    except:
        con.rollback()
        messagebox.showinfo("Error","Oops, Some Error Occurred in Query4!!!")
    con.close()


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

pic=Image.open('issuebook.jpg')
#blurred=pic.filter(ImageFilter.BoxBlur(20))
render=ImageTk.PhotoImage(pic)
img=Label(win,image=render)
img.place(x=0,y=0,relwidth=1,relheight=1)


header=Frame(win,height=100,width=1000,bg='black',relief="ridge",bd=10,padx=30,pady=30)
header.pack(side=TOP)

def main():
    win.destroy()
    os.system('login.py')

def home():
    win.destroy()
    os.system('adminarea.py')

left=Frame(win,height=100,width=100,bg="black",relief="sunken")
left.pack(side=LEFT,anchor=N,padx=4)

aa=Button(left,text="Home",fg="white",bg="black",font=("harrington",20,"bold"),command=home)
aa.grid(row=0,column=0)

right=Frame(win,height=100,width=100,bg="black",relief="sunken")
right.pack(side=RIGHT,anchor=N,padx=4)

out=Button(right,text="Logout",fg="red",bg="black",font=("harrington",20,"bold"),command=main)
out.grid(row=0,column=0)

lb1=Label(header,text="ISSUE BOOK",font=("harrington",45,"bold"),width=38,fg="lime",bg="black")
lb1.grid(row=0,column=0)

body=Frame(win,height=400,width=400,bg="black",relief="sunken",bd=10,padx=40,pady=40)
body.pack(pady=40)

lb2=Label(body,text="Roll Number ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb2.grid(row=0,column=0,sticky=W)

a=StringVar()
tb1=Entry(body,textvariable=a,bg="black",fg="white")
tb1.grid(row=0,column=1)

lb3=Label(body,text="Book Name ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb3.grid(row=1,column=0,sticky=W)

b=StringVar()
tb1=Entry(body,textvariable=b,bg="black",fg="white")
tb1.grid(row=1,column=1)

lb4=Label(body,text="ISBN ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb4.grid(row=2,column=0,sticky=W)

c=StringVar()
tb2=Entry(body,textvariable=c,bg="black",fg="white")
tb2.grid(row=2,column=1)

#lb5=Label(body,text="Date of Issue ",fg="lime",bg="black",font=("harrington",20,"bold"))
#lb5.grid(row=3,column=0,sticky=W)

#d=StringVar()
#tb3=Entry(body,textvariable=d,bg="black",fg="white")
#tb3.grid(row=3,column=1)

#lb6=Label(body,text="Return Days  ",fg="lime",bg="black",font=("harrington",20,"bold"))
#lb6.grid(row=3,column=0,sticky=W)

#e=StringVar()
#tb4=Entry(body,textvariable=e,bg="black",fg="white")
#tb4.grid(row=3,column=1)

btn=Button(body,text="Submit",font=("harrington",20,"bold"),relief="groove",fg="yellow",bg="black",command=check)
btn.grid(row=3,column=0,columnspan=2,pady=10,padx=10)

win.mainloop()
