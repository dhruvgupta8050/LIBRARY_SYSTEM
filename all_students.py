from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image,ImageFilter
import os
import pymysql
def admin():
    win.destroy()
    os.system('adminarea.py')

def show():
    try:
        con=pymysql.connect(host='localhost',user='root',password='',db='library')
        c=con.cursor()
        c.execute("select * from student order by rollno")
        result=c.fetchall()
        count=c.rowcount
        l=len(result[0])
        if(count>0):
            for r in range(count):
                for c in range(l):
                    lb=Label(details,text=result[r][c],borderwidth=1,font=("Comic Sans MS",10)).grid(row=r+1,column=c,padx=20,pady=3,sticky=W)

    except:
        con.rollback()
        messagebox.showinfo("Error","Oops, Some Error Occured!!!")
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

lb1=Label(header,text="ALL STUDENTS DETAIL",font=("harrington",45,"bold"),width=38,fg="lime",bg="black")
lb1.grid(row=0,column=0)


#Canvas to insert frame in it
canvas=Canvas(win,height=505,width=650)
canvas.pack(side=LEFT,fill=BOTH,expand=TRUE,padx=160)
vsb=Scrollbar(canvas,orient=VERTICAL,command=canvas.yview)
vsb.pack(side=RIGHT,fill=Y)
canvas.config(yscrollcommand=vsb.set)

details=Frame(canvas,height=400,width=600,relief="sunken")
details.pack(pady=5,fill=BOTH,expand=TRUE)
canvas.create_window((4,4),window=details,anchor=N)

def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

lb=Label(details,text="Roll Number",font=("Comic Sans MS",10,"bold")).grid(row=0,column=0,sticky=W,padx=20,pady=3)
lb=Label(details,text="Student Name",font=("Comic Sans MS",10,"bold")).grid(row=0,column=1,sticky=W,padx=20,pady=3)
lb=Label(details,text="Father's Name",font=("Comic Sans MS",10,"bold")).grid(row=0,column=2,sticky=W,padx=20,pady=3)
lb=Label(details,text="Contact",font=("Comic Sans MS",10,"bold")).grid(row=0,column=3,sticky=W,padx=20,pady=3)
lb=Label(details,text="DOB",font=("Comic Sans MS",10,"bold")).grid(row=0,column=4,sticky=W,padx=20,pady=3)
lb=Label(details,text="Branch",font=("Comic Sans MS",10,"bold")).grid(row=0,column=5,sticky=W,padx=20,pady=3)
lb=Label(details,text="Fine",font=("Comic Sans MS",10,"bold")).grid(row=0,column=6,sticky=W,padx=20,pady=3)

details.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
show()
win.mainloop()
