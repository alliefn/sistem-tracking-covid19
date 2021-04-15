import tkinter as tk
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rs_covid"
)
cursor = db.cursor()


def addRumahSakit():
    nama = namaRumahSakit.get()
    alamat = alamatRumahSakit.get()

    if(len(nama) != 0 and len(alamat) != 0):
        query = "INSERT INTO RUMAHSAKIT (nama, alamat) VALUES (%s, %s)"
        cursor.execute(query, (nama, alamat))
        db.commit()

        print(cursor.rowcount, "record inserted.")
    else:
        print("Please input field")


window = tk.Tk()
window.title("Simple Text Editor")
window.geometry("800x800")
window.configure(background='#c8eed9')

# Title
title = tk.Label(text="INPUT DATA RUMAH SAKIT")
title.config(font=("Calibri", 20, 'bold'))
title.config(background='#c8eed9')
title.pack(pady=20)

# Form
namaRumahSakitLabel = tk.Label(text="Nama Rumah Sakit")
namaRumahSakitLabel.config(font=("Calibri", 16, 'bold'))
namaRumahSakitLabel.config(background='#c8eed9')
namaRumahSakitLabel.place(x=30, y=70)

alamatRumahSakitLabel = tk.Label(text="Alamat Rumah Sakit")
alamatRumahSakitLabel.config(font=("Calibri", 16, 'bold'))
alamatRumahSakitLabel.config(background='#c8eed9')
alamatRumahSakitLabel.place(x=30, y=120)

colon1Label = tk.Label(text=":")
colon1Label.config(font=("Calibri", 16, 'bold'))
colon1Label.config(background='#c8eed9')
colon1Label.place(x=250, y=70)

colon2Label = tk.Label(text=":")
colon2Label.config(font=("Calibri", 16, 'bold'))
colon2Label.config(background='#c8eed9')
colon2Label.place(x=250, y=120)

namaRumahSakit = tk.StringVar()
alamatRumahSakit = tk.StringVar()

namaRumahSakitEntry = tk.Entry(textvariable=namaRumahSakit, width="30")
alamatRumahSakitEntry = tk.Entry(textvariable=alamatRumahSakit, width="30")
namaRumahSakitEntry.place(x=270, y=75)
alamatRumahSakitEntry.place(x=270, y=125)

addRumahSakitButton = tk.Button(
    window, text="Add New RumahSakit", command=addRumahSakit)
addRumahSakitButton.place(x=300, y=200)

window.mainloop()
