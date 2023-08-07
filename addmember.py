from tkinter import *
from tkinter import messagebox
import sqlite3
con=sqlite3.connect('library.db')
cur=con.cursor()

class AddMember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Add Member")
        self.resizable(False,False)
####################################################frames#######################################################
#top frame
        self.topFrame=Frame(self,height=100,bg='white')
        self.topFrame.pack(fill=X)
#bottom frame
        self.bottomFrame=Frame(self,height=600,bg='pink')
        self.bottomFrame.pack(fill=X)
#heading image
        self.top_image=PhotoImage(file='user1.png')
        top_image_lbl=Label(self.topFrame,image=self.top_image,bg='white')
        top_image_lbl.place(x=120,y=10)
        heading=Label(self.topFrame,text='Add Member',font='arial 25 bold',fg='black',bg='white')
        heading.place(x=290,y=60)
###############################################entries and labels################################################
#name
        self.lbl_name=Label(self.bottomFrame,text="NAME:",font='arial 15 bold',fg='black',bg='pink')
        self.lbl_name.place(x=30,y=40)
        self.ent_name=Entry(self.bottomFrame,width=30,bd=4)
        self.ent_name.insert(0,"please enter name")
        self.ent_name.place(x=150,y=45)
#phone
        self.lbl_phone=Label(self.bottomFrame,text="PH.NO.:",font='arial 15 bold',fg='black',bg='pink')
        self.lbl_phone.place(x=30,y=80)
        self.ent_phone=Entry(self.bottomFrame,width=30,bd=4)
        self.ent_phone.insert(0,"please enter phone number")
        self.ent_phone.place(x=150,y=85)
#button
        button=Button(self.bottomFrame,text='Add Member',fg='red',font='arial 15 bold',command=self.addMember)
        button.place(x=270,y=200)
    def addMember(self):
        name=self.ent_name.get()
        phone=self.ent_phone.get()
        if (name and phone !=""):
            try:
                query="INSERT INTO 'Members' (Member_name,Member_phone) VALUES(?,?)"
                cur.execute(query,(name,phone))
                con.commit()
                messagebox.showinfo("Success","Successfully added to database",icon='info')
            except:
                messagebox.showerror("Error","Cant add to database",icon='warning')
        else:
                messagebox.showerror("Error","Feild cant be empty",icon='warning')