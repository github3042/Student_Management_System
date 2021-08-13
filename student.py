from tkinter import *      # provide  GUI interface 
from tkinter import ttk  # provide compo box
# from tkinter.font import BOLDfont
class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management") 
        self.root.geometry("1120x700+0+0")

        #  To create a label 
        title = Label(self.root,text="Student Management",bd = 10, relief = GROOVE,
        font = ("times new roman",40, 'bold'),bg = "grey", fg = "black")
        title.pack(side=TOP, fill= X)

        # =============== Manage Frame ===================
        Manage_Frame = Frame(self.root, bd = 4, relief = RIDGE, bg = "crimson")
        Manage_Frame.place(x = 20, y = 100, width = 470, height = 600)

        m_title = Label(Manage_Frame,text = "Manage Student", bg = "crimson", fg = "white", font = ("times new roman", 30, 'bold'))
        m_title.grid(row = 0, columnspan=2, pady= 20)

        # Rollno
        lbl_roll = Label(Manage_Frame,text = "Roll No.", bg = "crimson", fg = "white", font = ("times new roman", 15, 'bold'))
        lbl_roll.grid(row = 1, column = 0, pady = 10, padx= 20, sticky = "w")

        txt_roll = Entry(Manage_Frame, font = ("times new roman", 15, 'bold'), bd = 5, relief = GROOVE )
        txt_roll.grid(row = 1, column =1, pady = 10, padx= 20, sticky = "w")

        # Name
        lbl_name = Label(Manage_Frame,text = "Name", bg = "crimson", fg = "white", font = ("times new roman", 15, 'bold'))
        lbl_name.grid(row = 2, column =0, pady = 10, padx= 20, sticky = "w")

        txt_name = Entry(Manage_Frame, font = ("times new roman", 15, 'bold'), bd = 5, relief = GROOVE )
        txt_name.grid(row = 2, column =1, pady = 10, padx= 20, sticky = "w")

        # Email
        lbl_email = Label(Manage_Frame,text = "Email", bg = "crimson", fg = "white", font = ("times new roman", 15, 'bold'))
        lbl_email.grid(row = 3, column = 0, pady = 10, padx= 20, sticky = "w")

        txt_email = Entry(Manage_Frame, font = ("times new roman", 15, 'bold'), bd = 5, relief = GROOVE )
        txt_email.grid(row = 3, column =1, pady = 10, padx= 20, sticky = "w")

        # Gender
        lbl_gender = Label(Manage_Frame,text = "Gender", bg = "crimson", fg = "white", font = ("times new roman", 15, 'bold'))
        lbl_gender.grid(row = 4, column = 0, pady = 10, padx= 20, sticky = "w")

        combo_gender = ttk.Combobox(Manage_Frame, font = ("times new roman", 13, 'bold'), state = "readonly")
        combo_gender['values'] = ("Male", "Female","Other")
        combo_gender.grid(row = 4, column = 1, pady = 10, padx= 20, sticky = "w")

        # Contact
        lbl_contact = Label(Manage_Frame,text = "Contact", bg = "crimson", fg = "white", font = ("times new roman", 15, 'bold'))
        lbl_contact.grid(row = 5, column = 0, pady = 10, padx= 20, sticky = "w")

        txt_contact = Entry(Manage_Frame, font = ("times new roman", 15, 'bold'), bd = 5, relief = GROOVE )
        txt_contact.grid(row = 5, column =1, pady = 10, padx= 20, sticky = "w")

        # Date of Birth 
        lbl_dob = Label(Manage_Frame,text = "D.O.B", bg = "crimson", fg = "white", font = ("times new roman", 15, 'bold'))
        lbl_dob.grid(row = 6, column = 0, pady = 10, padx= 20, sticky = "w")

        txt_dob = Entry(Manage_Frame, font = ("times new roman", 15, 'bold'), bd = 5, relief = GROOVE )
        txt_dob.grid(row = 6, column =1, pady = 10, padx= 20, sticky = "w")

        # Address
        lbl_address = Label(Manage_Frame,text = "Address", bg = "crimson", fg = "white", font = ("times new roman", 15, 'bold'))
        lbl_address.grid(row = 7, column = 0, pady = 10, padx= 20, sticky = "w")

        txt_address = Text(Manage_Frame,width = 19, height = 3, font = ("",15))
        txt_address.grid(row = 7, column =1, pady = 10, padx= 20, sticky = "w")


        # =============== Button Frame ===================
        Btn_Frame = Frame(Manage_Frame, bd = 4, relief = RIDGE, bg = "crimson")
        Btn_Frame.place(x = 10, y =530, width = 450, )

        Addbtn = Button(Btn_Frame, text="Add",width=10, bg="grey",fg="white",font=("",10,'bold')).grid(row=0, column=0,padx=10,pady=10)
        Updatebtn = Button(Btn_Frame, text="Update",width=10,  bg="grey",fg="white",font=("",10,'bold')).grid(row=0, column=1,padx=10,pady=10)
        Deletebtn = Button(Btn_Frame, text="Delete",width=10,  bg="grey",fg="white",font=("",10,'bold')).grid(row=0, column=2,padx=10,pady=10)
        Clearbtn = Button(Btn_Frame, text="Clear",width=10,  bg="grey",fg="white",font=("",10,'bold')).grid(row=0, column=3,padx=10,pady=10)

        # =============== Detail Frame ===================
        Detail_Frame = Frame(self.root, bd = 4, relief = RIDGE, bg = "crimson")
        Detail_Frame.place(x = 520, y = 100, width = 820, height = 600)

        lbl_seaarch = Label(Detail_Frame,text = "Search", bg = "crimson", fg = "white", font = ("times new roman", 20, 'bold'))
        lbl_seaarch.grid(row = 0, column = 0, pady = 10, padx= 20, sticky = "w")

        combo_search = ttk.Combobox(Detail_Frame, width  = 10,  font = ("times new roman", 13, 'bold'), state = "readonly")
        combo_search['values'] = ("RollNo", "Name","Contact")
        combo_search.grid(row = 0, column = 1, pady = 10, padx= 20, sticky = "w")

        txt_search = Entry(Detail_Frame, width = 20, font = ("times new roman", 10, 'bold'), bd = 5, relief = GROOVE )
        txt_search.grid(row = 0, column = 2, pady = 10, padx= 20, sticky = "w")

        searchbtn = Button(Detail_Frame, text="Search",width=10,  bg="grey",fg="white",font=("",10,'bold')).grid(row=0, column=3,padx=10,pady=10)
        showvalbtn = Button(Detail_Frame, text="ShowAll",width=10,  bg="grey",fg="white",font=("",10,'bold')).grid(row=0, column=4,padx=10,pady=10)

         # =============== Table Frame ===================

        Tabel_Frame = Frame(Detail_Frame, bd = 4, relief = RIDGE, bg = "crimson")
        Tabel_Frame.place(x = 10, y = 70, width = 770, height = 500)

        scroll_x = Scrollbar(Tabel_Frame, orient=HORIZONTAL)
        scroll_y= Scrollbar(Tabel_Frame, orient=VERTICAL)

        Student_table = ttk.Treeview(Tabel_Frame, columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)

        Student_table.heading("roll",text="Roll No.")
        Student_table.heading("name",text="Name")
        Student_table.heading("email",text="Email")
        Student_table.heading("gender",text="Gender")
        Student_table.heading("contact",text="Contact")
        Student_table.heading("dob",text="D.O.B")
        Student_table.heading("address",text="Address")

        Student_table['show'] = 'headings' # if we not add this it show extra space 

        Student_table.column("roll",width=50)
        Student_table.column("name",width=130)
        Student_table.column("email",width=100)
        Student_table.column("gender",width=100)
        Student_table.column("contact",width=100)
        Student_table.column("dob",width=100)
        Student_table.column("address",width=160)

        Student_table.pack(fill=BOTH,expand=1)  


root = Tk()
ob = Student(root)
root.mainloop()