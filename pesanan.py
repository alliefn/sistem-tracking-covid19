import mysql.connector
import tkinter as tk
from tkinter import ttk
from style import *
from util import *
from tkinter import messagebox as mb
from datetime import datetime, timedelta
class MenuTampilPesanan(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background = BG_COLOR)
        self.updateTampilan()

    def updateTampilan(self):
        clearFrame(self)
        # Navbar Frame
        self.navbar = tk.Frame(self, width = 560, height = 25, relief = tk.GROOVE, borderwidth=1)
    
        #Order button
        self.confirmPesananBtn = tk.Button(master=self.navbar, text="Home", cursor="hand2", highlightthickness = 0, bd = 0, command=lambda:self.controller.show_frame("AdminHome"))
        self.confirmPesananBtn.configure(font=SMALL_FONT)
        self.confirmPesananBtn.config(background=BG_COLOR)
        self.confirmPesananBtn.config(width=20)
        self.confirmPesananBtn.pack(side=tk.LEFT, padx=5)

        self.navbar.grid(row=0,column=0)
        self.navbar.configure(background=BG_COLOR)    

        self.controller.mycursor.execute("SELECT * FROM pesanan;")
        result = self.controller.mycursor.fetchall()
        i = 0

        for tup in result:
            i = i + 1
        # b = tk.Button(self, width = 20, font=('Arial',10), fg="black", text="Proses", command = lambda:self.prosesPesanan(result[r-1][0]))
        # b.grid(row=1,column=0)
        # e = tk.Entry(self,width=20, font=('Arial',12), fg="black")
        # e.grid(row=1,column=1)
        for r in range(i+1):
            for c in range(1,6):
                if(c == 1 and r != 0):
                    b = tk.Button(self, width = 20, height = 1, font=('Arial',10), fg="black", text="Proses", command = lambda:self.prosesPesanan(result[r-1][0]))
                    b.grid(row=r+2,column=c-1)
                else:
                    e = tk.Text(self, width=20, height = 1, font=('Arial',14), fg="black")
                    e.grid(row=r+2,column=c-1)
                    if (r == 0):
                        if ( c == 1):
                            e.insert(tk.END,"Proses")
                        elif (c == 2):
                            e.insert(tk.END,"Username")
                        elif (c == 3):
                            e.insert(tk.END,"Status")
                        elif (c == 4):
                            e.insert(tk.END,"Tanggal Pemesanan")
                        else:
                            e.insert(tk.END,"Status Konfirmasi")
                    else:    
                        e.insert(tk.END,result[r-1][c])
                    # e.config(state="readonly")
    
    def prosesPesanan(self, idPesanan):
        self.controller.mycursor.execute("SELECT username, id_kamar FROM pesanan;")
        result = self.controller.mycursor.fetchall()
        
        uname = result[0][0]
        id_kamar = result[0][1]

        self.controller.mycursor.execute("SELECT k.nama, rs.nama FROM kamar k inner join rumahsakit rs on rs.id = k.rumah_sakit_id where k.id = " + getStringFromResult(id_kamar))
        result = self.controller.mycursor.fetchall()
        
        namaKamar = result[0][0]
        namaRS = result[0][1]

        self.controller.mycursor.execute("SELECT nama FROM user where username = '" + uname + "'")
        result = self.controller.mycursor.fetchall()
        
        nama = result[0][0]

        self.controller.frames["MenuProsesPesanan"].tampilkanProsesPesanan(idPesanan, nama, namaRS, namaKamar, uname)
class MenuBuatPesanan(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background = BG_COLOR)

        createNavbarPengguna(self)

        #TITLE
        self.title = tk.Label(self, text="BUAT PESANAN")
        self.title.config(font=TITLE_FONT)
        self.title.config(background=BG_COLOR)
        self.title.pack(pady=40)

        self.namaRSLabel = tk.Label(self, text="Masukkan nama RS\t\t:")
        self.namaRSLabel.config(font=LARGE_FONT)
        self.namaRSLabel.config(background=BG_COLOR)
        self.namaRSLabel.place(x=30, y=90)

        self.namaKamarLabel = tk.Label(self, text="Masukkan nama Kamar\t:")
        self.namaKamarLabel.config(font=LARGE_FONT)
        self.namaKamarLabel.config(background=BG_COLOR)
        self.namaKamarLabel.place(x=30, y=140)

        namaRS = tk.StringVar()  
        namaKamar = tk.StringVar()

        self.namaRSEntry = tk.Entry(self, textvariable=namaRS, width="30")
        self.namaRSEntry.place(x=320, y=100)
        self.namaKamarEntry = tk.Entry(self, textvariable=namaKamar, width="30")
        self.namaKamarEntry.place(x=320, y=150)

        self.tampilkanDataKamarButton = tk.Button(self,  text="Tampilkan Daftar Kamar", command=lambda:self.controller.show_frame("MenuTampilDataKamar"))
        self.tampilkanDataKamarButton.place(x=300, y=200, width=200)
        self.buatPesananButton = tk.Button(self,  text="Pesan", command=lambda:self.buatPesanan())
        self.buatPesananButton.place(x=300, y=260, width=200)

        self.surpriseLabel = tk.Label(self, text="Catatan: PERBESAR LAYAR KE KANAN UNTUK MELIHAT JUMLAH KAMAR \nYANG TERSEDIA SAAT MELIHAT TABEL KAMAR")
        self.surpriseLabel.config(font=("Calibri", 12, 'bold'))
        self.surpriseLabel.config(background=BG_COLOR)
        self.surpriseLabel.place(x=30, y=350)

    def buatPesanan(self):
        # Siapin value yang mau dimasukin
        kamar = self.namaKamarEntry.get()
        rs = self.namaRSEntry.get()
        idKamar = getIDKamar(self.controller.mycursor,kamar,rs)
        nowDate =  getNowDateAsString()
        user = self.controller.username # NANTI PAS DIBUAT MAIN PROGRAM, KASIH INI AKSES KE GLOBAL VARIABLE USERNAME BUAT TAU SIAPA YG LOGIN T_T
        
        # Cek apakah terjadi kesamaan id pesanan pada tabel dan yang baru di-generate
        if((not checkIfUserBooked(self.controller.mycursor, user)) and len(idKamar) > 0):
            idKamar = str(idKamar[0])

            insertQuery = "INSERT INTO pesanan(id_kamar, username, status, tanggal_pesan, is_confirmed) VALUES (%s,%s,%s,%s,%s);"
            val = (idKamar, user,"On Hold",nowDate,"Belum")
            self.controller.mycursor.execute(insertQuery,val)
            self.controller.dB.commit()
            isError = False
            self.controller.frames["MenuTampilPesanan"].updateTampilan()
            self.loadKonfirmasiPesanan(idKamar)
        else:
            mb.showwarning("Tidak Dapat Melakukan Pesanan", "Anda sudah melakukan pemesanan dan tidak dapat memesan kamar lagi sampai Admin mengonfirmasi pesanan Anda")
    
    def loadKonfirmasiPesanan(self, IDKamar):    
        searchQuery = "select harga from kamar where id=" + str(IDKamar) + ";"
        self.controller.mycursor.execute(searchQuery)
        result = self.controller.mycursor.fetchall()
        uang = "Rp" + getStringFromResult(result[0])
        self.controller.frames["MenuKonfirmasiPesanan"].jumlahUangLabel.config(text=uang)
        self.controller.show_frame("MenuKonfirmasiPesanan")

def buatPesananTest(RS,Kamar,User):
    dB = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="trackingCovid"
        )
    mycursor = dB.cursor()
    query = "select * from pesanan where username=\'" + User + "\' and id_kamar=" + getStringFromResult(getIDKamar(mycursor,Kamar,RS)) + ";"
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result

class MenuKonfirmasiPesanan(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background = BG_COLOR)

        createNavbarAdmin(self)

        self.title = tk.Label(self, text="BUAT PESANAN")
        self.title.config(font=TITLE_FONT)
        self.title.config(background=BG_COLOR)
        self.title.pack(pady=20)

        self.berhasilLabel = tk.Label(self, text="Pesanan Berhasil Dibuat!")
        self.berhasilLabel.config(font=LARGE_FONT)
        self.berhasilLabel.config(background=BG_COLOR)
        self.berhasilLabel.place(x=300, y=70)

        self.transferLabel = tk.Label(self, text="Silakan lakukan pembayaran melalui transfer bank")
        self.transferLabel.config(font=LARGE_FONT)
        self.transferLabel.config(background=BG_COLOR)
        self.transferLabel.place(x=200, y=120)

        self.bankLabel = tk.Label(self, text="ABC sebesar")
        self.bankLabel.config(font=LARGE_FONT)
        self.bankLabel.config(background=BG_COLOR)
        self.bankLabel.place(x=350, y=140)

        uang = ""
        self.jumlahUangLabel = tk.Label(self, text=uang)
        self.jumlahUangLabel.config(font=LARGE_FONT)
        self.jumlahUangLabel.config(background=BG_COLOR)
        self.jumlahUangLabel.place(x=340, y=180)

        self.konfirmasiLabel = tk.Label(self, text="Masukkan username Anda dan klik tombol di bawah jika telah melakukan transfer")
        self.konfirmasiLabel.config(font=LARGE_FONT)
        self.konfirmasiLabel.config(background=BG_COLOR)
        self.konfirmasiLabel.place(x=100, y=230)

        user = tk.StringVar()
        self.userEntry = tk.Entry(self, textvariable=user, width="30")
        self.userEntry.place(x=260, y=255)

        self.konfirmasiButton = tk.Button(self, text="Konfirmasi Pesanan", command= lambda: self.changeToSudah())
        self.konfirmasiButton.place(x=320, y=290, height=50, width=150)

    def changeToSudah(self):
        user = self.controller.username
        query = "update pesanan set is_confirmed=\'Sudah\' where username=\"" + user+"\""
        self.controller.mycursor.execute(query)
        self.controller.dB.commit()
        mb.showinfo('Berhasil!', 'Konfirmasi pembayaran telah diterima!')

class MenuProsesPesanan(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background = BG_COLOR)

        createNavbarAdmin(self)

        self.namaLabel = tk.Label(self, text="Nama \t\t:")
        self.namaLabel.config(font=LARGE_FONT)
        self.namaLabel.config(background=BG_COLOR)
        self.namaLabel.place(x=30, y=70)

        self.rsLabel = tk.Label(self, text="Rumah Sakit\t:")
        self.rsLabel.config(font=LARGE_FONT)
        self.rsLabel.config(background=BG_COLOR)
        self.rsLabel.place(x=30, y=120)

        self.kamarLabel = tk.Label(self, text="Kamar\t\t:")
        self.kamarLabel.config(font=LARGE_FONT)
        self.kamarLabel.config(background=BG_COLOR)
        self.kamarLabel.place(x=30, y=170)

        self.suhuLabel = tk.Label(self, text="Suhu 3 hari terakhir\t:")
        self.suhuLabel.config(font=LARGE_FONT)
        self.suhuLabel.config(background=BG_COLOR)
        self.suhuLabel.place(x=30, y=220)

        self.IDPesanan = tk.StringVar()  
        self.statusBaru = tk.StringVar()

        self.statusBaruEntry = ttk.Combobox(self,width=30,textvariable=self.statusBaru)
        self.statusBaruEntry['values'] = ('On Hold', 'Diterima', 'Ditolak')
        self.statusBaruEntry.place(x=30, y=270)

        self.prosesPesananButton = tk.Button(self, text="Proses Pesanan", cursor="hand2", command= lambda: self.prosesPesanan(self.IDPesanan.get(),self.statusBaru.get()))
        self.prosesPesananButton.place(x=280, y=270, width=250)

    def tampilkanProsesPesanan(self, idPesanan, nama, namaRS, namaKamar, username):
        self.namaLabel.config(text = "Nama \t\t: " + str(nama))
        self.rsLabel.config(text = "Rumah Sakit\t: " + str(namaRS))
        self.kamarLabel.config(text = "Kamar\t\t: " + str(namaKamar))

        tgl1 = datetime.now()
        tgl2 = datetime.now() - timedelta(days=1)
        tgl3 = datetime.now() - timedelta(days=2)

        query = "select value from suhu where username = %s and (tanggal_input = %s or tanggal_input = %s or tanggal_input = %s)"
        self.controller.mycursor.execute("select value from suhu where username = %s and (tanggal_input = %s or tanggal_input = %s or tanggal_input = %s)", (str(username), str(tgl1), str(tgl2), str(tgl3)))
        result = self.controller.mycursor.fetchall()

        suhutext = "Suhu 3 hari terakhir\t: "
        i = 0
        while(i < 3 and i < len(result)):
            suhutext += str(result[i]) + " "
            i += 1

        while(i < 3):
            suhutext += "- "
            i += 1

        self.suhuLabel.config(text=suhutext)
        self.prosesPesananButton.config(command= lambda: self.prosesPesanan(idPesanan))
        self.controller.show_frame("MenuProsesPesanan")

    def prosesPesanan(self,idPesanan):
        
        # Menerima atau menolak pesanan oleh admin
        ID = idPesanan
        status = self.statusBaru.get()

        # Mengurangi jumlah kamar yang tersedia jika pesanan diterima
        if (status == 'Diterima'):
            queryKurangiKamar = "UPDATE kamar SET jumlah=jumlah-1 WHERE id IN (SELECT id_kamar FROM pesanan WHERE id_pesanan=" + str(ID) + ");"
            self.controller.mycursor.execute(queryKurangiKamar)
            self.controller.dB.commit()
        # IDPesananPilihan = result[nomorPesanan-1][0]

        dummy = updateQuery(status,ID,self.controller.dB,self.controller.mycursor)

        mb.showinfo('Berhasil!', 'Status Pesanan berhasil di-update!')
        self.controller.frames["MenuTampilPesanan"].updateTampilan()


class MenuTampilDataKamar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background = BG_COLOR)
        self.updateTampilan()

    def updateTampilan(self):
        clearFrame(self)
        # Navbar Frame
        self.navbar = tk.Frame(self, width = 560, height = 25, relief = tk.GROOVE, borderwidth=1)
    
        #Order button
        self.buatPesananbtn = tk.Button(master=self.navbar, text="Buat Pesanan", cursor="hand2", highlightthickness = 0, bd = 0, command=lambda:self.controller.show_frame("MenuBuatPesanan"))
        self.buatPesananbtn.configure(font=SMALL_FONT)
        self.buatPesananbtn.config(background=BG_COLOR)
        self.buatPesananbtn.config(width=30)
        self.buatPesananbtn.pack(side=tk.LEFT, padx=5)

        self.navbar.grid(row=0,column=0)
        self.navbar.configure(background=BG_COLOR)
        
        self.controller.mycursor.execute("SELECT k.nama,rs.nama,rs.alamat,k.harga,k.jumlah FROM kamar as k inner join rumahsakit as rs on k.rumah_sakit_id=rs.id;")
        result = self.controller.mycursor.fetchall()
        print(result)
        i = 0
        for tup in result:
            i = i + 1
        for r in range(i+1):
            for c in range(5):
                e = tk.Entry(self,width=30, font=('Arial',12), fg="black")
                e.grid(row=r+1,column=c)
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
                e.config(state="readonly")

# class MenuTampilStatusPesanan(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#     self.controller = controller
#     self.configure(background = BG_COLOR)
#     self.updateTampilan()

#         self.namaLabel = tk.Label(self, text="Nama \t\t:")
#         self.namaLabel.config(font=LARGE_FONT)
#         self.namaLabel.config(background=BG_COLOR)
#         self.namaLabel.place(x=30, y=70)

#         self.rsLabel = tk.Label(self, text="Rumah Sakit\t:")
#         self.rsLabel.config(font=LARGE_FONT)
#         self.rsLabel.config(background=BG_COLOR)
#         self.rsLabel.place(x=30, y=120)

#         self.kamarLabel = tk.Label(self, text="Kamar\t\t:")
#         self.kamarLabel.config(font=LARGE_FONT)
#         self.kamarLabel.config(background=BG_COLOR)
#         self.kamarLabel.place(x=30, y=170)