import tkinter as tk
import mysql.connector

def tampilkanDataKamar():
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dika090301",
    database="trackingCovid"
    )
    cursor_db = db.cursor()

    window = tk.Tk()
    window.title("Tabel Kamar - PERBESAR LAYAR KE KANAN UNTUK MELIHAT JUMLAH KAMAR YANG TERSEDIA")
    window.geometry("800x800")
    window.configure(background='#c8eed9')

    cursor_db.execute("SELECT k.nama_kamar,rs.nama,rs.alamat,k.harga,k.jumlah FROM kamar as k, rumahsakit as rs WHERE k.id_RS=rs.id_RS;")
    result = cursor_db.fetchall()
    i = 0
    for tup in result:
        i = i + 1
    for r in range(i+1):
        for c in range(5):
            e = tk.Entry(window,width=30, font=('Arial',12), fg="black")
            e.grid(row=r,column=c)
            if (r == 0):
                if (c == 0):
                    e.insert(tk.END,"Nama Kamar")
                elif (c == 1):
                    e.insert(tk.END,"Nama RS")
                elif (c == 2):
                    e.insert(tk.END,"Alamat RS")
                elif (c == 3):
                    e.insert(tk.END,"Harga")
                else:
                    e.insert(tk.END,"Jumlah Tersisa")
            else:
                e.insert(tk.END,result[r-1][c])

    window.mainloop()