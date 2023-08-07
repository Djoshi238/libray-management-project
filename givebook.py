from tkinter import *
from tkinter import ttk 
import sqlite3

from tkinter import messagebox
con=sqlite3.connect('library.db')
cur=con.cursor()
class GiveBook(Toplevel):
        def __init__(self):
                Toplevel.__init__(self)
                self.geometry("650x750+550+200")
                self.title("Lend Book")
                self.resizable(False,False)
                query="SELECT * FROM books"
                books=cur.execute(query).fetchall()
                book_list=[]
                for book in books:
                        book_list.append(str(book[0])+"-"+book[1])
                query2="SELECT* FROM MEMBERS"
                members=cur.execute(query2).fetchall()
                member_list=[]
                for member in members:
                        member_list.append(str(member[0])+"-"+member[1])
                #top frame
                self.topFrame=Frame(self,height=150,bg='white')
                self.topFrame.pack(fill=X)
#bottom frame
                self.bottomFrame=Frame(self,height=600,bg='pink')
                self.bottomFrame.pack(fill=X)
#heading image
                self.top_image=PhotoImage(file='LEND1.png')
                top_image_lbl=Label(self.topFrame,image=self.top_image,bg='white')
                top_image_lbl.place(x=150,y=10)
                heading=Label(self.topFrame,text='LEND BOOK',font='arial 25 bold',fg='black',bg='white')
                heading.place(x=290,y=60)
###############################################entries and labels################################################
#BOOK name
                self.book_name=StringVar()
                self.lbl_name=Label(self.bottomFrame,text="BOOK NAME:",font='arial 15 bold',fg='black',bg='pink')
                self.lbl_name.place(x=30,y=40) 
                self.combo_name=ttk.Combobox(self.bottomFrame,textvariable=self.book_name)
                self.combo_name['values']=book_list
                self.combo_name.place(x=200,y=45)
#MEMBER NAME
                self.member_name=StringVar()
                self.lbl_phone=Label(self.bottomFrame,text="MEMBER NAME:",font='arial 15 bold',fg='black',bg='pink')
                self.lbl_phone.place(x=30,y=80)
                self.combo_member=ttk.Combobox(self.bottomFrame,textvariable=self.member_name)
                self.combo_member['values']=member_list
                self.combo_member.place(x=200,y=85)
#button
                button=Button(self.bottomFrame,text='LEND BOOK',command=self.lendBook)
                button.place(x=270,y=200)
        def lendBook(self):
                book_name=self.book_name.get()
                self.book_id=book_name.split("-")[0]
                member_name=self.member_name.get()
                if(book_name and member_name !=""):
                        try:
                                query="INSERT INTO 'BORROWERS'(bbook_id,bmember_id) VALUES(?,?)"
                                cur.execute(query,(book_name,member_name))
                                con.commit()
                                messagebox.showinfo("Success","Successfully added to database!",icon='info')
                                cur.execute("UPDATE books SET book_status=? WHERE book_id=?",(1,self.book_id))
                                con.commit()
                        except:    
                                 messagebox.showerror("ERROR","Cant add to database",icon='warning')
                else:
                        messagebox.showerror("ERROR","FEILD cant be empty",icon='warning')
