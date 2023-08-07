from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

con=sqlite3.connect('library.db')
cur=con.cursor()

class ReturnBook(Toplevel):
  def __init__(self):
    Toplevel.__init__(self)
    self.geometry("650x750+550+200")
    self.title("Lend Book")
    self.resizable(False,False)
    self.iconbitmap('returnbook.ico')

    query="SELECT * FROM books WHERE book_status=1"
    books=cur.execute(query).fetchall()
    book_list=[]
    for book in books:
      book_list.append(str(book[0])+"-"+book[1])


################################Frames##############################
    #Top Frame
    self.topFrame=Frame(self,height=150,bg='WHITE')
    self.topFrame.pack(fill=X)

    #Bottom Frame
    self.bottomFrame=Frame(self,height=600,bg='PINK')
    self.bottomFrame.pack(fill=X)

    #heading,image
    self.top_image=PhotoImage(file='lendbook.png')
    top_image_lbl=Label(self.topFrame,image=self.top_image,bg='white')
    top_image_lbl.place(x=120,y=10)
    heading=Label(self.topFrame,text='RETURN BOOK',font='arial 22 bold',fg='BLACK',bg='white')
    heading.place(x=290,y=60)

############################################Entries and Labels########################################
        
    #book name
    self.book_name=StringVar()
    self.lbl_name=Label(self.bottomFrame,text='Book Name:',font='arial 15 bold',fg='white',bg='PINK')
    self.lbl_name.place(x=40,y=40)
    self.combo_name=ttk.Combobox(self.bottomFrame,textvariable=self.book_name,width=50)
    self.combo_name['values']=book_list
    self.combo_name.place(x=200,y=45)

    #Button
    button=Button(self.bottomFrame,text='Return Book',command=self.returnBook)
    button.place(x=450,y=120)

  def returnBook(self):
    book_name=self.book_name.get()
    self.book_id=book_name.split('-')[0]

    if (book_name != ""):
      try:
        print("abhay")
        query="DELETE FROM 'borrowers' WHERE bbook_id=?"
        cur.execute(query,(self.book_id))
        con.commit()
        messagebox.showinfo("Success","Successfully added to database!",icon='info')
        cur.execute("UPDATE books SET book_status=? WHERE book_id=?",(0,self.book_id))
        con.commit()

      except:
        messagebox.showerror("Error","Can't add to Database",icon='warning')

    else:
      messagebox.showerror("Error","Fields can't be empty",icon='warning')