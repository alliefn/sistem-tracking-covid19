import tkinter as tk
import mysql.connector

def tampilkanPesanan():
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dika090301",
    database="trackingCovid"
    )
    cursor_db = db.cursor()

    window = tk.Tk()
    window.title("Tabel Pesanan")
    window.geometry("800x800")
    window.configure(background='#c8eed9')

    cursor_db.execute("SELECT * FROM pesanan;")
    result = cursor_db.fetchall()
    i = 0
    for tup in result:
        i = i + 1
    for r in range(i+1):
        for c in range(5):
            e = tk.Entry(window,width=20, font=('Arial',12), fg="black")
            e.grid(row=r,column=c)
            if (r == 0):
                if (c == 0):
                    e.insert(tk.END,"ID Pesanan")
                elif (c == 1):
                    e.insert(tk.END,"ID Kamar")
                elif (c == 2):
                    e.insert(tk.END,"Username")
                elif (c == 3):
                    e.insert(tk.END,"Status")
                else:
                    e.insert(tk.END,"Tanggal Pemesanan")
            else:    
                e.insert(tk.END,result[r-1][c])
    
    window.mainloop()