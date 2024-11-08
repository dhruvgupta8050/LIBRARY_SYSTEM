from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image,ImageFilter
import os
import pymysql
def admin():
    win.destroy()
    os.system('adminarea.py')

def addb():
    book=a.get()
    isbn=b.get()
    q=c.get()
    if (book == '' or isbn == '' or q == ''):
        messagebox.showinfo("Error", "Empty Detail(s), Please Enter Details")
    else:
        try:

            con=pymysql.connect(host='localhost',user='root',password='',db='library')
            cr=con.cursor()
            cr.execute("insert into books(book_name,isbn,quantity) values('"+book+"','"+isbn+"','"+q+"')")
            con.commit()
            messagebox.showinfo("Message", "Book Added Successfully")
            a.set('')
            b.set('')
            c.set('')

        except:
            con.rollback()
            messagebox.showinfo("Error","Book Not Added")
        con.close()

def updb():
    book=a.get()
    isbn=b.get()
    q=c.get()
    if(book=='' or isbn=='' or q==''):
        messagebox.showinfo("Error","Empty Detail(s), Please Enter Details")
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='library')
            cr=con.cursor()
            cr.execute("update books set book_name='"+book+"',quantity=quantity+'"+q+"',available=available+'"+q+"' where isbn='"+isbn+"'")
            con.commit()
            messagebox.showinfo("Message", "Book Details Updated Successfully")
            a.set('')
            b.set('')
            c.set('')

        except:
            con.rollback()
            messagebox.showinfo("Error","Book Details Not Updated")
        con.close()

def delb():
    isbn=b.get()
    if(isbn==''):
        messagebox.showinfo("Error","Please Enter ISBN")
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='library')
            cr=con.cursor()
            cr.execute("delete from books where isbn='"+isbn+"'")
            con.commit()
            messagebox.showinfo("Message", "Book Deleted Successfully")
            a.set('')
            b.set('')
            c.set('')

        except:
            con.rollback()
            messagebox.showinfo("Error","Book Details Not Updated")
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

pic=Image.open('addb.jpg')
#blurred=pic.filter(ImageFilter.BoxBlur(20))
render=ImageTk.PhotoImage(pic)
img=Label(win,image=render)
img.place(x=0,y=0,relwidth=1,relheight=1)

header=Frame(win,height=100,width=1000,bg='black',relief="ridge",bd=10,padx=30,pady=30)
header.pack(side=TOP)

lb1=Label(header,text="ADD BOOK",font=("harrington",45,"bold"),width=38,fg="lime",bg="black")
lb1.grid(row=0,column=0)

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

body=Frame(win,height=400,width=400,bg="black",relief="sunken",bd=10,padx=40,pady=40)
body.pack(pady=40)

lb2=Label(body,text="Book Name ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb2.grid(row=0,column=1,sticky=W)

a=StringVar()
tb1=Entry(body,textvariable=a,bg="black",fg="white")
tb1.grid(row=0,column=2)

lb3=Label(body,text="ISBN ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb3.grid(row=1,column=1,sticky=W)

b=StringVar()
tb2=Entry(body,textvariable=b,bg="black",fg="white")
tb2.grid(row=1,column=2)

lb4=Label(body,text="Quantity ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb4.grid(row=2,column=1,sticky=W)

c=StringVar()
tb3=Entry(body,textvariable=c,bg="black",fg="white")
tb3.grid(row=2,column=2)

btn=Button(body,text="Update",font=("harrington",20,"bold"),relief="groove",fg="yellow",bg="black",command=updb)
btn.grid(row=3,column=0)

ubtn=Button(body,text="Submit",font=("harrington",20,"bold"),relief="groove",fg="yellow",bg="black",command=addb)
ubtn.grid(row=3,column=1,columnspan=2,pady=10)

dbtn=Button(body,text="Delete",font=("harrington",20,"bold"),relief="groove",fg="yellow",bg="black",command=delb)
dbtn.grid(row=3,column=3)

win.mainloop()
