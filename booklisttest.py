from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image,ImageFilter
import pymysql
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


def book_list():
    rn=r.get()
    con=pymysql.connect(host='localhost',user='root',password='',db='library')
    cr=con.cursor()
    cr.execute("select book_name,isbn,issue_date,return_date from issuebook where rollno='"+rn+"'")
    result=cr.fetchall()
    count=cr.rowcount
    l=len(result[0])
    if(count>0):
        for rw in range(count):
            for cl in range(l):
                lb=Label(booklist,text=result[rw][cl]).grid(row=rw+1,column=cl)
    else:
        messagebox.showinfo("Error","Oops, Something Went Wrong!!!")
    con.close()



body=Frame(win,height=400,width=400,bg="black",relief="sunken",bd=10,padx=40)
body.pack(pady=10)

booklist=Frame(win,height=100,width=100,bd=10,relief='sunken')
booklist.pack()

lb11=Label(body,text="Enter Roll No to pull record",fg="orange",bg="black",font=("harrington",25,"bold"))
lb11.grid(row=0,column=0,pady=5,columnspan=2,sticky=W)

lb12=Label(body,text="Roll Number",fg="lime",bg="black",font=("harrington",20,"bold"))
lb12.grid(row=1,column=0,sticky=W)

r=StringVar()
tb11=Entry(body,textvariable=r,bg="black",fg="white")
tb11.grid(row=1,column=1)

btn=Button(body,text="Submit",font=("harrington",15,"bold"),relief="groove",fg="yellow",bg="black",command=book_list)
btn.grid(row=2,column=0,columnspan=2,pady=5,padx=10)

lb=Label(booklist,text="Book Name").grid(row=0,column=0)
lb=Label(booklist,text="ISBN").grid(row=0,column=1)
lb=Label(booklist,text="Date of Issue").grid(row=0,column=2)
lb=Label(booklist,text="Last Date of Return").grid(row=0,column=3)

win.mainloop()