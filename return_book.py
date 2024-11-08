from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image,ImageFilter
import os
import datetime
import pymysql
def admin():
    win.destroy()
    os.system('adminarea.py')

today=datetime.datetime.now().date()

def update():
    isbn=b.get()
    if (isbn == ''):
        messagebox.showinfo("Error", "Empty Field(s)")
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='library')
            cr=con.cursor()
            cr.execute("UPDATE books SET issued=issued-1,available=available+1 where isbn='"+isbn+"' ")
            con.commit()
            #messagebox.showinfo("Message", "Books Data Updated")
            calfine()
        except:
            con.rollback()
            messagebox.showinfo("Error","Oops, Some Error Occurred in Query1!!! Books Data Not Updated.")
        con.close()




def calfine():
    rn=a.get()
    isbn=b.get()
    if (rn == ''):
        messagebox.showinfo("Error", "Empty Field(s)")
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='', db='library')
            c = con.cursor()
            c.execute("select return_date from issuebook where rollno='" + rn + "' and isbn='" + isbn + "'")
            result=c.fetchall()
            count=c.rowcount
            if(count>0):
                for row in result:
                    late=today-row[0]
                    days=late.days
                    if (days > 0):
                        fine = days * 2
                        fn.set(fine)
                        updatefine()
                    else:
                        retb()
                #messagebox.showinfo("Message","Fine Calculated")


        except:
            con.rollback()
            messagebox.showinfo("Error","Oops, Some Error Occured!!! Can't Calculalte Fine")
        con.close()


def retb():
    rn=a.get()
    isbn=b.get()
    try:
        con=pymysql.connect(host='localhost',user='root',password='',db='library')
        c=con.cursor()
        c.execute("delete from issuebook where rollno='"+rn+"' and isbn='"+isbn+"'")
        con.commit()
        messagebox.showinfo("Message", "Book Returned")
        a.set('')
        b.set('')

    except:
        con.rollback()
        messagebox.showinfo("Error","Book Not Returned")
    con.close()



def updatefine():
    rn = a.get()
    fine=fn.get()
    try:
        con = pymysql.connect(host='localhost', user='root', password='', db='library')
        c = con.cursor()
        c.execute("update student SET fine=fine+'"+fine+"' where rollno='" + rn + "'")
        #messagebox.showinfo("Message","Fine Updated")
        con.commit()
        retb()

    except:
        con.rollback()
        messagebox.showinfo("Error", "Oops, Some Error Occured!!! Can't Update Fine")
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

pic=Image.open('return4.jpg')
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

lb1=Label(header,text="RETURN BOOK",font=("harrington",45,"bold"),width=38,fg="lime",bg="black")
lb1.grid(row=0,column=0)

body=Frame(win,height=400,width=400,bg="black",relief="sunken",bd=10,padx=40,pady=40)
body.pack(pady=40)

lb2=Label(body,text="Roll Number ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb2.grid(row=0,column=0,pady=10,sticky=W)

a=StringVar()
tb1=Entry(body,textvariable=a,bg="black",fg="white")
tb1.grid(row=0,column=1)


lb3=Label(body,text="ISBN ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb3.grid(row=1,column=0,pady=10,sticky=W)

b=StringVar()
tb2=Entry(body,textvariable=b,bg="black",fg="white")
tb2.grid(row=1,column=1)

#lb3=Label(body,text="ISBN ",fg="lime",bg="black",font=("harrington",20,"bold"))
#lb3.grid(row=1,column=0,sticky=W)

#b=StringVar()
#tb2=Entry(body,textvariable=b,bg="black",fg="white",show="*")
#tb2.grid(row=1,column=1)

fn=StringVar()
invisible=Entry(win,textvariable=fn)

btn=Button(body,text="Submit",font=("harrington",20,"bold"),relief="groove",fg="yellow",bg="black",command=update)
btn.grid(row=2,column=0,columnspan=2,pady=10,padx=10)

win.mainloop()
