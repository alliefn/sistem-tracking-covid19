import tkinter as tk
from style import *
import tkinter.messagebox as mb
import re

# Mengecek suatu email valid atau tidak
def emailvalid(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if re.search(regex,email):
        return True
    else:
        return False

# Mengecek suatu phone number valid atau tidak,
# phone number harus berasal dari negara +62
def phonevalid(phonenumber):
    regex = '(?:\+62)?0?8\d{2}(\d{8})'
    if re.search(regex, phonenumber):
        return True
    else:
        return False

# Utilitas untuk pindah halaman ke login
def open_login(window):
    window.destroy()
    login()

class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background = BG_COLOR)
        # BAGIAN TERATAS: LOGIN PAGE
        # login page frame
        self.frm_loginpg = tk.Frame(self, width = 560, height = 25, relief = tk.GROOVE, borderwidth=1)
        self.frm_loginpg.place(x=0, y=0, height = 25, width = 560)
        self.frm_loginpg.configure(background=BG_COLOR)

        # Label login page
        self.lbl_loginpg = tk.Label(master=self.frm_loginpg, text="Login Page", bg=BG_COLOR)
        self.lbl_loginpg.place(x=0,y=0)

        # Logout button
        # Button keluar dari aplikasi
        self.btn_exit = tk.Button(master=self.frm_loginpg, text="Exit", cursor="hand2", highlightthickness = 0, bd = 0, command = lambda window = self.master : exit(window)) # command: fungsi keluar
        self.btn_exit.configure(font=SMALL_FONT)
        self.btn_exit.pack(side=tk.RIGHT, padx=5)
        self.btn_exit.configure(background=BG_COLOR)
        
        # Sign up button
        # Button sign up
        self.btn_signup = tk.Button(master=self.frm_loginpg, text="Sign up", cursor="hand2", highlightthickness = 0, bd = 0, command = lambda: controller.show_frame("SignUp")) # command: fungsi ke signup
        self.btn_signup.configure(font=SMALL_FONT)
        self.btn_signup.pack(side=tk.RIGHT, padx=5)
        self.btn_signup.configure(background=BG_COLOR)

        # NAMA APLIKASI DI BAGIAN PALING KIRI
        # Nameframe
        self.frm_name = tk.Frame(self, width = 280, height = 280, relief = tk.GROOVE, borderwidth = 1)
        self.frm_name.place(x=0, y=25, height = 280, width=280)
        self.frm_name.configure(background=BG_COLOR)

        # Name label
        self.lbl_name = tk.Label(master=self.frm_name, text = "Coronavirus\nTracking\nSystem", bg=BG_COLOR)
        self.lbl_name.pack(expand=True)

        # FORM SIGNIN DI TENGAH
        # Signin frame
        self.frm_signin = tk.Frame(self, width = 280, height = 280, relief = tk.GROOVE, borderwidth = 1)
        self.frm_signin.place(x=280,y=25,height = 280,width=280)
        self.frm_signin.configure(background=BG_COLOR)

        # Login label
        self.lbl_login = tk.Label(master=self.frm_signin, text="Login", bg=BG_COLOR)
        self.lbl_login.pack(side=tk.TOP)

        # Username label
        self.lbl_uname = tk.Label(master=self.frm_signin, text="Username:", bg=BG_COLOR)
        self.lbl_uname.place(x=70,y=90)

        # Username form
        self.ent_uname = tk.Entry(master=self.frm_signin, width = 20)
        self.ent_uname.place(x=70,y=110)
        self.ent_uname.insert(0,"Username")

        # Password label
        self.lbl_password = tk.Label(master=self.frm_signin, text="Password:", bg=BG_COLOR)
        self.lbl_password.place(x=70,y=130)

        # Password form
        self.ent_password = tk.Entry(master=self.frm_signin, width = 20, show="*")
        self.ent_password.place(x=70,y=150)
        self.ent_password.insert(0,"Password")

        # Submit button
        self.btn_submit = tk.Button(master=self.frm_signin, text="Sign in", cursor="hand2", command = self.signin)
        self.btn_submit.place(x=105,y=175)

    def signin(self, *args):
        uname = self.ent_uname.get()
        passw = self.ent_password.get()
        sql = "SELECT username, password, role FROM User WHERE username = '" + uname + "' and " + "password = '" + passw + "'"
        self.controller.mycursor.execute(sql)
        hasil = self.controller.mycursor.fetchall()

        # Cek ada hasil atau nggak
        if (len(hasil) == 0):
            mb.showerror("Error","Username atau password Anda salah")
        else:
            i = 0
            for line in hasil:
                for ch in line:
                    if (ch != '(' and ch != "'"):
                        ch = ch # Ubah ch ke ch yang udah di"perbaiki"
                    i += 1
                    if (i == 3):
                        status_pengguna = ch
            ucapan = "Selamat datang, " + str(uname) + "!"
            mb.showinfo("Informasi",ucapan)
            self.controller.username = str(uname)
            self.controller.role = str(status_pengguna)
            self.controller.loggedIn = True

            if (self.controller.role == "admin"):
                self.controller.show_frame("AdminHome")
            else:
                self.controller.show_frame("MenuSuhu")

class SignUp(tk.Frame):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background = BG_COLOR)
        # BAGIAN TERATAS: Sign up PAGE
        # login page frame
        self.frm_loginpg = tk.Frame(master=self, width = 560, height = 25, relief = tk.GROOVE, borderwidth=1)
        self.frm_loginpg.place(x=0, y=0, height = 25, width = 560)
        self.frm_loginpg.configure(background=BG_COLOR)

        # Label login page
        self.lbl_loginpg = tk.Label(master=self.frm_loginpg, text="Login Page - Sign Up", bg=BG_COLOR)
        self.lbl_loginpg.place(x=0,y=0)

        # Logout button
        # Button input data Covid-19
        self.btn_exit = tk.Button(master=self.frm_loginpg, text="Exit", cursor="hand2", highlightthickness = 0, bd = 0, command = lambda window = self.master : exit(window)) # command: fungsi keluar
        self.btn_exit.configure(font=SMALL_FONT, padx=5)
        self.btn_exit.configure(background=BG_COLOR)
        self.btn_exit.pack(side=tk.RIGHT)

        # Logout button
        # Button input data Covid-19
        self.btn_signup = tk.Button(master=self.frm_loginpg, text="Sign in", cursor="hand2", highlightthickness = 0, bd = 0, command=lambda: controller.show_frame("Login")) # command: fungsi ke laman sign in
        self.btn_signup.configure(font=SMALL_FONT, padx=5)
        self.btn_signup.configure(background=BG_COLOR)
        self.btn_signup.pack(side=tk.RIGHT)

        # FORM SIGNUP DI BAGIAN PALING KANAN
        # Signup frame
        self.frm_signup = tk.Frame(master=self, width = 560, height = 280, relief = tk.GROOVE, borderwidth = 1)
        self.frm_signup.place(x=0,y=25,height = 280,width=560)
        self.frm_signup.configure(background=BG_COLOR)

        # Register label
        self.lbl_register = tk.Label(master=self.frm_signup, text="Daftar Anggota Baru", bg=BG_COLOR)
        self.lbl_register.pack()

        # Username label
        self.lbl_unamenew = tk.Label(master=self.frm_signup, text="Username:", bg=BG_COLOR)
        self.lbl_unamenew.place(x=220,y=30)

        # Username form
        self.ent_unamenew = tk.Entry(master=self.frm_signup, width = 20)
        self.ent_unamenew.place(x=220,y=50)
        self.ent_unamenew.insert(0,"Username")

        # Name label
        self.lbl_name = tk.Label(master=self.frm_signup, text="Name:", bg=BG_COLOR)
        self.lbl_name.place(x=220,y=70)

        # Name form
        self.ent_name = tk.Entry(master=self.frm_signup, width = 20)
        self.ent_name.place(x=220,y=90)
        self.ent_name.insert(0,"Your Name")

        # Email label
        self.lbl_email = tk.Label(master=self.frm_signup, text="Email:", bg=BG_COLOR)
        self.lbl_email.place(x=220,y=110)

        # Email form
        self.ent_email = tk.Entry(master=self.frm_signup, width = 20)
        self.ent_email.place(x=220,y=130)
        self.ent_email.insert(0,"Your Email")

        # Password label
        self.lbl_passwordnew = tk.Label(master=self.frm_signup, text="Password:", bg=BG_COLOR)
        self.lbl_passwordnew.place(x=220,y=150)

        # Password form
        self.ent_passwordnew = tk.Entry(master=self.frm_signup, width = 20, show = "*")
        self.ent_passwordnew.place(x=220,y=170)
        self.ent_passwordnew.insert(0,"Password")

        # Phone number label
        self.lbl_phone = tk.Label(master=self.frm_signup, text="Nomor telepon:", bg=BG_COLOR)
        self.lbl_phone.place(x=220,y=190)

        # Phone number form
        self.ent_phone = tk.Entry(master=self.frm_signup, width = 20)
        self.ent_phone.place(x=220,y=210)
        self.ent_phone.insert(0,"080000000000")

        # Submit button
        self.btn_submit = tk.Button(master=self.frm_signup, cursor="hand2", text="Sign up", command = lambda : self.signup())
        self.btn_submit.place(x=250,y=235)

    def signup(self, *args):
        uname = self.ent_unamenew.get()
        name = self.ent_name.get()
        passw = self.ent_passwordnew.get()
        surel = self.ent_email.get()
        noTel = self.ent_phone.get()
        sql = "SELECT username FROM User WHERE username = '" + uname + "'"
        self.controller.mycursor.execute(sql)
        hasil = self.controller.mycursor.fetchall()

        if (len(hasil) > 0 or not emailvalid(surel) or not phonevalid(noTel)):
            if (len(hasil) > 0):
                mb.showerror("Error","Username sudah digunakan!")
            elif (not (emailvalid(surel))):
                mb.showerror("Error","Email tidak valid")
            elif (not (phonevalid(noTel))):
                mb.showerror("Error","Nomor telepon tidak valid")
        else:
            self.controller.mycursor.execute("INSERT INTO User VALUES (%s, %s, %s, %s, %s, %s)", (uname, name, passw, surel, noTel, "pengguna"))
            self.controller.dB.commit()
            ucapan = "Selamat datang, " + str(uname) + "!"
            mb.showinfo("Informasi",ucapan)
            self.controller.show_frame("MenuSuhu")
            #ag.menuSuhu(uname, mycursor, dB, 4)
            # menuSuhu(uname) datangnya dari Tami