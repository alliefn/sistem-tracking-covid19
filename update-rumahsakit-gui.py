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


def updateRumahSakit():
    idRs = idRumahSakit.get()
    nama = namaRumahSakit.get()
    alamat = alamatRumahSakit.get()

    try:
        if(len(nama) == 0 and len(alamat) == 0 and len(idRs) == 0):
            raise Exception("Lengkapi input!")
        elif(len(nama) == 0):
            raise Exception("Input nama rumah sakit!")
        elif(len(alamat) == 0):
            raise Exception("Input alamat rumah sakit!")
        elif(len(idRs) == 0):
            raise Exception("Input id rumah sakit!")
        else:
            query = "UPDATE rumahsakit SET nama = %s, alamat = %s WHERE id = %s"
            cursor.execute(query, (nama, alamat, idRs))
            db.commit()
            if(cursor.rowcount == 0):
                raise Exception("Not Valid Input")
            print(cursor.rowcount, "record(s) affected")
    except Exception as err:
        tkinter.messagebox.showerror("Error", str(err))
    finally:
        idRumahSakitEntry.delete(0, 'end')
        namaRumahSakitEntry.delete(0, 'end')
        alamatRumahSakitEntry.delete(0, 'end')


window = tk.Tk()
window.title("Simple Text Editor")
window.geometry("800x800")
window.configure(background='#c8eed9')

# Title
title = tk.Label(text="UPDATE DATA RUMAH SAKIT")
title.config(font=("Calibri", 20, 'bold'))
title.config(background='#c8eed9')
title.pack(pady=20)

# Form
namaRumahSakitLabel = tk.Label(text="ID Rumah Sakit")
namaRumahSakitLabel.config(font=("Calibri", 16, 'bold'))
namaRumahSakitLabel.config(background='#c8eed9')
namaRumahSakitLabel.place(x=30, y=70)

namaRumahSakitLabel = tk.Label(text="Nama Rumah Sakit Baru")
namaRumahSakitLabel.config(font=("Calibri", 16, 'bold'))
namaRumahSakitLabel.config(background='#c8eed9')
namaRumahSakitLabel.place(x=30, y=120)

alamatRumahSakitLabel = tk.Label(text="Alamat Rumah Sakit Baru")
alamatRumahSakitLabel.config(font=("Calibri", 16, 'bold'))
alamatRumahSakitLabel.config(background='#c8eed9')
alamatRumahSakitLabel.place(x=30, y=170)

colon1Label = tk.Label(text=":")
colon1Label.config(font=("Calibri", 16, 'bold'))
colon1Label.config(background='#c8eed9')
colon1Label.place(x=270, y=70)

colon2Label = tk.Label(text=":")
colon2Label.config(font=("Calibri", 16, 'bold'))
colon2Label.config(background='#c8eed9')
colon2Label.place(x=270, y=120)

colon2Label = tk.Label(text=":")
colon2Label.config(font=("Calibri", 16, 'bold'))
colon2Label.config(background='#c8eed9')
colon2Label.place(x=270, y=170)

idRumahSakit = tk.StringVar()
namaRumahSakit = tk.StringVar()
alamatRumahSakit = tk.StringVar()

idRumahSakitEntry = tk.Entry(textvariable=idRumahSakit, width="30")
namaRumahSakitEntry = tk.Entry(textvariable=namaRumahSakit, width="30")
alamatRumahSakitEntry = tk.Entry(textvariable=alamatRumahSakit, width="30")
idRumahSakitEntry.place(x=290, y=75)
namaRumahSakitEntry.place(x=290, y=125)
alamatRumahSakitEntry.place(x=290, y=175)

addRumahSakitButton = tk.Button(
    window, text="Update RumahSakit", command=updateRumahSakit)
addRumahSakitButton.place(x=300, y=220)

window.mainloop()
