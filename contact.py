from tkinter import Tk,PhotoImage,Button,Label,LabelFrame,W,E,N,S, Entry,END,StringVar,Scrollbar,Toplevel
from tkinter import ttk
import sqlite3
class Contacts:
    db_fileName='app.db'
    def __init__(self,root):
        self.root = root
        self.create_GUI()
        ttk.style.configure("Treeview",font=('helvetica',10))
        ttk.style.configure("Treeview.Heading",font=('helvetica' ,12,'bold'))
    

    def create_GUI(self):
        self.create_left_logo()
        self.create_label_frame()
        self.create_message_area()
        self.create_treeview()
        self.create_scrollbar()
        self.create_button()
        ttk.style = ttk.Style()
    def create_left_logo(self):
        photo=PhotoImage(file="C:/Users/shahw/PycharmProjects/CurdAppliationPython/logo/logo.gif")
        label=Label(image=photo)
        label.image=photo
        label.grid(row=0,column=0)
    def create_label_frame(self):
        labelframe= LabelFrame(self.root,text="Create New Contact",bg="sky blue",font="helvetica 10")
        labelframe.grid(row=0,column=1,padx=8,pady=8,sticky="ew")
        Label(labelframe,text="Name",bg="black",fg="white").grid(row=1,column=1,sticky=W,padx=2,pady=15)
        self.namefield=Entry(labelframe).grid(row=1,column=2,sticky=W,padx=5,pady=2)
        Label(labelframe, text="Email", bg="black", fg="white").grid(row=2, column=1, sticky=W, padx=2, pady=15)
        self.emailfield = Entry(labelframe).grid(row=2, column=2, sticky=W, padx=5, pady=2)
        Label(labelframe, text="Number", bg="black", fg="white").grid(row=3, column=1, sticky=W, padx=2, pady=15)
        self.numfield = Entry(labelframe).grid(row=3, column=2, sticky=W, padx=5, pady=2)
        Button(labelframe,text="Add Contact",command="",bg="blue",fg="white").grid(row=4,column=2,sticky=E,padx=5,pady=5)
    def create_message_area(self):
        self.message=Label(text="",fg="red").grid(row=3,column=1,sticky=W)

    def create_treeview(self):
        self.tree=ttk.Treeview(height=10,column=("email","number"),style='Treeview')
        self.tree.grid(row=6,column=0,columnspan=3)
        self.tree.heading('#0',text="Name",anchor=W)
        self.tree.heading('email',text="Email",anchor=W)
        self.tree.heading("number",text="Number",anchor=W)
    def create_scrollbar(self):
        self.scrollbar=Scrollbar(orient='vertical',command=self.tree.yview)
        self.scrollbar.grid(row=6,column=3,rowspan=10,sticky='sn')
    def create_button(self):
        Button(text="Delete Selected",command="",bg="red",fg="white").grid(row=8,column=0,sticky=W,padx=50,pady=10)
        Button(text="Update Selected",command="",bg="purple",fg="white").grid(row=8,column=1,sticky=W)

if __name__ == '__main__':
    root=Tk()
    root.title("User Information")
    application=Contacts(root)
    root.mainloop()