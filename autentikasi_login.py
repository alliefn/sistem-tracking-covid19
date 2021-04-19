import mysql.connector
import tkinter as tk

# Jadi fungsi login ini bakal me-set 3 variabel
# Username, login, sama status_pengguna
# Username biar tahu itu siapa yang lagi pake
# status_pengguna dia siapa
# Login buat bisa akses segala fitur (Karena udah login)

def signup(window):

	# Form signup
	frm_form = tk.Frame()
	frm_form.pack()

	# Label & Entry username
	lbl_username = tk.Label(master=frm_form, text="Username")
	lbl_username.grid(row=0, column=0,sticky="e")

	ent_username = tk.Entry(master=frm_form, width=50)
	ent_username.grid(row=0,column=1)

	# Label & Entry password
	lbl_pswd = tk.Label(master=frm_form, text="Password")
	lbl_pswd.grid(row=1, column=0,sticky="e")

	ent_pswd = tk.Entry(master=frm_form, width=50)
	ent_pswd.grid(row=1,column=1)

	# Frame tombol
	frm_buttons = tk.Frame()
	frm_buttons.pack(fill=tk.X, ipadx = 5, ipady=5)

	btn_submit = tk.Button(master=frm_buttons, text="Submit")
	btn_submit.pack(side=tk.RIGHT,padx=10,ipadx=10)

def signin(window):

	# Form signin
	frm_form = tk.Frame()
	frm_form.pack()

	# Label & Entry username
	lbl_username = tk.Label(master=frm_form, text="Username")
	lbl_username.grid(row=0, column=0,sticky="e")

	ent_username = tk.Entry(master=frm_form, width=50)
	ent_username.grid(row=0,column=1)

	# Label & Entry password
	lbl_pswd = tk.Label(master=frm_form, text="Password")
	lbl_pswd.grid(row=1, column=0,sticky="e")

	ent_pswd = tk.Entry(master=frm_form, width=50)
	ent_pswd.grid(row=1,column=1)

	# Frame tombol
	frm_buttons = tk.Frame()
	frm_buttons.pack(fill=tk.X, ipadx = 5, ipady=5)

	btn_submit = tk.Button(master=frm_buttons, text="Submit")
	btn_submit.pack(side=tk.RIGHT,padx=10,ipadx=10)


def login():
    dN = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=""
            )
    mycursor = dN.cursor()

    mycursor.execute("DROP DATABASE IF EXISTS virusTrack")
    mycursor.execute("CREATE DATABASE virusTrack")

    dB = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="virusTrack"
            )

    mycursor = dB.cursor()

    mycursor.execute("CREATE TABLE User (username VARCHAR(255) PRIMARY KEY, nama VARCHAR(255), surel VARCHAR(255), password VARCHAR(20), nomor_telepon VARCHAR(100), role VARCHAR(10))")

    # PROGRAM UTAMA
    pilihan = ""
    login = False
    window = tk.Tk()
    window.title("Sistem Tracking Corona")
    greeting = tk.Label (
    	text = "Selamat datang di aplikasi Sistem Tracking Corona",
    	foreground="white",
    	background="black",
    	width = 49,
    	height = 2
    )
    button1 = tk.Button (
    	text = "Sign in",
    	width = 25,
    	height = 1,
    	bg = "blue",
    	fg = "yellow",
    	command = signin(window)
    )
    button2 = tk.Button (
    	text = "Sign up",
    	width = 25,
    	height = 1,
    	bg = "blue",
    	fg = "yellow",
    	command = signup(window)
    )
    greeting.pack()
    button1.pack()
    button2.pack()
    window.mainloop()
    while (pilihan != "exit" and not login):
        print("Selamat datang di aplikasi Sistem Tracking Corona!\n")
        print("Pilih 1 untuk sign in")
        print("Pilih 2 untuk sign up")
        print("> ",end='')

        pilihan = input()

        if (pilihan == '1'):
            print("\nMasukkan username Anda: ",end='')
            uname = input()
            print("Masukkan password Anda: ",end='')
            passw = input()
            sql = "SELECT username, password, role FROM User WHERE username = '" + uname + "' and " + "password = '" + passw + "'"
            mycursor.execute(sql)
            hasil = mycursor.fetchall()

            # Cek ada hasil atau nggak
            if (len(hasil) == 0):
                print("Tidak ada yang memenuhi\n")
            else:
                i = 0
                for line in hasil:
                    for ch in line:
                        if (ch != '(' and ch != "'"):
                            ch = ch # Ubah ch ke ch yang udah di"perbaiki"
                        i += 1
                        if (i == 3):
                            status_pengguna = ch
                print("Selamat datang,", uname)
               # login = True
        elif (pilihan == '2'):
            print("Masukkan username Anda: ",end='')
            uname = input()
            print("Masukkan nama Anda: ",end='')
            name = input()
            print("Masukkan password Anda: ",end='')
            passw = input()
            print("Masukkan email Anda: ",end='')
            surel = input()
            print("Masukkan nomor telepon Anda: ",end='')
            noTel = input()
            sql = "SELECT username FROM User WHERE username = '" + uname + "'"
            mycursor.execute(sql)
            hasil = mycursor.fetchall()
            if (len(hasil) > 0):
                print("Username sudah digunakan!\n")
            else:
                mycursor.execute("INSERT INTO User VALUES (%s, %s, %s, %s, %s, %s)", (uname, name, passw, surel, noTel, "Pengguna"))
                dB.commit()
                print("Selamat datang,", uname)
                print()
                #login = True
        elif (pilihan == "exit"):
            print("Sampai jumpa ya!")
        else:
            print("Perintah salah!\n")

# Keperluan debugging
login()
