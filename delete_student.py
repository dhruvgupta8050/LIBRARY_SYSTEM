from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image,ImageFilter
import os
import pymysql
def admin():
    win.destroy()
    os.system('adminarea.py')

def dels():
    rn=a.get()
    try:
        con=pymysql.connect(host='localhost',user='root',password='',db='library')
        c=con.cursor()
        c.execute("delete from student where rollno='"+rn+"'")
        con.commit()
        messagebox.showinfo("Message", "Student Record Deleted")
        a.set('')

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

pic=Image.open('dels.jpg')
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

lb1=Label(header,text="DELETE STUDENT",font=("harrington",45,"bold"),width=38,fg="lime",bg="black")
lb1.grid(row=0,column=0)

body=Frame(win,height=400,width=400,bg="black",relief="sunken",bd=10,padx=40,pady=40)
body.pack(pady=40)

lb2=Label(body,text="Roll Number ",fg="lime",bg="black",font=("harrington",20,"bold"))
lb2.grid(row=0,column=0,pady=10,sticky=W)

a=StringVar()
tb1=Entry(body,textvariable=a,bg="black",fg="white")
tb1.grid(row=0,column=1)

#lb3=Label(body,text="ISBN ",fg="lime",bg="black",font=("harrington",20,"bold"))
#lb3.grid(row=1,column=0,sticky=W)

#b=StringVar()
#tb2=Entry(body,textvariable=b,bg="black",fg="white",show="*")
#tb2.grid(row=1,column=1)

btn=Button(body,text="Submit",font=("harrington",20,"bold"),relief="groove",fg="yellow",bg="black",command=dels)
btn.grid(row=1,column=0,columnspan=2,pady=10,padx=10)

win.mainloop()
