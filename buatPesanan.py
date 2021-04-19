# GUI Buat Pesanan Khusus Pengguna
from tampilkanDataKamar import *
import tkinter as tk
import mysql.connector

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
    

window = tk.Tk()
window.title("Proses Pesanan")
window.geometry("800x800")
window.configure(background='#c8eed9')

title = tk.Label(text="BUAT PESANAN")
title.config(font=("Calibri", 20, 'bold'))
title.config(background='#c8eed9')
title.pack(pady=20)

namaRSLabel = tk.Label(text="Masukkan nama RS\t:")
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
namaKamarEntry.place(x=320, y=70)

tampilkanDataKamarButton = tk.Button(window, text="Tampilkan Daftar Kamar", command=tampilkanDataKamar)
tampilkanDataKamarButton.place(x=300, y=220, height=50, width=200)
buatPesananButton = tk.Button(window, text="Pesan", command=prosesPesanan)
buatPesananButton.place(x=300, y=280, height=50, width=200)