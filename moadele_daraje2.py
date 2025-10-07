from tkinter import *
from tkinter import messagebox
import math

def on_enter1(e):
    delete_btn.config(background="#D2691E",fg="white",cursor="hand2")
def on_leave1(e):
    delete_btn.config(background="orange",fg="white",cursor="arrow")

def on_enter2(e):
    enter_btn.config(background="#00FA9A",fg="white",cursor="hand2")
def on_leave2(e):
    enter_btn.config(background="green",fg="white",cursor="arrow")
def on_enter3(e):
    close_btn.config(background="white",fg="black",cursor="hand2")
def on_leave3(e):
    close_btn.config(background="black",foreground="white",cursor="arrow")
    
def delte():
    entry_A.delete(0,END)
    entry_B.delete(0,END)
    entry_c.delete(0,END)
    
def close():
    win.destroy()

def click():
    try:
        a = int(entry_A.get())
        b = int(entry_B.get())
        c = int(entry_c.get())
        x = (b ** 2) - 4 * a * c
        
        if x < 0:
            natije = "rishe haghighi nadarad"
        if x == 0:
            pc3 = -b / (2 * a)
            natije = f"rishe moza af ast \n {pc3}"
        if x > 0:
            pc1 = (-b - math.sqrt(x)) / (2 * a)
            pc2 = (-b + math.sqrt(x)) / (2 * a)
            natije = f"2 rishe ahghighi dard = {pc1} va {pc2}"
            
        
        new = Toplevel(win)
        new.title("natije")
        new.geometry("500x500")
        new.resizable(False,False)
        new.config(background="green")
        
        new_lable = Label(new,text=f"{natije}",font=("arial",16),width=20,bg="orange",fg="blue")
        new_lable.pack(padx=10,pady=10)
        
        new_btn = Button(new,text="close",width=20,font=("arial",16),bg="red",fg="white",command=new.destroy)
        new_btn.pack(padx=10,pady=10)
        
        new.mainloop()
    except ValueError:
        messagebox.showinfo("please enter your number")
            
            
        
win = Tk()
win.title("moadele daraje 2")
win.geometry("520x520")
win.resizable(False,False)
win.config(background="dark red")

lable_A = Label(win,text="A",font=("arial",17),width=11,bg="purple",fg="white")
lable_A.pack(padx=10,pady=10)

entry_A = Entry(win,bg="#66CDAA",fg="white",justify=CENTER,width=16,font=("arial",17))
entry_A.pack(padx=10,pady=10)

lable_B = Label(win,text="B",font=("arial",17),width=11,bg="purple",fg="white")
lable_B.pack(padx=10,pady=10)

entry_B = Entry(win,bg="#66CDAA",fg="white",justify=CENTER,width=16,font=("arial",17))
entry_B.pack(padx=10,pady=10)

lable_c = Label(win,text="C",font=("arial",17),width=11,bg="purple",fg="white")
lable_c.pack(padx=10,pady=10)

entry_c = Entry(win,bg="#66CDAA",fg="white",justify=CENTER,width=16,font=("arial",17))
entry_c.pack(padx=10,pady=10)


delete_btn = Button(win,text="delete",font=("Arial",16),bg="orange",fg="white",width=20,command=delte)
delete_btn.pack(padx=10,pady=10)

enter_btn = Button(win,text="Enter",font=("arial",16),bg="green",fg="white",width=20,command=click)
enter_btn.pack(padx=10,pady=10)

close_btn = Button(win,text="close",width=20,font=("arial",16),bg="white",fg="black",command=close)
close_btn.pack(padx=10,pady=10)


win.mainloop()




