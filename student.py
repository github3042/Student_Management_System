from tkinter import *      # provide  GUI interface 
from tkinter import ttk  # provide combo box
import pymysql # fordatabase
from tkinter import messagebox  # to show validaation 
# from tkinter.font import BOLDfont
class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System") 
        self.root.geometry("1600x700+0+0")

        #  To create a label 
        title = Label(self.root,text="Student Management",bd = 10, relief = GROOVE,
        font = ("times new roman",40, 'bold'),bg = "#FFC0CB", fg = "black")
        title.pack(side=TOP, fill= X)

        # ========= All Variables ===========
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.address_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        # =============== Manage Frame ===================
        Manage_Frame = Frame(self.root, bd = 4, relief = RIDGE, bg = "#B6B6B4")
        Manage_Frame.place(x = 20, y = 100, width = 470, height = 600)

        m_title = Label(Manage_Frame,text = "Manage Student", bg = "#B6B6B4", fg = "black", font = ("times new roman", 30, 'bold'))
        m_title.grid(row = 0, columnspan=2, pady= 20)

        # Rollno
        lbl_roll = Label(Manage_Frame,text = "Roll No.", bg = "#B6B6B4", fg = "black", font = ("times new roman", 15, 'bold'))
        lbl_roll.grid(row = 1, column = 0, pady = 10, padx= 20, sticky = "w")

        txt_roll = Entry(Manage_Frame, textvariable = self.Roll_No_var, font = ("times new roman", 15, 'bold'), bd = 5, relief = GROOVE )
        txt_roll.grid(row = 1, column =1, pady = 10, padx= 20, sticky = "w")

        # Name
        lbl_name = Label(Manage_Frame,text = "Name", bg = "#B6B6B4", fg = "black", font = ("times new roman", 15, 'bold'))
        lbl_name.grid(row = 2, column =0, pady = 10, padx= 20, sticky = "w")

        txt_name = Entry(Manage_Frame, textvariable= self.name_var, font = ("times new roman", 15, 'bold'), bd = 5, relief = GROOVE )
        txt_name.grid(row = 2, column =1, pady = 10, padx= 20, sticky = "w")

        # Email
        lbl_email = Label(Manage_Frame,text = "Email", bg = "#B6B6B4", fg = "black", font = ("times new roman", 15, 'bold'))
        lbl_email.grid(row = 3, column = 0, pady = 10, padx= 20, sticky = "w")

        txt_email = Entry(Manage_Frame, textvariable= self.email_var, font = ("times new roman", 15, 'bold'), bd = 5, relief = GROOVE )
        txt_email.grid(row = 3, column =1, pady = 10, padx= 20, sticky = "w")

        # Gender
        lbl_gender = Label(Manage_Frame,text = "Gender", bg = "#B6B6B4", fg = "black", font = ("times new roman", 15, 'bold'))
        lbl_gender.grid(row = 4, column = 0, pady = 10, padx= 20, sticky = "w")

        combo_gender = ttk.Combobox(Manage_Frame,  textvariable= self.gender_var, font = ("times new roman", 13, 'bold'), state = "readonly")
        combo_gender['values'] = ("Male", "Female","Other")
        combo_gender.grid(row = 4, column = 1, pady = 10, padx= 20, sticky = "w")

        # Contact
        lbl_contact = Label(Manage_Frame,text = "Contact", bg = "#B6B6B4", fg = "black", font = ("times new roman", 15, 'bold'))
        lbl_contact.grid(row = 5, column = 0, pady = 10, padx= 20, sticky = "w")

        txt_contact = Entry(Manage_Frame, textvariable= self.contact_var, font = ("times new roman", 15, 'bold'), bd = 5, relief = GROOVE )
        txt_contact.grid(row = 5, column =1, pady = 10, padx= 20, sticky = "w")

        # Date of Birth 
        lbl_dob = Label(Manage_Frame,text = "D.O.B", bg = "#B6B6B4", fg = "black", font = ("times new roman", 15, 'bold'))
        lbl_dob.grid(row = 6, column = 0, pady = 10, padx= 20, sticky = "w")

        txt_dob = Entry(Manage_Frame, textvariable= self.dob_var, font = ("times new roman", 15, 'bold'), bd = 5, relief = GROOVE )
        txt_dob.grid(row = 6, column =1, pady = 10, padx= 20, sticky = "w")

        # Address
        lbl_address = Label(Manage_Frame,text = "Address", bg = "#B6B6B4", fg = "black", font = ("times new roman", 15, 'bold'))
        lbl_address.grid(row = 7, column = 0, pady = 10, padx= 20, sticky = "w")

        self.txt_address = Text(Manage_Frame,width = 19, height = 3, font = ("",15))
        self.txt_address.grid(row = 7, column =1, pady = 10, padx= 20, sticky = "w")


        # =============== Button Frame ===================
        Btn_Frame = Frame(Manage_Frame, bd = 4, relief = RIDGE, bg = "#B6B6B4")
        Btn_Frame.place(x = 10, y =530, width = 450, )

        Addbtn = Button(Btn_Frame, command=self.add_student, text="Add",width=10, bg="#033E3E",fg="white",cursor="hand2",font=("",10,'bold')).grid(row=0, column=0,padx=10,pady=10)
        Updatebtn = Button(Btn_Frame, command=self.update_data, text="Update",width=10,  bg="#033E3E",fg="white",cursor="hand2",font=("",10,'bold')).grid(row=0, column=1,padx=10,pady=10)
        Deletebtn = Button(Btn_Frame, command=self.delete_data, text="Delete",width=10,  bg="#033E3E",fg="white",cursor="hand2",font=("",10,'bold')).grid(row=0, column=2,padx=10,pady=10)
        Clearbtn = Button(Btn_Frame, command=self.clear, text="Clear",width=10,  bg="#033E3E",fg="white",cursor="hand2",font=("",10,'bold')).grid(row=0, column=3,padx=10,pady=10)

        # =============== Detail Frame ===================
        Detail_Frame = Frame(self.root, bd = 4, relief = RIDGE, bg = "#B6B6B4")
        Detail_Frame.place(x = 520, y = 100, width = 820, height = 600)

        lbl_search = Label(Detail_Frame,text = "Search", bg = "#B6B6B4", fg = "black", font = ("times new roman", 20, 'bold'))
        lbl_search.grid(row = 0, column = 0, pady = 10, padx= 20, sticky = "w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable= self.search_by, width  = 10,  font = ("times new roman", 13, 'bold'), state = "readonly")
        combo_search['values'] = ("Roll_No", "Name","Contact")
        combo_search.grid(row = 0, column = 1, pady = 10, padx= 20, sticky = "w")

        txt_search = Entry(Detail_Frame,textvariable=self.search_txt, width = 20, font = ("times new roman", 10, 'bold'), bd = 5, relief = GROOVE )
        txt_search.grid(row = 0, column = 2, pady = 10, padx= 20, sticky = "w")

        searchbtn = Button(Detail_Frame, command=self.search_data, text="Search",width=10,  bg="#033E3E",fg="white",cursor="hand2",font=("",10,'bold')).grid(row=0, column=3,padx=10,pady=10)
        showvalbtn = Button(Detail_Frame, command=self.fetch_data, text="ShowAll",width=10,  bg="#033E3E",fg="white",cursor="hand2",font=("",10,'bold')).grid(row=0, column=4,padx=10,pady=10)

         # =============== Table Frame ===================

        Tabel_Frame = Frame(Detail_Frame, bd = 4, relief = RIDGE, bg = "#B6B6B4")
        Tabel_Frame.place(x = 10, y = 70, width = 770, height = 500)

        scroll_x = Scrollbar(Tabel_Frame, orient=HORIZONTAL)
        scroll_y= Scrollbar(Tabel_Frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Tabel_Frame, columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll",text="Roll No.")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("address",text="Address")

        self.Student_table['show'] = 'headings' # if we not add this it show extra space 

        self.Student_table.column("roll",width=50)
        self.Student_table.column("name",width=80)
        self.Student_table.column("email",width=130)
        self.Student_table.column("gender",width=80)
        self.Student_table.column("contact",width=80)
        self.Student_table.column("dob",width=80)
        self.Student_table.column("address",width=160)

        self.Student_table.pack(fill=BOTH,expand=1) 

        # bind dat to show inform when button is realised
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        # to show data when the program is executed 
        self.fetch_data()
    
    def add_student(self):
        if(self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.name_var.get()=="" or self.email_var.get() ==""
         or self.gender_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="" ):
            messagebox.showerror("Error","All feild are required! ")
        # elif(self.Roll_No_var.get()== "neme=%s"):
        #     messagebox.showerror("Error","The rollno is already exits ")
        else:   
            con=pymysql.connect(host="localhost", user="root", password="", database="sms") # database connection
            cur = con.cursor() # to exicute query
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                                self.name_var.get(),
                                                                                self.email_var.get(),
                                                                                self.gender_var.get(),
                                                                                self.contact_var.get(),
                                                                                self.dob_var.get(),
                                                                                self.txt_address.get('1.0',END)
                                                                                ))                   
            con.commit()       
            self.fetch_data()
            self.clear()                                               
            con.close()

            messagebox.showinfo("Message","Record has been inserted.")
        # To fetch data from database 
    def fetch_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="sms") # database connection
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,value = row)
            con.commit()
        con.close()
    
    # Clear Form data 
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)

    #  to fetch data in form section for edit
    def get_cursor(self, eve):
        cursor_row = self.Student_table.focus()
        content = self.Student_table.item(cursor_row)
        row = content['values']

        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END, row[6])

    # Update data 
    def update_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="sms") 
        cur = con.cursor() # to exicute query
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(self.name_var.get(),
                                                                                                                self.email_var.get(),
                                                                                                                self.gender_var.get(),
                                                                                                                self.contact_var.get(),
                                                                                                                self.dob_var.get(),
                                                                                                                self.txt_address.get('1.0',END),
                                                                                                                self.Roll_No_var.get()
                                                                                                                ))   
        messagebox.showinfo("Message"," Record updated successfully!")                                                                                                        
        con.commit()      
        self.fetch_data()
        self.clear()
        con.close()

    # Delete data 
    def delete_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="sms") # database connection
        cur = con.cursor()
        cur.execute("delete from students where roll_no = %s", self.Roll_No_var.get())

        messagebox.showinfo("Message"," Record deleted successfully!")

        con.commit()      
        con.close()
        self.fetch_data()
        self.clear()       

 # Searcch data 
    def search_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="sms") # database connection
        cur = con.cursor()
        cur.execute("select * from students where "+ str(self.search_by.get())+" Like '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,value = row)
            con.commit()
        con.close()


root = Tk()
ob = Student(root)
root.mainloop()