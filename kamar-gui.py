import tkinter as tk
import tkinter.messagebox
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rs_covid"
)
cursor = db.cursor()


def addKamar():
    idRs = idRumahSakit.get()
    harga = hargaKamar.get()
    jumlah = jumlahKamar.get()

    try:
        if(len(idRs) == 0 and len(harga) == 0 and len(jumlah) == 0):
            raise Exception("Masukkan Input!")
        elif(len(idRs) == 0):
            raise Exception("Input nama id rumah sakit!")
        elif(len(harga) == 0):
            raise Exception("Input alamat harga kamar!")
        elif(len(jumlah) == 0):
            raise Exception("Input jumlah kamar!")
        else:
            query = "SELECT * from rumahsakit WHERE id = %s"
            cursor.execute(query, (idRs, ))
            if(cursor.fetchone() == None):
                raise Exception("ID Rumah Sakit Tidak Valid")
            query = "INSERT INTO kamar (rumah_sakit_id, harga, jumlah) VALUES (%s, %s, %s)"
            cursor.execute(query, (idRs, harga, jumlah))
            db.commit()
            print(cursor.rowcount, "record inserted.")
    except Exception as err:
        tkinter.messagebox.showerror("Error", str(err))
    finally:
        idRumahSakitEntry.delete(0, 'end')
        hargaKamarEntry.delete(0, 'end')
        jumlahKamarEntry.delete(0, 'end')


window = tk.Tk()
window.title("Simple Text Editor")
window.geometry("800x800")
window.configure(background='#c8eed9')

# Title
title = tk.Label(text="INPUT DATA KAMAR")
title.config(font=("Calibri", 20, 'bold'))
title.config(background='#c8eed9')
title.pack(pady=20)

# Form
idRumahSakitLabel = tk.Label(text="ID Rumah Sakit")
idRumahSakitLabel.config(font=("Calibri", 16, 'bold'))
idRumahSakitLabel.config(background='#c8eed9')
idRumahSakitLabel.place(x=30, y=70)

hargaKamarLabel = tk.Label(text="Harga Kamar")
hargaKamarLabel.config(font=("Calibri", 16, 'bold'))
hargaKamarLabel.config(background='#c8eed9')
hargaKamarLabel.place(x=30, y=120)

jumlahKamarLabel = tk.Label(text="Jumlah Kamar")
jumlahKamarLabel.config(font=("Calibri", 16, 'bold'))
jumlahKamarLabel.config(background='#c8eed9')
jumlahKamarLabel.place(x=30, y=170)

colon1Label = tk.Label(text=":")
colon1Label.config(font=("Calibri", 16, 'bold'))
colon1Label.config(background='#c8eed9')
colon1Label.place(x=250, y=70)

colon2Label = tk.Label(text=":")
colon2Label.config(font=("Calibri", 16, 'bold'))
colon2Label.config(background='#c8eed9')
colon2Label.place(x=250, y=120)

colon2Label = tk.Label(text=":")
colon2Label.config(font=("Calibri", 16, 'bold'))
colon2Label.config(background='#c8eed9')
colon2Label.place(x=250, y=170)

idRumahSakit = tk.StringVar()
hargaKamar = tk.StringVar()
jumlahKamar = tk.StringVar()

idRumahSakitEntry = tk.Entry(textvariable=idRumahSakit, width="30")
hargaKamarEntry = tk.Entry(textvariable=hargaKamar, width="30")
jumlahKamarEntry = tk.Entry(textvariable=jumlahKamar, width="30")

idRumahSakitEntry.place(x=270, y=75)
hargaKamarEntry.place(x=270, y=125)
jumlahKamarEntry.place(x=270, y=175)

addKamarButton = tk.Button(
    window, text="Add New Kamar", command=addKamar)
addKamarButton.place(x=300, y=220)

window.mainloop()
