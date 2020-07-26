from Tkinter import *
root=Tk()
root.geometry('650x400')
Label(root,text='About The Developer',font='Arial 60').grid(row=0,column=2)
Label(root,text='PYTHON and DBMS Project',font='Comic 30').grid(row=1,column=2)
Label(root,text='The Developer of this program is AKSHAT UPADHYAY who developed the program under guidance\n of Mr.Nilesh Patel and Mr. Mahesh Kumar. The program is a Contactbook\nof what we see in our mobilephones').grid(row=2,column=2)
Label(root,text='move mouse on screen to close',fg='red').grid(row=4,column=2)
def f(e=1):
    root.destroy()
root.bind('<Motion>',f)
root.mainloop()
