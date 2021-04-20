# GUI Buat Pesanan Khusus Pengguna
from tampilkanDataKamar import *
from konfirmasiPesanan import *
import tkinter as tk
import mysql.connector
import random
import datetime

def getNowDateAsString():
    now = datetime.datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    dateFormat = year + "-" + month + "-" + day
    return dateFormat

def randomIDPesananGenerator(cursor_db):
    randomID = random.randint(700,(10**5)-1)
    # cursor_db.execute("select id_pesanan from pesanan;")
    # checkingResult = cursor_db.fetchall()
    # isDuplikat = False
    # while (not isDuplikat):
    #     for tup in checkingResult:
    #         if (tup == randomID):
    #             isDuplikat = True
    #             break
    #     if (isDuplikat):
    #         randomID = random.randint(700,(10**5)-1)
    #         isDuplikat = False
    return randomID

def getIDRS(cursor_db,namaRS):
    query = "select id_RS from rumahsakit where nama=\'" + namaRS + "\';"
    cursor_db.execute(query)
    result = cursor_db.fetchall()
    return result[0]

def getIDKamar(cursor_db,namaKamar,namaRS):
    idRS = getStringFromResult(getIDRS(cursor_db,namaRS))
    query = "select id_kamar from kamar where nama_kamar=\'" + namaKamar + "\' and id_RS=" + idRS + ";"
    cursor_db.execute(query)
    result = cursor_db.fetchall()
    return result[0]

def buatPesanan():
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dika090301",
    database="trackingCovid"
    )
    cursor_db = db.cursor()
    rs = namaRS.get()
    kamar = namaKamar.get()

    # Siapin value yang mau dimasukin
    IDKamar = getIDKamar(cursor_db,kamar,rs)
    newRandomID = randomIDPesananGenerator(cursor_db)
    nowDate = getNowDateAsString()
    user = "username" + str(newRandomID) # NANTI PAS DIBUAT MAIN PROGRAM, KASIH INI AKSES KE GLOBAL VARIABLE USERNAME BUAT TAU SIAPA YG LOGIN T_T
    
    # Cek apakah terjadi kesamaan id pesanan pada tabel dan yang baru di-generate
    isError = True
    while (isError):
        try:
            insertQuery = ("INSERT INTO pesanan" 
                           "VALUES (%s,%s,%s,%s,%s,%s);")
            val = (newRandomID,getStringFromResult(IDKamar),user,"On Hold",nowDate,"Belum")
            cursor_db.execute(insertQuery,val)
            db.commit()
            isError = False
        except mysql.connector.Error as e:
            newRandomID = randomIDPesananGenerator(cursor_db)
            isError = True
    konfirmasiPesanan(IDKamar)

window = tk.Tk()
window.title("Pesan Kamar Rumah Sakit")
window.geometry("800x800")
window.configure(background='#c8eed9')

title = tk.Label(text="BUAT PESANAN")
title.config(font=("Calibri", 20, 'bold'))
title.config(background='#c8eed9')
title.pack(pady=20)

namaRSLabel = tk.Label(text="Masukkan nama RS\t\t:")
namaRSLabel.config(font=("Calibri", 16, 'bold'))
namaRSLabel.config(background='#c8eed9')
namaRSLabel.place(x=30, y=70)

namaKamarLabel = tk.Label(text="Masukkan nama Kamar\t:")
namaKamarLabel.config(font=("Calibri", 16, 'bold'))
namaKamarLabel.config(background='#c8eed9')
namaKamarLabel.place(x=30, y=120)

namaRS = tk.StringVar()  
namaKamar = tk.StringVar()

namaRSEntry = tk.Entry(textvariable=namaRS, width="30")
namaRSEntry.place(x=320, y=70)
namaKamarEntry = tk.Entry(textvariable=namaKamar, width="30")
namaKamarEntry.place(x=320, y=120)

tampilkanDataKamarButton = tk.Button(window, text="Tampilkan Daftar Kamar", command=tampilkanDataKamar)
tampilkanDataKamarButton.place(x=300, y=180, height=50, width=200)
buatPesananButton = tk.Button(window, text="Pesan", command=buatPesanan)
buatPesananButton.place(x=300, y=240, height=50, width=200)

surpriseLabel = tk.Label(text="Catatan: PERBESAR LAYAR KE KANAN UNTUK MELIHAT JUMLAH KAMAR YANG TERSEDIA SAAT MELIHAT TABEL KAMAR")
surpriseLabel.config(font=("Calibri", 12, 'bold'))
surpriseLabel.config(background='#c8eed9')
surpriseLabel.place(x=30, y=330)

window.mainloop()