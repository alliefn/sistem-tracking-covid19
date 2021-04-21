# GUI Proses Pesanan Khusus Admin
from tampilkanPesanan import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import mysql.connector

def updateQuery(status,ID,db,cursor_db):
    query = "UPDATE pesanan SET status=\'" + status + "\' WHERE id_pesanan=" + str(ID) + ";"
    cursor_db.execute(query)
    db.commit()
    query = "SELECT status FROM pesanan " + "where id_pesanan=" + str(ID) + ";"
    cursor_db.execute(query)
    hasil = cursor_db.fetchone()
    return hasil[0]

def prosesPesanan(idPesanan,statusPesanan):
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", # placeholder
    database="trackingCovid"
    )
    cursor_db = db.cursor()
    # cursor_db.execute("SELECT * FROM pesanan;")
    # result = cursor_db.fetchall()
    # print("No \t ID Pesanan \t\t ID Kamar \t\t Username \t\t Tanggal Pesan \t\t Status")
    # i = 0
    # for tup in result:
    #     i = i + 1
    #     print(i+" \t "+tup[0]+" \t\t "+tup[1]+" \t\t "+tup[2]+" \t\t "+tup[3]+" \t\t "+tup[4])
    # for row in range(i):
    #     for column in range(5):
    #         e = 
    
    # Menerima atau menolak pesanan oleh admin
    ID = idPesanan
    status = statusPesanan

    # Mengurangi jumlah kamar yang tersedia jika pesanan diterima
    if (status == 'Diterima'):
        queryKurangiKamar = "UPDATE kamar SET jumlah=jumlah-1 WHERE id IN (SELECT id_kamar FROM pesanan WHERE id_pesanan=" + str(ID) + ");"
        cursor_db.execute(queryKurangiKamar)
        db.commit()
    # IDPesananPilihan = result[nomorPesanan-1][0]

    dummy = updateQuery(status,ID,db,cursor_db)

    mb.showinfo('Berhasil!', 'Status Pesanan berhasil di-update!')

window = tk.Tk()
window.title("Proses Pesanan")
window.geometry("800x800")
window.configure(background='#c8eed9')

title = tk.Label(text="PROSES PESANAN USER")
title.config(font=("Calibri", 20, 'bold'))
title.config(background='#c8eed9')
title.pack(pady=20)

IDPesananLabel = tk.Label(text="ID Pesanan yang akan diproses\t:")
IDPesananLabel.config(font=("Calibri", 16, 'bold'))
IDPesananLabel.config(background='#c8eed9')
IDPesananLabel.place(x=30, y=70)

statusBaruLabel = tk.Label(text="Status Baru Pesanan\t\t:")
statusBaruLabel.config(font=("Calibri", 16, 'bold'))
statusBaruLabel.config(background='#c8eed9')
statusBaruLabel.place(x=30, y=120)

IDPesanan = tk.StringVar()  
statusBaru = tk.StringVar()

IDPesananEntry = tk.Entry(textvariable=IDPesanan, width="30")
IDPesananEntry.place(x=320, y=70)
statusBaruEntry = ttk.Combobox(window,width=30,textvariable=statusBaru)
statusBaruEntry['values'] = ('On Hold', 'Diterima', 'Ditolak')
statusBaruEntry.place(x=320, y=120)

tampilkanPesananButton = tk.Button(window, text="Tampilkan Pesanan", command=tampilkanPesanan)
tampilkanPesananButton.place(x=300, y=220, height=50, width=200)
prosesPesananButton = tk.Button(window, text="Proses Pesanan", command= lambda: prosesPesanan(IDPesanan.get(),statusBaru.get()))
prosesPesananButton.place(x=300, y=280, height=50, width=200)

# window.mainloop()