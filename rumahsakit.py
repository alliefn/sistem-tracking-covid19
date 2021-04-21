import tkinter as tk
import mysql.connector
from style import *
from util import createNavbarAdmin, createNavbarPengguna

class MenuInsertRS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background=BG_COLOR)

        createNavbarAdmin(self)
        
        # Title
        self.title = tk.Label(self, text="INPUT DATA RUMAH SAKIT")
        self.title.config(font=TITLE_FONT)
        self.title.config(background=BG_COLOR)
        self.title.pack(pady=40)

        # Form
        self.namaRumahSakitLabel = tk.Label(self, text="Nama Rumah Sakit")
        self.namaRumahSakitLabel.config(font=LARGE_FONT)
        self.namaRumahSakitLabel.config(background=BG_COLOR)
        self.namaRumahSakitLabel.place(x=30, y=90)

        self.alamatRumahSakitLabel = tk.Label(self, text="Alamat Rumah Sakit")
        self.alamatRumahSakitLabel.config(font=LARGE_FONT)
        self.alamatRumahSakitLabel.config(background=BG_COLOR)
        self.alamatRumahSakitLabel.place(x=30, y=140)

        self.colon1Label = tk.Label(self, text=":")
        self.colon1Label.config(font=LARGE_FONT)
        self.colon1Label.config(background=BG_COLOR)
        self.colon1Label.place(x=250, y=90)

        self.colon2Label = tk.Label(self, text=":")
        self.colon2Label.config(font=LARGE_FONT)
        self.colon2Label.config(background=BG_COLOR)
        self.colon2Label.place(x=250, y=140)

        self.namaRumahSakit = tk.StringVar()
        self.alamatRumahSakit = tk.StringVar()

        self.namaRumahSakitEntry = tk.Entry(
            self, textvariable=self.namaRumahSakit, width="30")
        self.alamatRumahSakitEntry = tk.Entry(
            self, textvariable=self.alamatRumahSakit, width="30")
        self.namaRumahSakitEntry.place(x=270, y=95)
        self.alamatRumahSakitEntry.place(x=270, y=145)

        self.addRumahSakitButton = tk.Button(
            self, text="Add New RumahSakit", command=lambda: self.addRumahSakit())
        self.addRumahSakitButton.place(x=300, y=240)

    def addRumahSakit(self):
        nama = self.namaRumahSakit.get()
        alamat = self.alamatRumahSakit.get()

        if(len(nama) != 0 and len(alamat) != 0):
            query = "INSERT INTO RUMAHSAKIT (nama, alamat) VALUES (%s, %s)"
            self.controller.mycursor.execute(query, (nama, alamat))
            self.controller.dB.commit()

            print(self.controller.mycursor.rowcount, "record inserted.")
        else:
            print("Please input field")


class MenuInsertKamar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background=BG_COLOR)

        createNavbarAdmin(self)

        # Title
        self.title = tk.Label(self, text="INPUT DATA KAMAR")
        self.title.config(font=TITLE_FONT)
        self.title.config(background=BG_COLOR)
        self.title.pack(pady=40)

        # Form
        self.idRumahSakitLabel = tk.Label(self, text="ID Rumah Sakit")
        self.idRumahSakitLabel.config(font=LARGE_FONT)
        self.idRumahSakitLabel.config(background=BG_COLOR)
        self.idRumahSakitLabel.place(x=30, y=90)

        self.hargaKamarLabel = tk.Label(self, text="Harga Kamar")
        self.hargaKamarLabel.config(font=LARGE_FONT)
        self.hargaKamarLabel.config(background=BG_COLOR)
        self.hargaKamarLabel.place(x=30, y=140)

        self.jumlahKamarLabel = tk.Label(self, text="Jumlah Kamar")
        self.jumlahKamarLabel.config(font=LARGE_FONT)
        self.jumlahKamarLabel.config(background=BG_COLOR)
        self.jumlahKamarLabel.place(x=30, y=190)

        self.namaKamarLabel = tk.Label(self, text="Nama Kamar")
        self.namaKamarLabel.config(font=LARGE_FONT)
        self.namaKamarLabel.config(background=BG_COLOR)
        self.namaKamarLabel.place(x=30, y=240)

        self.colon1Label = tk.Label(self, text=":")
        self.colon1Label.config(font=LARGE_FONT)
        self.colon1Label.config(background=BG_COLOR)
        self.colon1Label.place(x=250, y=90)

        self.colon2Label = tk.Label(self, text=":")
        self.colon2Label.config(font=LARGE_FONT)
        self.colon2Label.config(background=BG_COLOR)
        self.colon2Label.place(x=250, y=140)

        self.colon2Label = tk.Label(self, text=":")
        self.colon2Label.config(font=LARGE_FONT)
        self.colon2Label.config(background=BG_COLOR)
        self.colon2Label.place(x=250, y=190)

        self.colon2Label = tk.Label(self, text=":")
        self.colon2Label.config(font=LARGE_FONT)
        self.colon2Label.config(background=BG_COLOR)
        self.colon2Label.place(x=250, y=240)

        self.idRumahSakit = tk.StringVar()
        self.hargaKamar = tk.StringVar()
        self.jumlahKamar = tk.StringVar()
        self.namaKamar = tk.StringVar()

        self.idRumahSakitEntry = tk.Entry(
            self, textvariable=self.idRumahSakit, width="30")
        self.hargaKamarEntry = tk.Entry(
            self, textvariable=self.hargaKamar, width="30")
        self.jumlahKamarEntry = tk.Entry(
            self, textvariable=self.jumlahKamar, width="30")
        self.namaKamarEntry = tk.Entry(
            self, textvariable=self.namaKamar, width="30")

        self.idRumahSakitEntry.place(x=270, y=95)
        self.hargaKamarEntry.place(x=270, y=145)
        self.jumlahKamarEntry.place(x=270, y=195)
        self.namaKamarEntry.place(x=270, y=245)

        self.addKamarButton = tk.Button(
            self, text="Add New Kamar", command=lambda: self.addKamar())
        self.addKamarButton.place(x=300, y=270)

    def addKamar(self):
        idRs = self.idRumahSakit.get()
        harga = self.hargaKamar.get()
        jumlah = self.jumlahKamar.get()
        nama = self.namaKamar.get()

        try:
            if(len(idRs) == 0 and len(harga) == 0 and len(jumlah) == 0 and len(nama) == 0):
                raise Exception("Masukkan Input!")
            elif(len(idRs) == 0):
                raise Exception("Input nama id rumah sakit!")
            elif(len(harga) == 0):
                raise Exception("Input alamat harga kamar!")
            elif(len(jumlah) == 0):
                raise Exception("Input jumlah kamar!")
            elif(len(nama) == 0):
                raise Exception("Masukkan nama kamar")
            else:
                query = "SELECT * from rumahsakit WHERE id = %s"
                self.controller.mycursor.execute(query, (idRs, ))
                if(self.controller.mycursor.fetchone() == None):
                    raise Exception("ID Rumah Sakit Tidak Valid")
                query = "INSERT INTO Kamar (rumah_sakit_id, harga, jumlah, nama) VALUES (%s, %s, %s, %s)"
                self.controller.mycursor.execute(
                    query, (idRs, harga, jumlah, nama))
                self.controller.dB.commit()
                print(self.controller.mycursor.rowcount, "record inserted.")
        except Exception as err:
            print(err)
            # tkinter.messagebox.showerror("Error", str(err))
        finally:
            idRumahSakitEntry.delete(0, 'end')
            hargaKamarEntry.delete(0, 'end')
            jumlahKamarEntry.delete(0, 'end')
            namaKamarEntry.delete(0, 'end')


class MenuUpdateKamar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background=BG_COLOR)

        createNavbarAdmin(self)

        # Title
        self.title = tk.Label(self, text="Update Data Kamar")
        self.title.config(font=TITLE_FONT)
        self.title.config(background=BG_COLOR)
        self.title.pack(pady=40)

        # Form
        self.idKamarLabel = tk.Label(self, text="ID Kamar")
        self.idKamarLabel.config(font=LARGE_FONT)
        self.idKamarLabel.config(background=BG_COLOR)
        self.idKamarLabel.place(x=30, y=90)

        self.hargaKamarLabel = tk.Label(self, text="Harga Kamar")
        self.hargaKamarLabel.config(font=LARGE_FONT)
        self.hargaKamarLabel.config(background=BG_COLOR)
        self.hargaKamarLabel.place(x=30, y=140)

        self.jumlahKamarLabel = tk.Label(self, text="Jumlah Kamar")
        self.jumlahKamarLabel.config(font=LARGE_FONT)
        self.jumlahKamarLabel.config(background=BG_COLOR)
        self.jumlahKamarLabel.place(x=30, y=190)

        self.colon1Label = tk.Label(self, text=":")
        self.colon1Label.config(font=LARGE_FONT)
        self.colon1Label.config(background=BG_COLOR)
        self.colon1Label.place(x=250, y=90)

        self.colon2Label = tk.Label(self, text=":")
        self.colon2Label.config(font=LARGE_FONT)
        self.colon2Label.config(background=BG_COLOR)
        self.colon2Label.place(x=250, y=140)

        self.colon2Label = tk.Label(self, text=":")
        self.colon2Label.config(font=LARGE_FONT)
        self.colon2Label.config(background=BG_COLOR)
        self.colon2Label.place(x=250, y=190)

        self.idKamar = tk.StringVar()
        self.hargaKamar = tk.StringVar()
        self.jumlahKamar = tk.StringVar()

        self.idKamarEntry = tk.Entry(
            self, textvariable=self.idKamar, width="30")
        self.hargaKamarEntry = tk.Entry(
            self, textvariable=self.hargaKamar, width="30")
        self.jumlahKamarEntry = tk.Entry(
            self, textvariable=self.jumlahKamar, width="30")

        self.idKamarEntry.place(x=270, y=95)
        self.hargaKamarEntry.place(x=270, y=145)
        self.jumlahKamarEntry.place(x=270, y=195)

        self.addKamarButton = tk.Button(
            self, text="Update Kamar", command=lambda: self.addKamar())
        self.addKamarButton.place(x=300, y=240)

    def addKamar(self):
        kamarId = self.idKamar.get()
        harga = self.hargaKamar.get()
        jumlah = self.jumlahKamar.get()

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
                self.controller.mycursor.execute(
                    query, (harga, jumlah, kamarId))
                self.controller.dB.commit()
                if(self.controller.mycursor.rowcount == 0):
                    raise Exception("Not Valid Input")
                print(self.controller.mycursor.rowcount, "record(s) affected")
        except Exception as err:
            print(err)
        finally:
            idKamarEntry.delete(0, 'end')
            hargaKamarEntry.delete(0, 'end')
            jumlahKamarEntry.delete(0, 'end')


class MenuUpdateRS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background=BG_COLOR)

        createNavbarAdmin(self)

        # Title
        self.title = tk.Label(text="UPDATE DATA RUMAH SAKIT")
        self.title.config(font=("Calibri", 20, 'bold'))
        self.title.config(background='#c8eed9')
        self.title.pack(pady=20)

        # Form
        self.namaRumahSakitLabel = tk.Label(text="ID Rumah Sakit")
        self.namaRumahSakitLabel.config(font=("Calibri", 16, 'bold'))
        self.namaRumahSakitLabel.config(background='#c8eed9')
        self.namaRumahSakitLabel.place(x=30, y=70)

        self.namaRumahSakitLabel = tk.Label(text="Nama Rumah Sakit Baru")
        self.namaRumahSakitLabel.config(font=("Calibri", 16, 'bold'))
        self.namaRumahSakitLabel.config(background='#c8eed9')
        self.namaRumahSakitLabel.place(x=30, y=120)

        self.alamatRumahSakitLabel = tk.Label(text="Alamat Rumah Sakit Baru")
        self.alamatRumahSakitLabel.config(font=("Calibri", 16, 'bold'))
        self.alamatRumahSakitLabel.config(background='#c8eed9')
        self.alamatRumahSakitLabel.place(x=30, y=170)

        self.colon1Label = tk.Label(text=":")
        self.colon1Label.config(font=("Calibri", 16, 'bold'))
        self.colon1Label.config(background='#c8eed9')
        self.colon1Label.place(x=270, y=70)

        self.colon2Label = tk.Label(text=":")
        self.colon2Label.config(font=("Calibri", 16, 'bold'))
        self.colon2Label.config(background='#c8eed9')
        self.colon2Label.place(x=270, y=120)

        self.colon2Label = tk.Label(text=":")
        self.colon2Label.config(font=("Calibri", 16, 'bold'))
        self.colon2Label.config(background='#c8eed9')
        self.colon2Label.place(x=270, y=170)

        self.idRumahSakit = tk.StringVar()
        self.namaRumahSakit = tk.StringVar()
        self.alamatRumahSakit = tk.StringVar()

        self.idRumahSakitEntry = tk.Entry(
            textvariable=self.idRumahSakit, width="30")
        self.namaRumahSakitEntry = tk.Entry(
            textvariable=self.namaRumahSakit, width="30")
        self.alamatRumahSakitEntry = tk.Entry(
            textvariable=self.alamatRumahSakit, width="30")
        idRumahSakitEntry.place(x=290, y=75)
        namaRumahSakitEntry.place(x=290, y=125)
        alamatRumahSakitEntry.place(x=290, y=175)

        self.addRumahSakitButton = tk.Button(
            self, text="Update RumahSakit", command=lambda: self.updateRumahSakit())
        addRumahSakitButton.place(x=300, y=220)

    def updateRumahSakit(self):
        idRs = self.idRumahSakit.get()
        nama = self.namaRumahSakit.get()
        alamat = self.alamatRumahSakit.get()

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
                self.controller.mycursor.execute(query, (nama, alamat, idRs))
                self.controller.dB.commit()
                if(self.controller.mycursor.rowcount == 0):
                    raise Exception("Not Valid Input")
                print(self.controller.mycursor.rowcount, "record(s) affected")
        except Exception as err:
            print(err)
            # tkinter.messagebox.showerror("Error", str(err))
        finally:
            self.idRumahSakitEntry.delete(0, 'end')
            self.namaRumahSakitEntry.delete(0, 'end')
            self.alamatRumahSakitEntry.delete(0, 'end')


def addRumahSakitTest(nama, alamat, mydb, mycursor):
    mycursor.execute(
        "SELECT * FROM rumahsakit WHERE nama = %s and alamat = %s", (nama, alamat))
    myresult = mycursor.fetchall()
    return myresult


def addKamarTest(idRs, harga, jumlah, nama, mydb, mycursor):
    mycursor.execute(
        "SELECT * FROM kamar WHERE rumah_sakit_id = %s and harga = %s and jumlah = %s and nama = %s", (idRs, harga, jumlah, nama))
    myresult = mycursor.fetchall()
    return myresult


def updateRumahSakitTest(idRs, nama, alamat, mydb, mycursor):
    mycursor.execute(
        "SELECT * FROM rumahsakit WHERE id = %s and nama = %s and alamat = %s", (idRs, nama, alamat))
    myresult = mycursor.fetchall()
    return myresult


def updateKamarTest(idKamar, idRs, harga, jumlah, nama, mydb, mycursor):
    mycursor.execute(
        "SELECT * FROM kamar WHERE id = %s and rumah_sakit_id = %s and harga = %s and jumlah = %s and nama = %s", (idKamar, idRs, harga, jumlah, nama))
    myresult = mycursor.fetchall()
    return myresult
