from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image,ImageFilter
import os
import pymysql
def admin():
    win.destroy()
    os.system('adminarea.py')

def adds():
    rn=a.get()
    sn=b.get()
    fn=c.get()
    pn=d.get()
    dob=e.get()
    br=f.get()
    if(rn=='' or sn=='' or fn=='' or pn=='' or dob=='' or br==''):
        messagebox.showinfo("Error","Empty Detail(s), Please Enter Details")
    else:
        try:

            con=pymysql.connect(host='localhost',user='root',password='',db='library')
            cr=con.cursor()
            cr.execute("insert into student(rollno,student_name,father_name,contact,dob,branch) values('"+rn+"','"+sn+"','"+fn+"','"+pn+"','"+dob+"','"+br+"')")
            con.commit()
            messagebox.showinfo("Message", "Student Added Successfully")
            a.set('')
            b.set('')
            c.set('')
            d.set('')
            e.set('')
            f.set('')

        except:
            con.rollback()
            messagebox.showinfo("Error","Student Not Added")
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

pic=Image.open('adds.jpg')
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

lb1=Label(header,text="ADD STUDENT",font=("harrington",45,"bold"),width=38,fg="lime",bg="black")
lb1.grid(row=0,column=0)

body=Frame(win,height=400,width=400,bg="black",relief="sunken",bd=10,padx=40,pady=40)
body.pack(pady=40)

lb2=Label(body,text="Roll Number ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb2.grid(row=0,column=0,sticky=W)

a=StringVar()
tb1=Entry(body,textvariable=a,bg="black",fg="white")
tb1.grid(row=0,column=1)

lb3=Label(body,text="Student Name ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb3.grid(row=1,column=0,sticky=W)

b=StringVar()
tb2=Entry(body,textvariable=b,bg="black",fg="white")
tb2.grid(row=1,column=1)

lb4=Label(body,text="Father's Name ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb4.grid(row=2,column=0,sticky=W)

c=StringVar()
tb3=Entry(body,textvariable=c,bg="black",fg="white")
tb3.grid(row=2,column=1)

lb5=Label(body,text="Contact ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb5.grid(row=3,column=0,sticky=W)

d=StringVar()
tb4=Entry(body,textvariable=d,bg="black",fg="white")
tb4.grid(row=3,column=1)

lb6=Label(body,text="D.O.B ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb6.grid(row=4,column=0,sticky=W)

e=StringVar()
tb5=Entry(body,textvariable=e,bg="black",fg="white")
tb5.grid(row=4,column=1)

lb7=Label(body,text="Branch ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb7.grid(row=5,column=0,sticky=W)

f=StringVar()
tb6=Entry(body,textvariable=f,bg="black",fg="white")
tb6.grid(row=5,column=1)

btn=Button(body,text="Submit",font=("harrington",20,"bold"),relief="groove",fg="yellow",bg="black",command=adds)
btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10)

win.mainloop()
