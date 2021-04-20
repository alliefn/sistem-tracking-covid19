import tkinter as tk
import mysql.connector
from tkinter import messagebox as mb

def getStringFromResult(result):
    temp = str(result)
    newString = ""
    for i in temp:
        if ((ord(i) >= 48 and ord(i) <= 57) or ord(i) == 46):
            if (ord(i) == 46):
                newString = newString + ','
            else:
                newString = newString + i
    return newString

def getStringFromResultTest(result):
    temp = str(result)
    newString = ""
    for i in temp:
        if ((ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122) or (ord(i) == 32)):
            newString = newString + i
    return newString

def changeToSudah(user):
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dika090301", # placeholder
    database="trackingCovid"
    )
    cursor_db = db.cursor()
    query = "update pesanan set is_confirmed=\'Sudah\' where username=\'" + user + "\';"
    cursor_db.execute(query)
    db.commit()
    mb.showinfo('Berhasil!', 'Konfirmasi pembayaran telah diterima!')

def konfirmasiPesanan(IDKamar):
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dika090301", # placeholder
    database="trackingCovid"
    )
    cursor_db = db.cursor()
    searchQuery = "select harga from kamar where id=" + str(IDKamar) + ";"
    cursor_db.execute(searchQuery)
    result = cursor_db.fetchall()

    window2 = tk.Tk()
    window2.title("Konfirmasi Pesanan")
    window2.geometry("800x800")
    window2.configure(background='#c8eed9')

    berhasilLabel = tk.Label(window2,text="Pesanan Berhasil Dibuat!")
    berhasilLabel.config(font=("Calibri", 16, 'bold'))
    berhasilLabel.config(background='#c8eed9')
    berhasilLabel.place(x=300, y=70)

    transferLabel = tk.Label(window2,text="Silakan lakukan pembayaran melalui transfer bank")
    transferLabel.config(font=("Calibri", 16, 'bold'))
    transferLabel.config(background='#c8eed9')
    transferLabel.place(x=200, y=120)

    bankLabel = tk.Label(window2,text="ABC sebesar")
    bankLabel.config(font=("Calibri", 16, 'bold'))
    bankLabel.config(background='#c8eed9')
    bankLabel.place(x=350, y=140)

    uang = "Rp" + getStringFromResult(result[0])
    jumlahUangLabel = tk.Label(window2,text=uang)
    jumlahUangLabel.config(font=("Calibri", 16, 'bold'))
    jumlahUangLabel.config(background='#c8eed9')
    jumlahUangLabel.place(x=340, y=180)

    konfirmasiLabel = tk.Label(window2,text="Masukkan username Anda dan klik tombol di bawah jika telah melakukan transfer")
    konfirmasiLabel.config(font=("Calibri", 16, 'bold'))
    konfirmasiLabel.config(background='#c8eed9')
    konfirmasiLabel.place(x=100, y=230)

    # user = tk.StringVar()
    # userEntry = tk.Entry(textvariable=user, width="30")
    # userEntry.place(x=260, y=255)
    # userToBeInput = user.get()

    konfirmasiButton = tk.Button(window2, text="Konfirmasi Pesanan", command= lambda: changeToSudah("kimberly")) # TOLONG NANTI ARGUMEN INI DIGANTI SAMA USER YANG LAGI LOGIN YYYYY
    konfirmasiButton.place(x=320, y=290, height=50, width=150)
    window2.mainloop()