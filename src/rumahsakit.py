import tkinter as tk
import tkinter.messagebox as mb
import mysql.connector
from style import *
from util import createNavbarAdmin, createNavbarPengguna, clearFrame


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

        try:
            if(len(nama) == 0 and len(alamat) == 0):
                raise Exception("Input nama dan alamat rumah sakit!")
            elif(len(nama) == 0):
                raise Exception("Input nama rumah sakit!")
            elif(len(alamat) == 0):
                raise Exception("Input alamat rumah sakit!")
            else:
                query = "INSERT INTO RUMAHSAKIT (nama, alamat) VALUES (%s, %s)"
                self.controller.mycursor.execute(query, (nama, alamat))
                self.controller.dB.commit()
                print(self.controller.mycursor.rowcount, "record inserted.")
                self.controller.frames["MenuTampilDataRS"].updateTampilan()
                self.controller.frames["MenuTampilDataKamar"].updateTampilan()
        except Exception as err:
            mb.showerror("Error", str(err))
        finally:
            self.namaRumahSakitEntry.delete(0, 'end')
            self.alamatRumahSakitEntry.delete(0, 'end')


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

        self.info = tk.Label(
            self, text="Untuk id rumah sakit dapat dilihat di Page \nDaftar Kamar dan Rumah Sakit")
        self.info.config(font=MEDIUM_FONT)
        self.info.config(background=BG_COLOR)
        self.info.place(x=100, y=320)

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

                self.controller.frames["MenuTampilDataRS"].updateTampilan()
                self.controller.frames["MenuTampilDataKamar"].updateTampilan()
        except Exception as err:
            mb.showerror("Error", str(err))
        finally:
            self.idRumahSakitEntry.delete(0, 'end')
            self.hargaKamarEntry.delete(0, 'end')
            self.jumlahKamarEntry.delete(0, 'end')
            self.namaKamarEntry.delete(0, 'end')


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

        self.info = tk.Label(
            self, text="Untuk id kamar dapat dilihat di Page \nDaftar Kamar dan Rumah Sakit")
        self.info.config(font=MEDIUM_FONT)
        self.info.config(background=BG_COLOR)
        self.info.place(x=100, y=320)

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

                self.controller.frames["MenuTampilDataRS"].updateTampilan()
                self.controller.frames["MenuTampilDataKamar"].updateTampilan()
        except Exception as err:
            mb.showerror("Error", str(err))
        finally:
            self.idKamarEntry.delete(0, 'end')
            self.hargaKamarEntry.delete(0, 'end')
            self.jumlahKamarEntry.delete(0, 'end')


class MenuUpdateRS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background=BG_COLOR)

        createNavbarAdmin(self)

        # Title
        self.title = tk.Label(self, text="UPDATE DATA RUMAH SAKIT")
        self.title.config(font=TITLE_FONT)
        self.title.config(background=BG_COLOR)
        self.title.pack(pady=40)

        # Form
        self.namaRumahSakitLabel = tk.Label(self, text="ID Rumah Sakit")
        self.namaRumahSakitLabel.config(font=LARGE_FONT)
        self.namaRumahSakitLabel.config(background=BG_COLOR)
        self.namaRumahSakitLabel.place(x=30, y=90)

        self.namaRumahSakitLabel = tk.Label(self, text="Nama Rumah Sakit Baru")
        self.namaRumahSakitLabel.config(font=LARGE_FONT)
        self.namaRumahSakitLabel.config(background=BG_COLOR)
        self.namaRumahSakitLabel.place(x=30, y=140)

        self.alamatRumahSakitLabel = tk.Label(
            self, text="Alamat Rumah Sakit Baru")
        self.alamatRumahSakitLabel.config(font=LARGE_FONT)
        self.alamatRumahSakitLabel.config(background=BG_COLOR)
        self.alamatRumahSakitLabel.place(x=30, y=190)

        self.colon1Label = tk.Label(self, text=":")
        self.colon1Label.config(font=LARGE_FONT)
        self.colon1Label.config(background=BG_COLOR)
        self.colon1Label.place(x=270, y=90)

        self.colon2Label = tk.Label(self, text=":")
        self.colon2Label.config(font=LARGE_FONT)
        self.colon2Label.config(background=BG_COLOR)
        self.colon2Label.place(x=270, y=140)

        self.colon2Label = tk.Label(self, text=":")
        self.colon2Label.config(font=LARGE_FONT)
        self.colon2Label.config(background=BG_COLOR)
        self.colon2Label.place(x=270, y=190)

        self.idRumahSakit = tk.StringVar()
        self.namaRumahSakit = tk.StringVar()
        self.alamatRumahSakit = tk.StringVar()

        self.idRumahSakitEntry = tk.Entry(
            self, textvariable=self.idRumahSakit, width="30")
        self.namaRumahSakitEntry = tk.Entry(
            self, textvariable=self.namaRumahSakit, width="30")
        self.alamatRumahSakitEntry = tk.Entry(
            self, textvariable=self.alamatRumahSakit, width="30")
        self.idRumahSakitEntry.place(x=290, y=95)
        self.namaRumahSakitEntry.place(x=290, y=145)
        self.alamatRumahSakitEntry.place(x=290, y=195)

        self.addRumahSakitButton = tk.Button(
            self, text="Update RumahSakit", command=lambda: self.updateRumahSakit())
        self.addRumahSakitButton.place(x=300, y=240)

        self.info = tk.Label(
            self, text="Untuk id rumah sakit dapat dilihat di Page \nDaftar Kamar dan Rumah Sakit")
        self.info.config(font=MEDIUM_FONT)
        self.info.config(background=BG_COLOR)
        self.info.place(x=100, y=320)

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

                self.controller.frames["MenuTampilDataRS"].updateTampilan()
                self.controller.frames["MenuTampilDataKamar"].updateTampilan()
        except Exception as err:
            mb.showerror("Error", str(err))
        finally:
            self.idRumahSakitEntry.delete(0, 'end')
            self.namaRumahSakitEntry.delete(0, 'end')
            self.alamatRumahSakitEntry.delete(0, 'end')


class MenuTampilDataRS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background=BG_COLOR)
        self.updateTampilan()

    def updateTampilan(self):
        clearFrame(self)
        self.data = tk.Frame(self)
        self.homeButton = tk.Button(self, text = "Home",command=lambda : frame.controller.show_frame("AdminHome"))
        self.homeButton.pack()

        self.homeButton = tk.Button(
            self, text="Home", command=lambda: self.controller.show_frame("AdminHome"))
        self.homeButton.pack()

        self.controller.mycursor.execute(
            "SELECT k.nama,rs.nama,rs.alamat, k.id, rs.id FROM kamar as k, rumahsakit as rs WHERE k.rumah_sakit_id=rs.id;")
        result = self.controller.mycursor.fetchall()

        i = 0
        for tup in result:
            i = i + 1
        for r in range(i+1):
            for c in range(5):
                e = tk.Entry(self.data, width=30,
                             font=('Arial', 12), fg="black")
                e.grid(row=r, column=c)
                if (r == 0):
                    if (c == 0):
                        e.insert(tk.END, "Nama Kamar")
                    elif (c == 1):
                        e.insert(tk.END, "Nama RS")
                    elif (c == 2):
                        e.insert(tk.END, "Alamat RS")
                    elif (c == 3):
                        e.insert(tk.END, "Id Kamar")
                    else:
                        e.insert(tk.END, "Id Rumah Sakit")
                else:
                    e.insert(tk.END, result[r-1][c])
                e.config(state="readonly")

        self.data.pack()

        self.warning = tk.Label(
            self, text="PERBESAR LAYAR KE KANAN UNTUK MELIHAT JUMLAH KAMAR YANG TERSEDIA")
        self.warning.pack()
        self.warning.config(bg=BG_COLOR)
        self.warning.config(font=LARGE_FONT)


class MenuTampilDataRS2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background=BG_COLOR)
        self.updateTampilan()

    def updateTampilan(self):
        clearFrame(self)
        self.data = tk.Frame(self)

        self.homeButton = tk.Button(
            self, text="Home", command=lambda: self.controller.show_frame("AdminHome"))
        self.homeButton.pack()

        self.controller.mycursor.execute(
            "SELECT rs.id, rs.nama, rs.alamat FROM rumahsakit as rs;")
        result = self.controller.mycursor.fetchall()

        i = 0
        for tup in result:
            i = i + 1
        for r in range(i+1):
            for c in range(3):
                e = tk.Entry(self.data, width=30,
                             font=('Arial', 12), fg="black")
                e.grid(row=r, column=c)
                if (r == 0):
                    if (c == 0):
                        e.insert(tk.END, "ID RS")
                    elif (c == 1):
                        e.insert(tk.END, "Nama RS")
                    elif (c == 2):
                        e.insert(tk.END, "Alamat RS")
                else:
                    e.insert(tk.END, result[r-1][c])
                e.config(state="readonly")

        self.data.pack()

        self.warning = tk.Label(
            self, text="PERBESAR LAYAR KE KANAN UNTUK MELIHAT JUMLAH KAMAR YANG TERSEDIA")
        self.warning.pack()
        self.warning.config(bg=BG_COLOR)
        self.warning.config(font=LARGE_FONT)


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
