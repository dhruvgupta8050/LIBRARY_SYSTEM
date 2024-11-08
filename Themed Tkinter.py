from tkinter import*
win=Tk()
from tkinter import ttk
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

l1 = ttk.Label(text="Test", style="BW.TLabel").grid(row=0,column=0)
l2 = ttk.Label(text="Test", style="BW.TLabel").grid(row=0,column=1)
cb=ttk.Combobox(values="Option1 Option2 Option3 ")
cb2=ttk.Combobox(value="0 1 2 3 4 5 6")
print(cb2.location)
cb2.grid(row=2,column=0)
cb.grid(row=1,column=0)
win.mainloop()