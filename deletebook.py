from tkinter import *
from tkinter import ttk 
import sqlite3
from tkinter import messagebox

con=sqlite3.connect('library.db')
cur=con.cursor()
class DelBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Delete Book")
        self.resizable(False,False)

        query="SELECT * FROM books"
        books=cur.execute(query).fetchall()
        book_list=[]
        for book in books:
                book_list.append(str(book[0])+"-"+book[1])

#top frame
        self.topFrame=Frame(self,height=100,bg='white')
        self.topFrame.pack(fill=X)
#bottom frame
        self.bottomFrame=Frame(self,height=600,bg='pink')
        self.bottomFrame.pack(fill=X)
#heading image
        self.top_image=PhotoImage(file='del4.png')
        top_image_lbl=Label(self.topFrame,image=self.top_image,bg='white')
        top_image_lbl.place(x=120,y=10)
        heading=Label(self.topFrame,text='DELETE BOOKS',font='arial 25 bold',fg='black',bg='white')
        heading.place(x=290,y=60)
###############################################entries and labels################################################
#name
        self.book_name=StringVar()
        self.lbl_name=Label(self.bottomFrame,text="BOOK NAME:",font='arial 15 bold',fg='black',bg='pink')
        self.lbl_name.place(x=30,y=40) 
        self.combo_name=ttk.Combobox(self.bottomFrame,textvariable=self.book_name)
        self.combo_name['values']=book_list
        self.combo_name.place(x=200,y=45)
#button
        button=Button(self.bottomFrame,text='Delete Book',fg='red',font='arial 15 bold',command=self.delBook)
        button.place(x=270,y=200)
    def delBook(self):
        book_name=self.book_name.get()
        self.book_id=book_name.split("-")[0]
        if (book_name!=""):
            try:
                query="DELETE FROM 'BOOKS' WHERE book_id=?"
                cur.execute(query,(self.book_id))
                con.commit()
                messagebox.showinfo("Success","Successfully deleted from database",icon='info')
            except:
                messagebox.showerror("Error","Cant delete from database",icon='warning')
        else:
                messagebox.showerror("Error","Feild cant be empty",icon='warning')