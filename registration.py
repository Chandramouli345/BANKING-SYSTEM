from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter.messagebox as msg
import random
import mysql.connector
class Gui:
   def __init__(self,Mainpage):
        self.Mainpage=Mainpage
        self.Mainpage.title("BANK LOGIN")
        self.Mainpage.geometry("1550x800+0+0")
        bg=ImageTk.PhotoImage(file="BGImage.jpg")
        Lbl_bg=Label(Mainpage,image=bg)
        Lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

#===========================================FRAME=====================================================

        frame=Frame(Mainpage,bg="lightblue")
        frame.place(x=510,y=170,width=340,height=450)

#==============================Logo ON FRAME===================================================

        bank=Image.open(r"BANK.jpg")
        bank=bank.resize((100,100),Image.ANTIALIAS)
        photo=ImageTk.PhotoImage(bank)
        b_img=Label(image=photo,bg="lightblue",borderwidth=0)
        b_img.place(x=630,y=190,width=100,height=100)

#===================== username and password ========================

        name=Label(frame,text="Email ID:",font=("times new roman",12,"bold"),fg="red",bg="lightblue")
        name.place(x=10,y=200)
        self.n_l=Entry(frame)
        self.n_l.place(x=100,y=200)

        author=Label(frame,text="Password:",font=("times new roman",12,"bold"),fg="red",bg="lightblue")
        author.place(x=10,y=250)
        self.a_l=Entry(frame)
        self.a_l.place(x=100,y=250)

#================= login Button ==================================================

        l_img=Image.open(r"login-button-png-5.png")
        l_img = l_img.resize((100, 100), Image.ANTIALIAS)
        png = ImageTk.PhotoImage(l_img)
        lognbutn=Button(frame,image=png,command=self.login)
        lognbutn.place(x=120,y=300,width=80,height=35)
#========================== Registration Button ====================================

        regbutn = Button(frame,text="Register Here",font=("times new roman",10,"bold"),borderwidth=0,
                         fg="black",bg="lightblue",command=self.reg)
        regbutn.place(x=5, y=350, width=160)

#================================== forgotpasswrd==========================================

        pwdbutn = Button(frame, text="Forgot Password?", font=("times new roman", 10, "bold"), borderwidth=0,
                         fg="black",bg="lightblue")
        pwdbutn.place(x=10, y=380, width=160)

        Mainpage.mainloop()

#======================= registration page =============================================================================

   def reg(self):
        regpage = Tk()
        regpage.title("Registration page")
        regpage.geometry("400x500")
        regpage.config(bg="lightblue")

        c1=Label(regpage,text="Name")
        c1.place(x=50,y=100)
        self.e_n=Entry(regpage)
        self.e_n.place(x=200,y=100)

        c2 = Label(regpage, text="Mobile number")
        c2.place(x=50, y=200)
        self.e_m = Entry(regpage)
        self.e_m.place(x=200, y=200)

        c3 = Label(regpage, text="Email Id ")
        c3.place(x=50, y=300)
        self.e_g = Entry(regpage)
        self.e_g.place(x=200, y=300)

        c4 = Label(regpage, text="Password")
        c4.place(x=50, y=400)
        self.e_p = Entry(regpage)
        self.e_p.place(x=200, y=400)

        b1=Button(regpage,text="SUBMIT",command=self.validation)
        b1.place(x=200,y=450)

        regpage.mainloop()
#========================== VAlidating Entry fields=========================

   def validation(self):
        if self.e_n.get()=="":
             msg.showerror('Error','Please enter your name',parent=self.Mainpage)
        elif self.e_m.get()=="" or len(self.e_m.get())!=10:
             msg.showerror('Error','Please enter your mobile',parent=self.Mainpage)
        elif self.e_g.get()=="":
             msg.showerror('Error','Please enter your email',parent=self.Mainpage)
        elif self.e_p.get()=="":
             msg.showerror('Error','Please enter your password',parent=self.Mainpage)

#================================ Acoount number generation=========================
        else:
             tk = Tk()
             b2 = Button(tk, text="OK", command=self.connect)
             b2.place(x=10, y=30)
             list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
             self.number = ""
             b1 = Label(tk, text="")
             b1.place(x=10, y=10)
             for i in range(10):
                  self.number = self.number + random.choice(list)
                  b1.config(text=self.number)


#============================= connecting to sql======================================================
   def connect(self):
        mydb=mysql.connector.connect(host="localhost",user="root",port=3306,password="",database="Bank")
        mycursor=mydb.cursor()
        Name=self.e_n.get()
        Mobilenumber=self.e_m.get()
        email=self.e_g.get()
        password=self.e_p.get()
        number=self.number
        mycursor.execute("insert into registration values(%s,%s,%s,%s,%s)",(Name,Mobilenumber,email,password,number))
        mydb.commit()
        msg.showinfo("registration","Registration Successful")

#========================== Login validation==============================

   def login(self):
        if self.n_l.get() == "" or self.a_l.get() == "":
             msg.showerror("Error", "All credentials required", parent=self.Mainpage)
        else:
             try:
                  mydb = mysql.connector.connect(host="localhost", user="root", port=3306, password="",
                                                 database="Bank")
                  mycursor = mydb.cursor()
                  mycursor.execute("select * from registration where email=%s and Password=%s", (self.n_l.get(), self.a_l.get()))
                  row = mycursor.fetchone()
                  if row == None:
                       msg.showerror("Error", "Invalid credentials", parent=self.Mainpage)
                  else:
                       msg.showinfo("success", "Login Successful", parent=self.Mainpage)
             except Exception as es:
                  msg.showerror("Error", f"Error Due to: {str(es)}", parent=self.Mainpage)


if __name__=='__main__':
     Mainpage=Tk()
     s=Gui(Mainpage)
     Mainpage.mainloop()

