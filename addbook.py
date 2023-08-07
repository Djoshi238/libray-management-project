from tkinter import *
from tkinter import messagebox
import sqlite3
con=sqlite3.connect('library.db')
cur=con.cursor()

class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Add Book")
        self.resizable(False,False)
####################################################frames#######################################################
#top frame
        self.topFrame=Frame(self,height=100,bg='white')
        self.topFrame.pack(fill=X)
#bottom frame
        self.bottomFrame=Frame(self,height=600,bg='pink')
        self.bottomFrame.pack(fill=X)
#heading image
        self.top_image=PhotoImage(file='add2.png')
        top_image_lbl=Label(self.topFrame,image=self.top_image,bg='white')
        top_image_lbl.place(x=120,y=10)
        heading=Label(self.topFrame,text='ADD BOOKS',font='arial 25 bold',fg='black',bg='white')
        heading.place(x=290,y=60)
###############################################entries and labels################################################
#name
        self.lbl_name=Label(self.bottomFrame,text="NAME:",font='arial 15 bold',fg='black',bg='pink')
        self.lbl_name.place(x=30,y=40)
        self.ent_name=Entry(self.bottomFrame,width=30,bd=4)
        self.ent_name.insert(0,"please enter book name")
        self.ent_name.place(x=150,y=45)
#author
        self.lbl_author=Label(self.bottomFrame,text="AUTHOR:",font='arial 15 bold',fg='black',bg='pink')
        self.lbl_author.place(x=30,y=80)
        self.ent_author=Entry(self.bottomFrame,width=30,bd=4)
        self.ent_author.insert(0,"please enter author name")
        self.ent_author.place(x=150,y=85)
#page
        self.lbl_page=Label(self.bottomFrame,text="PAGE:",font='arial 15 bold',fg='black',bg='pink')
        self.lbl_page.place(x=30,y=120)
        self.ent_page=Entry(self.bottomFrame,width=30,bd=4)
        self.ent_page .insert(0,"please enter page number")
        self.ent_page.place(x=150,y=125)
#language
        self.lbl_language=Label(self.bottomFrame,text="LANGUAGE:",font='arial 15 bold',fg='black',bg='pink')
        self.lbl_language.place(x=30,y=160)
        self.ent_language=Entry(self.bottomFrame,width=30,bd=4)
        self.ent_language.insert(0,"please enter language name")
        self.ent_language.place(x=150,y=165)
#button
        button=Button(self.bottomFrame,text='Add Book',fg='red',font='arial 15 bold',command=self.addBook)
        button.place(x=270,y=200)
    def addBook(self):
        name=self.ent_name.get()
        author=self.ent_author.get()
        page=self.ent_page.get()
        language=self.ent_language.get()
        if (name and author and page and language !=""):
            try:
                query="INSERT INTO 'books' (book_name,book_author,book_pages,book_language) VALUES(?,?,?,?)"
                cur.execute(query,(name,author,page,language))
                con.commit()
                messagebox.showinfo("Success","Successfully added to database",icon='info')
            except:
                messagebox.showerror("Error","Cant add to database",icon='warning')
        else:
                messagebox.showerror("Error","Feild cant be empty",icon='warning')