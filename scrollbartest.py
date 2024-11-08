from tkinter import*
import pymysql
from tkinter import messagebox
def populate():
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
                    lb=Label(frame,text=result[r][c],borderwidth=1,font=("Comic Sans MS",10)).grid(row=r+1,column=c,padx=13,pady=2)

    except:
        con.rollback()
        messagebox.showinfo("Error","Oops, Some Error Occured!!!")
    con.close()

#    for row in range(100):
#        Label(frame, text="%s" % row, width=3, borderwidth="1",
#                 relief="solid").grid(row=row+1, column=0)
#        t="this is the second column for row %s" %row
#        Label(frame, text=t).grid(row=row+1, column=1)

def onFrameConfigure():
    '''Reset the scroll region to encompass the inner frame'''
    can.configure(scrollregion=can.bbox("all"))

root = Tk()
root.geometry("600x400")
can = Canvas(root, borderwidth=0, background="#ffffff")
frame = Frame(can, background="#ffffff")
frame.pack(fill="both", expand=True)
vsb = Scrollbar(can, orient="vertical", command=can.yview)
can.configure(yscrollcommand=vsb.set)

vsb.pack( side='right',fill="y")
can.pack( fill="both", expand=True)
can.create_window((4,4), window=frame, anchor="nw")
populate()

frame.bind("<Configure>", lambda event, canvs=can: onFrameConfigure())


root.mainloop()