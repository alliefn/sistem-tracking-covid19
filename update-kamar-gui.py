import tkinter as tk
import tkinter.messagebox
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kytnsx88",
    database="rs_covid"
)
cursor = db.cursor()


def addKamar():
    kamarId = idKamar.get()
    harga = hargaKamar.get()
    jumlah = jumlahKamar.get()

    try:
        if(len(kamarId) == 0 and len(harga) == 0 and len(jumlah) == 0):
            raise Exception("Masukkan Input!")
        elif(len(kamarId) == 0):
            raise Exception("Input kamar id!")
        elif(len(harga) == 0):
            raise Exception("Input alamat harga kamar!")
        elif(len(jumlah) == 0):
            raise Exception("Input jumlah kamar!")
        else:
            query = "UPDATE kamar SET harga = %s, jumlah = %s WHERE id = %s"
            cursor.execute(query, (harga, jumlah, kamarId))
            db.commit()
            if(cursor.rowcount == 0):
                raise Exception("Not Valid Input")
            print(cursor.rowcount, "record(s) affected")
    except Exception as err:
        tkinter.messagebox.showerror("Error", str(err))
    finally:
        idKamarEntry.delete(0, 'end')
        hargaKamarEntry.delete(0, 'end')
        jumlahKamarEntry.delete(0, 'end')


window = tk.Tk()
window.title("Simple Text Editor")
window.geometry("800x800")
window.configure(background='#c8eed9')

# Title
title = tk.Label(text="Update Data Kamar")
title.config(font=("Calibri", 20, 'bold'))
title.config(background='#c8eed9')
title.pack(pady=20)

# Form
idKamarLabel = tk.Label(text="ID Kamar")
idKamarLabel.config(font=("Calibri", 16, 'bold'))
idKamarLabel.config(background='#c8eed9')
idKamarLabel.place(x=30, y=70)

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

idKamar = tk.StringVar()
hargaKamar = tk.StringVar()
jumlahKamar = tk.StringVar()

idKamarEntry = tk.Entry(textvariable=idKamar, width="30")
hargaKamarEntry = tk.Entry(textvariable=hargaKamar, width="30")
jumlahKamarEntry = tk.Entry(textvariable=jumlahKamar, width="30")

idKamarEntry.place(x=270, y=75)
hargaKamarEntry.place(x=270, y=125)
jumlahKamarEntry.place(x=270, y=175)

addKamarButton = tk.Button(
    window, text="Update Kamar", command=addKamar)
addKamarButton.place(x=300, y=220)

window.mainloop()
