from tkinter import *
from tkinter import ttk 
import sqlite3
import addbook,addmember,givebook,deletebook,returnbook,deletemember
from tkinter import messagebox
con=sqlite3.connect('library.db')
cur=con.cursor()

class Main(object):
  def __init__(self,master):
        self.master=master
        def displayStatistics(evt):
          count_books=cur.execute("select count(book_id) from books").fetchall()
          count_members=cur.execute("select count(member_id) from members").fetchall()
          taken_books=cur.execute("select count(book_status) from books where book_status=1").fetchall()     
          print(count_books)
          self.lbl_book_count.config(text='total:'+str(count_books[0][0])+'books in library')
          self.lbl_member_count.config(text='total member:'+str(count_members[0][0]))
          self.lbl_taken_count.config(text='taken books:'+str(taken_books[0][0]))
        def displayBooks(self):
                books=cur.execute("select* from books").fetchall()
                count=0
                for book in books:
                        print(book)
                        self.list_books.insert(count ,str(book[0])+"-"+book[1])
                        count+=1
                def bookInfo(evt):
                        value=str(self.list_books.get(self.list_books.curselection()))
                        id=value.split('-')[0]
                        book=cur.execute("SELECT *FROM BOOKS WHERE book_id=?",(id))
                        book_info=book.fetchall()
                        print(book_info)
                        self.list_details.delete(0,'end')
                        self.list_details.insert(1,"BOOK NAME :"+book_info[0][1])
                        self.list_details.insert(2,"AUTHOR :"+book_info[0][2])
                        self.list_details.insert(3,"PAGE :"+book_info[0][3])
                        self.list_details.insert(4,"LANGUAGE :"+book_info[0][4])
                        if book_info[0][5]==0:
                                self.list_details.insert(4,'STATUS:AVAILABLE')
                        else:
                                self.list_details.insert(4,'STATUS:NOT AVAILABLE')
                def doubleClick(evt):
                        value=str(self.list_books.get(self.list_books.curselection()))
                        global given_id
                        given_id=value.split('-')[0]
                        given_book=GiveBook()
                        print(value)
                self.list_books.bind('<<ListboxSelect>>',bookInfo)
                self.tabs.bind('<<NotebookTabChanged>>',displayStatistics)
                #self.tabs.bind("<buttonrelease-1>",displayBooks)
                self.list_books.bind("<Double-Button-1>",doubleClick)
        #frames 
        mainFrame=Frame(self.master)
        mainFrame.pack()
        #top frames
        topFrame=Frame(mainFrame,width=1350,height=20,bg='pink',padx=20,borderwidth=2,relief=RIDGE)
        topFrame.pack(side=TOP,fill=X)
        #center frame
        centerFrame= Frame(mainFrame,width=1350,relief=SUNKEN,bg='grey',height=680)
        centerFrame.pack(side=TOP)
        #center left frame
        centerLeftFrame=Frame(centerFrame,width=900,height=700,bg='#f0f0f0',borderwidth=2,relief=SUNKEN)
        centerLeftFrame.pack(side=LEFT)
        #center right frame
        centerRightFrame=Frame(centerFrame,width=450,height=700,bg='#e0f0f0',borderwidth=2,relief=SUNKEN)
        centerRightFrame.pack()
        #search bar
        search_bar = LabelFrame(centerRightFrame,width=440,height=75,text='SEARCH BOX',bg='#9bc9ff')
        search_bar.pack(fill=BOTH)
        self.lbl_search=Label(search_bar,text='Search:',font='arial 12 bold',bg='#9bc9ff',fg='white')
        self.lbl_search.grid(row=0,column=0,padx=20,pady=10)
        self.ent_search=Entry(search_bar,width=30,bd=10)
        self.ent_search.grid(row=0,column=1,columnspan=3,padx=10,pady=10)
        self.btn_search=Button(search_bar,text='Search',font='arial 12',bg='#fcc324',fg='white',command=self.searchBooks)
        self.btn_search.grid(row=0,column=4,padx=20,pady=10)
        #list bar
        list_bar= LabelFrame(centerRightFrame,width=440,height=175,text='LIST BOX',bg='#fcc324')
        list_bar.pack(fill=BOTH)
        lbl_list=Label(list_bar,text='sort by',font='times 16 bold',fg='#2488ff',bg='#fcc324')
        lbl_list.grid(row=0,column=2)
        self.listChoice=IntVar()
        rb1=Radiobutton(list_bar,text='All Books',var=self.listChoice,value=1,bg='#fcc324')
        rb2=Radiobutton(list_bar,text='In Library',var=self.listChoice,value=2,bg='#fcc324')
        rb3=Radiobutton(list_bar,text='Borrowed By',var=self.listChoice,value=3,bg='#fcc324')
        rb1.grid(row=1,column=0)
        rb2.grid(row=1,column=1)
        rb3.grid(row=1,column=2)
        btn_list= Button(list_bar,text="list books",bg="#2488ff",fg='white',font='arial 12',command=self.listBooks)
        btn_list.grid(row=1,column=3,padx=40,pady=10)
        #title and image
        image_bar=Frame(centerRightFrame,width=440,height=350)
        image_bar.pack(fill=BOTH)
        self.title_right=Label(image_bar,text='Welcome to GBPIET Library',font='arial 30 bold')
        self.title_right.grid(row=0)
        self.img_library=PhotoImage(file='librarys.png')
        self.lblImg=Label(image_bar,image=self.img_library)
        self.lblImg.grid(row=1)

###############################################Tool Bar#########################################################

        #add book 
        self.iconbook=PhotoImage(file='adds.png')
        self.btnbook=Button(topFrame,text="ADD BOOKS",image=self.iconbook,compound=LEFT,font='aerial 12 bold',command=self.addBook)
        self.btnbook.pack(side=LEFT,padx=10)
        #Add member button 
        self.iconmember=PhotoImage(file='member.png')
        self.btnmember=Button(topFrame,text="ADD MEMBER",font='arial 12 bold',padx=10,command=self.addMember)
        self.btnmember.configure(image=self.iconmember,compound=LEFT)
        self.btnmember.pack(side=LEFT) 
        #ISSUE BOOK
        self.icongive=PhotoImage(file='issue.png')
        self.btngive=Button(topFrame,text='ISSUE BOOKS',font='arial 12 bold',padx=10)
        self.btngive.configure(image=self.icongive,compound=LEFT,command=self.giveBook)
        self.btngive.pack(side=LEFT)
        #del book 
        self.icondel=PhotoImage(file='del1.png')
        self.btndel=Button(topFrame,text="DELETE BOOKS",image=self.icondel,compound=LEFT,font='aerial 12 bold',command=self.delBook)
        self.btndel.pack(side=LEFT,padx=10)
        #return Book
        self.iconreturn=PhotoImage(file='returnbook.png')
        self.btnbook=Button(topFrame,text='RETURN BOOK',image=self.iconreturn,compound=LEFT,font='arial 12 bold',padx=10,command=self.returnBook)
        self.btnbook.pack(side=LEFT)
        #del member
        self.icondelm=PhotoImage(file='del3.png')
        self.btndelm=Button(topFrame,text="DELETE MEMBER",image=self.icondelm,compound=LEFT,font='aerial 12 bold',command=self.delMember)
        self.btndelm.pack(side=LEFT,padx=10)

       
######################################################Tabs#######################################################
######################################################tab1#######################################################
        self.tabs=ttk.Notebook(centerLeftFrame,width=900,height=660)
        self.tabs.pack()
        self.tab1_icon=PhotoImage(file='book.png')
        self.tab2_icon=PhotoImage(file='persons.png')
        self.tab1=ttk.Frame(self.tabs)
        self.tab2=ttk.Frame(self.tabs)
        self.tabs.add(self.tab1,text="Library management",image=self.tab1_icon,compound=LEFT)
        self.tabs.add(self.tab2,text="Statistics",image=self.tab2_icon,compound=LEFT)

        #list books
        self.list_books=Listbox(self.tab1,width=40,height=30,bd=5,font='times 12 bold')
        self.sb=Scrollbar(self.tab1,orient=VERTICAL)
        self.list_books.grid(row=0,column=0,padx=(10,0),pady=10,sticky=N)
        self.sb.config(command=self.list_books.yview)
        self.list_books.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0,column=0,sticky=N+S+E)
        #list details
        self.list_details=Listbox(self.tab1,width=80,height=30,bd=5,font='times 12 bold')
        self.list_details.grid(row=0,column=1,padx=(10,0),pady=10,sticky=N)
#####################################################tab2#######################################################
        #statistics
        self.lbl_book_count=Label(self.tab2,text="DIVYA",pady=20,font='verdana 14 bold')
        self.lbl_book_count.grid(row=0)
        self.lbl_member_count=Label(self.tab2,text="ABHAY",pady=20,font="verdana 14 bold")
        self.lbl_member_count.grid(row=1,sticky=W)
        self.lbl_taken_count=Label(self.tab2,text="",pady=20,font="verdana 14 bold")
        self.lbl_taken_count.grid(row=2,sticky=W)
        #fuctions
        displayBooks(self)
        displayStatistics(self)
  def addBook(self):
        add=addbook.AddBook()
  def addMember(self):
        member=addmember.AddMember()
  def searchBooks(self):
        value=self.ent_search.get()
        search=cur.execute("Select* from books where book_name LIKE ?",('%'+value+'%',)).fetchall()
        print(search)
        self.list_books.delete(0,END)
        count=0
        for book in search:
                self.list_books.insert(count,str(book[0])+"-"+(book[1]))
                count+=1
  def listBooks(self):
        value= self.listChoice.get()
        if value==1:
                allbooks=cur.execute("SELECT* FROM books").fetchall()
                self.list_books.delete(0,END)
                count=0
                for book in allbooks:
                        self.list_books.insert(count,str(book[0])+"-"+book[1]) 
                        count+=1
        elif value == 2:
                books_in_library=cur.execute("SELECT * FROM books WHERE book_status=?",(0,)).fetchall()
                self.list_books.delete(0,END)
                count=0
                for book in books_in_library:
                        self.list_books.insert(count,str(book[0])+"-"+book[1]) 
                        count+=1
        else:
                taken_books=cur.execute("SELECT * FROM books WHERE book_status=?",(1,)).fetchall()
                self.list_books.delete(0,END)
                count=0
                for book in taken_books:
                        self.list_books.insert(count,str(book[0])+"-"+book[1]) 
                        count+=1
       
  def giveBook(self):
                give_book=givebook.GiveBook()
  def returnBook(self):
        return_book=returnbook.ReturnBook()

  def delBook(self):
        delb=deletebook.DelBook()
  def delMember(self):
        delb=deletemember.DelMember()
class GiveBook(Toplevel):
        def __init__(self):
                Toplevel.__init__(self)
                self.geometry("650x750+550+200")
                self.title("Lend Book")
                self.resizable(False,False)
                global given_id
                self.book_id=int(given_id)
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
                self.combo_name.current(self.book_id-1)
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

def main():
    root=Tk()
    app=Main(root)
    root.title("GBPIET Library Management System")
    root.geometry("1350x750+350+200")
    root.iconbitmap("library.ico")
    root.mainloop()
if __name__ == '__main__':
    main() 