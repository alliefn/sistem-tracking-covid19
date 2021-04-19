import pytest
import mysql.connector
import tkinter as tk
from tkinter import messagebox as mb
import re
import autentikasi_login_gui as ag

# Mengecek suatu email valid atau tidak
def check_mail(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    return re.search(regex, email)

# Mengecek suatu phone number valid atau tidak,
# phone number harus berasal dari negara +62
def check_phone(phonenumber):
    regex = '(?:\+62)?0?8\d{2}(\d{8})'
    return re.search(regex, phonenumber)

# menuAdmin, muncul setelah login sukses
def menuAdmin(username):

    # PERSIAPAN WINDOW
    window = tk.Tk()
    window.title("Sistem Tracking Corona")
    window.geometry("560x220")
    window.configure(bg="#c8eed9")

    # BAGIAN TERATAS: Admin - Pilihan Menu
    # Frame admin page frame
    frm_mainpg = tk.Frame(master=window, width = 560, height = 25, relief = tk.GROOVE, borderwidth=1)
    frm_mainpg.place(x=0, y=0, height = 25, width = 560)
    frm_mainpg.configure(background='#c8eed9')

    # Label admin page
    lbl_mainpg = tk.Label(master=frm_mainpg, text="Admin - Pilihan Menu", bg='#c8eed9')
    lbl_mainpg.place(x=0,y=0)

    # BAGIAN BAWAH: MENU
    # Frame menu
    frm_menu = tk.Frame(master=window, width = 560, height = 195, relief = tk.GROOVE, borderwidth=1)
    frm_menu.place(x=0,y=25, height = 195, width = 560)
    frm_menu.configure(background='#c8eed9')

    # Label pilihan
    lbl_pil = tk.Label(master=frm_menu, text="Pilihan Menu Admin", bg='#c8eed9')
    lbl_pil.configure(font=("Calibri", 20))
    lbl_pil.pack(side=tk.TOP)

    # Button input data Covid-19
    btn_inputcovid = tk.Button(master=frm_menu, text="Input data Covid-19") # command: fungsi ke modul input data Covid
    btn_inputcovid.configure(font=("Calibri", 10))
    btn_inputcovid.pack(pady=10)

    # Button input data RS
    btn_inputrs = tk.Button(master=frm_menu, text="Input data Rumah Sakit") # command: fungsi ke modul input data RS
    btn_inputrs.configure(font=("Calibri", 10))
    btn_inputrs.pack(pady=10)

    # Button verifikasi pesanan pengguna
    btn_verify = tk.Button(master=frm_menu, text="Verifikasi pesanan pengguna") # command: fungsi ke modul verifikasi
    btn_verify.configure(font=("Calibri", 10))
    btn_verify.pack(pady=10)

    window.mainloop()

def login():
        
    # Persiapan database
    dB = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="trackingCovid"
            )
    mycursor = dB.cursor()

    # Persiapan window
    window = tk.Tk()
    window.geometry("840x305")
    window.title("Sistem Tracking Corona")
    window.configure(background='#c8eed9')

    # BAGIAN TERATAS: LOGIN PAGE
    # login page frame
    frm_loginpg = tk.Frame(master=window, width = 840, height = 25, relief = tk.GROOVE, borderwidth=1)
    frm_loginpg.place(x=0, y=0, height = 25, width = 840)
    frm_loginpg.configure(background='#c8eed9')

    # Label login page
    lbl_loginpg = tk.Label(master=frm_loginpg, text="Login Page", bg='#c8eed9')
    lbl_loginpg.place(x=0,y=0)

    # NAMA APLIKASI DI BAGIAN PALING KIRI
    # Nameframe
    frm_name = tk.Frame(master=window, width = 280, height = 280, relief = tk.GROOVE, borderwidth = 1)
    frm_name.place(x=0, y=25, height = 280, width=280)
    frm_name.configure(background='#c8eed9')

    # Name label
    lbl_name = tk.Label(master=frm_name, text = "Coronavirus\nTracking\nSystem", bg='#c8eed9')
    lbl_name.pack(expand=True)

    # FORM SIGNIN DI TENGAH
    # Signin frame
    frm_signin = tk.Frame(master=window, width = 280, height = 280, relief = tk.GROOVE, borderwidth = 1)
    frm_signin.place(x=280,y=25,height = 280,width=280)
    frm_signin.configure(background='#c8eed9')

    # Login label
    lbl_login = tk.Label(master=frm_signin, text="Login", bg='#c8eed9')
    lbl_login.pack(side=tk.TOP)

    # Username label
    lbl_uname = tk.Label(master=frm_signin, text="Username:", bg='#c8eed9')
    lbl_uname.place(x=70,y=90)

    # Username form
    ent_uname = tk.Entry(master=frm_signin, width = 20)
    ent_uname.place(x=70,y=110)
    ent_uname.insert(0,"Username")

    # Password label
    lbl_password = tk.Label(master=frm_signin, text="Password:", bg='#c8eed9')
    lbl_password.place(x=70,y=130)

    # Password form
    ent_password = tk.Entry(master=frm_signin, width = 20, show="*")
    ent_password.place(x=70,y=150)
    ent_password.insert(0,"Password")

    def signin(dB):
        uname = ent_uname.get()
        passw = ent_password.get()
        sql = "SELECT username, password, role FROM User WHERE username = '" + uname + "' and " + "password = '" + passw + "'"
        mycursor.execute(sql)
        hasil = mycursor.fetchall()

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
            mb.showinfo("Informasi","Selamat datang!")
            login = True
            uname = str(uname)
            status_pengguna = str(status_pengguna)
            window.destroy()
            if (status_pengguna == "admin"):
                menuAdmin(uname)
            else:
                ag.menuSuhu(uname, mycursor, dB, 4)
                # menuSuhu(uname) datangnya dari Tami

    # Submit button
    btn_submit = tk.Button(master=frm_signin, text="Sign in", command = lambda mydB = dB : signin(mydB))
    btn_submit.place(x=105,y=175)

    # FORM SIGNUP DI BAGIAN PALING KANAN
    # Signup frame
    frm_signup = tk.Frame(master=window, width = 280, height = 280, relief = tk.GROOVE, borderwidth = 1)
    frm_signup.place(x=560,y=25,height = 280,width=280)
    frm_signup.configure(background='#c8eed9')

    # Register label
    lbl_register = tk.Label(master=frm_signup, text="Daftar Anggota Baru", bg='#c8eed9')
    lbl_register.pack()

    # Username label
    lbl_unamenew = tk.Label(master=frm_signup, text="Username:", bg='#c8eed9')
    lbl_unamenew.place(x=70,y=30)

    # Username form
    ent_unamenew = tk.Entry(master=frm_signup, width = 20)
    ent_unamenew.place(x=70,y=50)
    ent_unamenew.insert(0,"Username")

    # Name label
    lbl_name = tk.Label(master=frm_signup, text="Name:", bg='#c8eed9')
    lbl_name.place(x=70,y=70)

    # Name form
    ent_name = tk.Entry(master=frm_signup, width = 20)
    ent_name.place(x=70,y=90)
    ent_name.insert(0,"Your Name")

    # Email label
    lbl_email = tk.Label(master=frm_signup, text="Email:", bg='#c8eed9')
    lbl_email.place(x=70,y=110)

    # Email form
    ent_email = tk.Entry(master=frm_signup, width = 20)
    ent_email.place(x=70,y=130)
    ent_email.insert(0,"Your Email")

    # Password label
    lbl_passwordnew = tk.Label(master=frm_signup, text="Password:", bg='#c8eed9')
    lbl_passwordnew.place(x=70,y=150)

    # Password form
    ent_passwordnew = tk.Entry(master=frm_signup, width = 20, show = "*")
    ent_passwordnew.place(x=70,y=170)
    ent_passwordnew.insert(0,"Password")

    # Phone number label
    lbl_phone = tk.Label(master=frm_signup, text="Nomor telepon:", bg='#c8eed9')
    lbl_phone.place(x=70,y=190)

    # Phone number form
    ent_phone = tk.Entry(master=frm_signup, width = 20)
    ent_phone.place(x=70,y=210)
    ent_phone.insert(0,"080000000000")

    def signup(dB):
        uname = ent_unamenew.get()
        name = ent_name.get()
        passw = ent_passwordnew.get()
        surel = ent_email.get()
        noTel = ent_phone.get()
        sql = "SELECT username FROM User WHERE username = '" + uname + "'"
        mycursor.execute(sql)
        hasil = mycursor.fetchall()

        if (len(hasil) > 0 or check_mail(surel) or check_phone(noTel)):
            if (len(hasil) > 0):
                mb.showerror("Error","Username sudah digunakan!")
            else:
                if (not (check_mail(surel))):
                    mb.showerror("Error","Email tidak valid")
                elif (not (check_phone(noTel))):
                    mb.showerror("Error","Nomor telepon tidak valid")
        else:
            mycursor.execute("INSERT INTO User VALUES (%s, %s, %s, %s, %s, %s)", (uname, name, passw, surel, noTel, "pengguna"))
            dB.commit()
            mb.showinfo("Informasi","Selamat datang!")
            window.destroy()
            ag.menuSuhu(uname, mycursor, dB, 4)
            # menuSuhu(uname) datangnya dari Tami

    # Submit button
    btn_submit = tk.Button(master=frm_signup, text="Sign up", command = lambda mydB = dB : signup(mydB))
    btn_submit.place(x=105,y=235)

    window.mainloop()

# Keperluan debugging
login()
