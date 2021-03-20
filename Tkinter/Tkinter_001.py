from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import psycopg2

class Login:
    def __init__(self,master):
        self.master=master
        self.master.title("Login System")
        self.master.geometry("1199x600+100+50")
        self.master.resizable(False,False)
        #Background Image
        self.bg=ImageTk.PhotoImage(file="images/ap4.jpg")
        self.bg_image=Label(self.master,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #Statusbar

        #Create Database or connect to one
        try:
            conn=psycopg2.connect(
                host='89.252.184.80',
                user='postgres',
                password='41011@bohE',
                database='deneme1'
            )
            curs=conn.cursor()
            messagebox.showinfo("Bilgi","Database bağlantısı başarılı",parent=self.master)
        except Exception as Hata:
            messagebox.showerror("Hata","Veritabanı bağlantı hatası : "+str(Hata))
        #Login Frame
        Frame_login=Frame(self.master,bg='lightblue',bd=1)
        Frame_login.place(x=730,y=330,height=230,width=400)

        title=Label(Frame_login,text="Kullanıcı Girişi",font=("Arial",15,'bold'),bg="lightblue",fg='#d77337')
        title.place(x=120,y=10)
        lbl_user=Label(Frame_login,text="Kullanıcı Adı",font=("Goudy old style",15),bg="lightblue")
        lbl_user.place(x=50,y=45)
        self.txt_user=Entry(Frame_login,font=("Goudy old style",15),width=30)
        self.txt_user.place(x=50,y=75)
        lbl_pass = Label(Frame_login, text="Parola", font=("Goudy old style", 15),bg="lightblue")
        lbl_pass.place(x=50, y=105)
        self.txt_pass = Entry(Frame_login, font=("Goudy old style", 15),width=30)
        self.txt_pass.place(x=50, y=135)

        btn_Forget=Button(Frame_login,command=self._forgetPass,cursor="hand2",text="Şifre Unuttun ?",bg="lightblue",fg='#d77337',font=("Arial",11),height=1,width=10,bd=0).place(x=50,y=165)
        btn_Login = Button(self.master,command=self._login,cursor="hand2", text="Login", bg="#d77337", fg='lightblue', font=("Arial", 15)).place(x=850,y=535,width=180,height=40)

    def _login(self):
        if self.txt_pass.get() =="" or self.txt_user.get()=="":
            messagebox.showerror("Hata","Tüm alanların girilmesi zorunludur",parent=self.master)
        elif self.txt_pass.get() !="123" or self.txt_user.get()!="nkuzu":
            messagebox.showerror("Hata","Geçersiz kullanıcı adı / parola",parent=self.master)
        else:
            messagebox.showinfo("Bilgi",f"Hoşgeldin {self.txt_user.get()}",parent=self.master)
            self.mainPage=Toplevel()
            self.mainPage.title(f"Gemont A.Ş. | {self.txt_user.get()}")
            self.mainPage.geometry("1200x750")
            self.mainPage.resizable(False,False)
            status = Label(self.mainPage, text="Kullanıcı : "+str(self.txt_user.get())).place(x=1000,y=730)

    def _forgetPass(self):
        forget_pass=Toplevel()
        forget_pass.title("Şifremi Unuttum")
        forget_pass.geometry("700x400")
        lbl_title=Label(forget_pass,text="Şifremi Hatırlatma").pack()
        lbl_user=Label(forget_pass,text="Kullanıcı Adı : ",font=("Arial",13)).place(x=15,y=15)


master=Tk()
obj=Login(master)
master.mainloop()