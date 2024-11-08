from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image,ImageFilter
import os
import pymysql
def admin():
    win.destroy()
    os.system('adminarea.py')

def removelb():
    for i in range(0,3):
        for j in range(0,4):
            lb=Label(booklist,text='                                         ').grid(row=i+1,column=j)

def sdetails():
    rn=r.get()
    if(rn==''):
        messagebox.showinfo("Error","Please Enter Roll Number First")
    else:
        con=pymysql.connect(host='localhost',user='root',password='',db='library')
        cr=con.cursor()
        cr.execute("select * from student where rollno='"+rn+"'")
        result=cr.fetchall()
        count=cr.rowcount
        if(count>0):
            for row in result:
                a.set(row[0])
                b.set(row[1])
                c.set(row[2])
                d.set(row[3])
                e.set(row[4])
                f.set(row[5])
                g.set(row[6])

            lb= Label(booklist, text="********************************").grid(row=4,column=0,columnspan=6)
            #tb1["state"]=DISABLED
            #booklist.destroy()
            removelb()
            book_list()
        else:
            messagebox.showinfo("Error","Incorrect Roll Number")
        con.close()


def update():
    rn=r.get()
    nrn=a.get()
    sn=b.get()
    fn=c.get()
    pn=d.get()
    dob=e.get()
    branch=f.get()
    fine=g.get()
    if(rn=='' or nrn=='' or sn=='' or fn=='' or pn=="" or dob=='' or branch=='' or fine==''):
        messagebox.showinfo("Error","Empty Field(s), Please Enter All Details")
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='', db='library')
            cr=con.cursor()
            cr.execute("update student set rollno='"+nrn+"',student_name='"+sn+"',father_name='"+fn+"',contact='"+pn+"',dob='"+dob+"',branch='"+branch+"',fine='"+fine+"' where rollno='"+rn+"'")
            con.commit()
            messagebox.showinfo("Message","Details Updated")
            a.set('')
            b.set('')
            c.set('')
            d.set('')
            e.set('')
            f.set('')
            g.set('')
            r.set('')

        except:
            messagebox.showinfo("Error","Oops, Some Error Occured!!! Details Not Updated")
            con.rollback()
        con.close()

def dels():
    rn=r.get()
    if(rn==''):
        messagebox.showinfo("Error","Please Enter Roll Number")
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='library')
            c=con.cursor()
            c.execute("delete from student where rollno='"+rn+"'")
            con.commit()
            messagebox.showinfo("Message", "Student Record Deleted")
            a.set('')
            b.set('')
            c.set('')
            d.set('')
            e.set('')
            f.set('')
            g.set('')
            r.set('')


        except:
            con.rollback()
            messagebox.showinfo("Error","Student Record Not Deleted")
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

pic=Image.open('studet.jpg')
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

lb1=Label(header,text="STUDENT DETAIL",font=("harrington",45,"bold"),width=38,fg="lime",bg="black")
lb1.grid(row=0,column=0)

body=Frame(win,height=400,width=400,bg="black",relief="sunken",bd=10,padx=40)
body.pack()

booklist=Frame(win,height=100,width=100,bd=1,relief='sunken')
booklist.pack()
lb=Label(booklist,text="Book Name",font=("Comic Sans MS",10,"bold")).grid(row=0,column=0,sticky=W,padx=13,pady=2)
lb=Label(booklist,text="ISBN",font=("Comic Sans MS",10,"bold")).grid(row=0,column=1,sticky=W,padx=13,pady=2)
lb=Label(booklist,text="Date of Issue",font=("Comic Sans MS",10,"bold")).grid(row=0,column=2,sticky=W,padx=13,pady=2)
lb=Label(booklist,text="Last Date of Return",font=("Comic Sans MS",10,"bold")).grid(row=0,column=3,sticky=W,padx=13,pady=2)

def book_list():
    rn=r.get()
    con=pymysql.connect(host='localhost',user='root',password='',db='library')
    cr=con.cursor()
    cr.execute("select book_name,isbn,issue_date,return_date from issuebook where rollno='"+rn+"'")
    result=cr.fetchall()
    count=cr.rowcount

    if(count>0):
        l = len(result[0])
        for rw in range(count):
            for cl in range(l):
                lb=Label(booklist,text=result[rw][cl],font=("Comic Sans MS",10),borderwidth=1)
                lb.grid(row=rw+1,column=cl,sticky=W,padx=13,pady=1)
        #r.set('')

    else:
        lb=Label(booklist,text="No Books Issued For Now",font=("Comic Sans MS",10),borderwidth=1).grid(row=4,column=0,columnspan=6,padx=13)
        #messagebox.showinfo("Error","Oops, Something Went Wrong in Query2!!! ")
    con.close()
#def totdet():
#    sdetails()
#    book_list()


lb11=Label(body,text="Enter Roll No to pull record",fg="orange",bg="black",font=("harrington",25,"bold"))
lb11.grid(row=0,column=0,pady=5,columnspan=2,sticky=W)

lb12=Label(body,text="Roll Number",fg="lime",bg="black",font=("harrington",20,"bold"))
lb12.grid(row=1,column=0,sticky=W)

r=StringVar()
tb11=Entry(body,textvariable=r,bg="black",fg="white")
tb11.grid(row=1,column=1)

btn=Button(body,text="Submit",font=("harrington",15,"bold"),relief="groove",fg="yellow",bg="black",command=sdetails)
btn.grid(row=2,column=0,columnspan=2,pady=5,padx=10)

can=Canvas(body,height=10,width=450,bd=0,relief="flat")
oval=can.create_line(0, 5, 452, 5,fill="green",width=13)
can.grid(row=3,column=0,columnspan=2)

lb2=Label(body,text="Roll Number ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb2.grid(row=4,column=0,sticky=W)

a=StringVar()
tb1=Entry(body,textvariable=a,bg="black",fg="white")
tb1.grid(row=4,column=1)

lb3=Label(body,text="Student Name ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb3.grid(row=5,column=0,sticky=W)

b=StringVar()
tb2=Entry(body,textvariable=b,bg="black",fg="white")
tb2.grid(row=5,column=1)

lb4=Label(body,text="Father's Name ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb4.grid(row=6,column=0,sticky=W)

c=StringVar()
tb3=Entry(body,textvariable=c,bg="black",fg="white")
tb3.grid(row=6,column=1)

lb5=Label(body,text="Contact ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb5.grid(row=7,column=0,sticky=W)

d=StringVar()
tb4=Entry(body,textvariable=d,bg="black",fg="white")
tb4.grid(row=7,column=1)

lb6=Label(body,text="D.O.B ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb6.grid(row=8,column=0,sticky=W)

e=StringVar()
tb5=Entry(body,textvariable=e,bg="black",fg="white")
tb5.grid(row=8,column=1)

lb7=Label(body,text="Branch ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb7.grid(row=9,column=0,sticky=W)

f=StringVar()
tb6=Entry(body,textvariable=f,bg="black",fg="white")
tb6.grid(row=9,column=1)

lb8=Label(body,text="Fine ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb8.grid(row=10,column=0,sticky=W)

g=StringVar()
tb7=Entry(body,textvariable=g,bg="black",fg="white")
tb7.grid(row=10,column=1)

ubtn=Button(body,text='Update',justify=CENTER,font=("harrington",15,"bold"),relief="groove",fg="yellow",bg="black",command=update)
ubtn.grid(row=11,column=0)

dbtn=Button(body,text='Delete',justify=CENTER,font=("harrington",15,"bold"),relief="groove",fg="yellow",bg="black",command=dels)
dbtn.grid(row=11,column=1)


win.mainloop()
