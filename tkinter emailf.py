from tkinter import*
root=Tk()
root.title('login app')
root.geometry('400x400')
frame=Frame(master=root,height=200,width=360,bg="#d0efff")

lbl1=Label(text="Full name",bg="#3895D3",fg="blue")
lbl2=Label(text="Email Id",bg="#3895D3",fg="white")
lbl3=Label(text="Enter password",bg="#7863E9",fg="Pink")

name_entry=Entry(frame)
email_entry=Entry(frame)
pass_entry=Entry(frame,show="*")

def display():
    name=name_entry.get()
    greet="Hey there! "+name
    message="\n congragulations for your new acc."
    textbox.insert(END , greet)
    textbox.insert(END,message)

textbox=Text(bg="#BEBEBE",fg="black")

btn=Button(text="Create an acc.",command=display,bg="red")
 
frame.place(x=20,y=0)
lbl1.place(x=20,y=20)
name_entry.place(x=150,y=20)
lbl2.place(x=20,y=80)
email_entry.place(x=150,y=80)
lbl3.place(x=20,y=140)
pass_entry.place(x=150,y=140)
btn.place(x=130,y=210)
textbox.place(y=250)

root.mainloop()