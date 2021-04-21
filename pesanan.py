import mysql.connector
import tkinter as tk
from style import *
from util import *
from tkinter import messagebox as mb

class MenuTampilPesanan(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background = BG_COLOR)

        # Navbar Frame
        self.navbar = tk.Frame(self, width = 560, height = 25, relief = tk.GROOVE, borderwidth=1)
        self.navbar.place(x=0, y=0, height = 25, width = 560)
        self.navbar.configure(background=BG_COLOR)

        # #Profile button
        # self.menuSuhuButton = tk.Button(master=self.navbar, text="Profile", cursor="hand2", highlightthickness = 0, bd = 0)
        # self.menuSuhuButton.configure(font=SMALL_FONT)
        # self.menuSuhuButton.config(background=BG_COLOR)
        # self.menuSuhuButton.pack(side=tk.RIGHT, padx=5)

        # Label admin page
        self.lbl_mainpg = tk.Label(master=self.navbar, text="Sistem Tracking Corona", bg=BG_COLOR)
        self.lbl_mainpg.pack(side=tk.LEFT, padx=5)

        #Order button
        self.menuSuhuButton = tk.Button(master=self.navbar, text="Order", cursor="hand2", highlightthickness = 0, bd = 0)
        self.menuSuhuButton.configure(font=SMALL_FONT)
        self.menuSuhuButton.config(background=BG_COLOR)
        self.menuSuhuButton.pack(side=tk.RIGHT, padx=5)

        #Suhu button
        self.menuSuhuButton = tk.Button(master=self.navbar, text="Suhu", cursor="hand2", highlightthickness = 0, bd = 0)
        self.menuSuhuButton.configure(font=SMALL_FONT)
        self.menuSuhuButton.config(background=BG_COLOR)
        self.menuSuhuButton.pack(side=tk.RIGHT, padx=5)

        #Home button
        self.homeButton = tk.Button(master=self.navbar, text="Home", cursor="hand2", highlightthickness = 0, bd = 0, command=lambda : self.controller.show_frame("PenggunaHome"))
        self.homeButton.configure(font=SMALL_FONT)
        self.homeButton.config(background=BG_COLOR)
        self.homeButton.pack(side=tk.RIGHT, padx=5)

        self.controller.mycursor.execute("SELECT * FROM pesanan;")
        result = self.controller.mycursor.fetchall()
        i = 0

        for tup in result:
            i = i + 1

        for r in range(i+1):
            for c in range(5):
                e = tk.Entry(self,width=20, font=('Arial',12), fg="black")
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
                    elif (c == 4):
                        e.insert(tk.END,"Tanggal Pemesanan")
                    else:
                        e.insert(tk.END,"Status Konfirmasi")
                else:    
                    e.insert(tk.END,result[r-1][c])

class MenuBuatPesanan(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background = BG_COLOR)

        # Navbar Frame
        self.navbar = tk.Frame(self, width = 560, height = 25, relief = tk.GROOVE, borderwidth=1)
        self.navbar.place(x=0, y=0, height = 25, width = 560)
        self.navbar.configure(background=BG_COLOR)

        # #Profile button
        # self.menuSuhuButton = tk.Button(master=self.navbar, text="Profile", cursor="hand2", highlightthickness = 0, bd = 0)
        # self.menuSuhuButton.configure(font=SMALL_FONT)
        # self.menuSuhuButton.config(background=BG_COLOR)
        # self.menuSuhuButton.pack(side=tk.RIGHT, padx=5)

        # Label admin page
        self.lbl_mainpg = tk.Label(master=self.navbar, text="Sistem Tracking Corona", bg=BG_COLOR)
        self.lbl_mainpg.pack(side=tk.LEFT, padx=5)

        #Order button
        self.menuSuhuButton = tk.Button(master=self.navbar, text="Order", cursor="hand2", highlightthickness = 0, bd = 0)
        self.menuSuhuButton.configure(font=SMALL_FONT)
        self.menuSuhuButton.config(background=BG_COLOR)
        self.menuSuhuButton.pack(side=tk.RIGHT, padx=5)

        #Suhu button
        self.menuSuhuButton = tk.Button(master=self.navbar, text="Suhu", cursor="hand2", highlightthickness = 0, bd = 0)
        self.menuSuhuButton.configure(font=SMALL_FONT)
        self.menuSuhuButton.config(background=BG_COLOR)
        self.menuSuhuButton.pack(side=tk.RIGHT, padx=5)

        #Home button
        self.homeButton = tk.Button(master=self.navbar, text="Home", cursor="hand2", highlightthickness = 0, bd = 0, command=lambda : self.controller.show_frame("PenggunaHome"))
        self.homeButton.configure(font=SMALL_FONT)
        self.homeButton.config(background=BG_COLOR)
        self.homeButton.pack(side=tk.RIGHT, padx=5)

        self.title = tk.Label(self, text="BUAT PESANAN")
        self.title.config(font=TITLE_FONT)
        self.title.config(background=BG_COLOR)
        self.title.pack(pady=20)

        self.namaRSLabel = tk.Label(self, text="Masukkan nama RS\t\t:")
        self.namaRSLabel.config(font=LARGE_FONT)
        self.namaRSLabel.config(background=BG_COLOR)
        self.namaRSLabel.place(x=30, y=70)

        self.namaKamarLabel = tk.Label(self, text="Masukkan nama Kamar\t:")
        self.namaKamarLabel.config(font=LARGE_FONT)
        self.namaKamarLabel.config(background=BG_COLOR)
        self.namaKamarLabel.place(x=30, y=120)

        namaRS = tk.StringVar()  
        namaKamar = tk.StringVar()

        self.namaRSEntry = tk.Entry(self, textvariable=namaRS, width="30")
        self.namaRSEntry.place(x=320, y=70)
        self.namaKamarEntry = tk.Entry(self, textvariable=namaKamar, width="30")
        self.namaKamarEntry.place(x=320, y=120)

        self.tampilkanDataKamarButton = tk.Button(self,  text="Tampilkan Daftar Kamar", command=lambda:self.controller.show_frame("MenuTampilDataKamar"))
        self.tampilkanDataKamarButton.place(x=300, y=180, height=50, width=200)
        self.buatPesananButton = tk.Button(self,  text="Pesan", command=lambda:self.buatPesanan())
        self.buatPesananButton.place(x=300, y=240, height=50, width=200)

        self.surpriseLabel = tk.Label(self, text="Catatan: PERBESAR LAYAR KE KANAN UNTUK MELIHAT JUMLAH KAMAR \nYANG TERSEDIA SAAT MELIHAT TABEL KAMAR")
        self.surpriseLabel.config(font=("Calibri", 12, 'bold'))
        self.surpriseLabel.config(background=BG_COLOR)
        self.surpriseLabel.place(x=30, y=330)

    def buatPesanan(self):
        # Siapin value yang mau dimasukin
        kamar = self.namaKamarEntry.get()
        rs = self.namaRSEntry.get()
        IDKamar = getStringFromResult(getIDKamar(self.controller.mycursor,kamar,rs))
        newRandomID =  str(randomIDPesananGenerator(self.controller.mycursor))
        nowDate =  getNowDateAsString()
        user = self.controller.username # NANTI PAS DIBUAT MAIN PROGRAM, KASIH INI AKSES KE GLOBAL VARIABLE USERNAME BUAT TAU SIAPA YG LOGIN T_T
        
        # Cek apakah terjadi kesamaan id pesanan pada tabel dan yang baru di-generate
        if(not checkIfUserBooked(self.controller.mycursor, user)):
            isError = True
            while (isError):
                try:
                    insertQuery = "INSERT INTO pesanan VALUES (%s,%s,%s,%s,%s,%s);"
                    val = (newRandomID,getStringFromResult(IDKamar),user,"On Hold",nowDate,"Belum")
                    self.controller.mycursor.execute(insertQuery,val)
                    self.controller.dB.commit()
                    isError = False
                except mysql.connector.Error as e:
                    newRandomID = randomIDPesananGenerator(self.controller.mycursor)
                    isError = True
                    break
            self.loadKonfirmasiPesanan(IDKamar)
        else:
            mb.showwarning("Tidak Dapat Melakukan Pesanan", "Anda sudah melakukan pemesanan dan tidak dapat memesan kamar lagi sampai Admin mengonfirmasi pesanan Anda")
    def loadKonfirmasiPesanan(self, IDKamar):    
        searchQuery = "select harga from kamar where id=" + str(IDKamar) + ";"
        self.controller.mycursor.execute(searchQuery)
        result = self.controller.mycursor.fetchall()
        uang = "Rp" + getHarga(result[0]) + ",00"
        self.controller.frames["MenuKonfirmasiPesanan"].jumlahUangLabel.config(text=uang)
        self.controller.show_frame("MenuKonfirmasiPesanan")

class MenuKonfirmasiPesanan(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background = BG_COLOR)

        # Navbar Frame
        self.navbar = tk.Frame(self, width = 560, height = 25, relief = tk.GROOVE, borderwidth=1)
        self.navbar.place(x=0, y=0, height = 25, width = 560)
        self.navbar.configure(background=BG_COLOR)

        # #Profile button
        # self.menuSuhuButton = tk.Button(master=self.navbar, text="Profile", cursor="hand2", highlightthickness = 0, bd = 0)
        # self.menuSuhuButton.configure(font=SMALL_FONT)
        # self.menuSuhuButton.config(background=BG_COLOR)
        # self.menuSuhuButton.pack(side=tk.RIGHT, padx=5)

        # Label admin page
        self.lbl_mainpg = tk.Label(master=self.navbar, text="Sistem Tracking Corona", bg=BG_COLOR)
        self.lbl_mainpg.pack(side=tk.LEFT, padx=5)

        #Order button
        self.menuSuhuButton = tk.Button(master=self.navbar, text="Order", cursor="hand2", highlightthickness = 0, bd = 0)
        self.menuSuhuButton.configure(font=SMALL_FONT)
        self.menuSuhuButton.config(background=BG_COLOR)
        self.menuSuhuButton.pack(side=tk.RIGHT, padx=5)

        #Suhu button
        self.menuSuhuButton = tk.Button(master=self.navbar, text="Suhu", cursor="hand2", highlightthickness = 0, bd = 0)
        self.menuSuhuButton.configure(font=SMALL_FONT)
        self.menuSuhuButton.config(background=BG_COLOR)
        self.menuSuhuButton.pack(side=tk.RIGHT, padx=5)

        #Home button
        self.homeButton = tk.Button(master=self.navbar, text="Home", cursor="hand2", highlightthickness = 0, bd = 0, command=lambda : self.controller.show_frame("PenggunaHome"))
        self.homeButton.configure(font=SMALL_FONT)
        self.homeButton.config(background=BG_COLOR)
        self.homeButton.pack(side=tk.RIGHT, padx=5)

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

        self.konfirmasiLabel = tk.Label(self, text="Klik tombol di bawah jika telah melakukan transfer")
        self.konfirmasiLabel.config(font=LARGE_FONT)
        self.konfirmasiLabel.config(background=BG_COLOR)
        self.konfirmasiLabel.place(x=100, y=230)

        # user = tk.StringVar()
        # self.userEntry = tk.Entry(self, textvariable=user, width="30")
        # self.userEntry.place(x=260, y=255)

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

        # Navbar Frame
        self.navbar = tk.Frame(self, width = 560, height = 25, relief = tk.GROOVE, borderwidth=1)
        self.navbar.place(x=0, y=0, height = 25, width = 560)
        self.navbar.configure(background=BG_COLOR)

        # #Profile button
        # self.menuSuhuButton = tk.Button(master=self.navbar, text="Profile", cursor="hand2", highlightthickness = 0, bd = 0)
        # self.menuSuhuButton.configure(font=SMALL_FONT)
        # self.menuSuhuButton.config(background=BG_COLOR)
        # self.menuSuhuButton.pack(side=tk.RIGHT, padx=5)

        # Label admin page
        self.lbl_mainpg = tk.Label(master=self.navbar, text="Sistem Tracking Corona", bg=BG_COLOR)
        self.lbl_mainpg.pack(side=tk.LEFT, padx=5)

        #Order button
        self.menuSuhuButton = tk.Button(master=self.navbar, text="Order", cursor="hand2", highlightthickness = 0, bd = 0)
        self.menuSuhuButton.configure(font=SMALL_FONT)
        self.menuSuhuButton.config(background=BG_COLOR)
        self.menuSuhuButton.pack(side=tk.RIGHT, padx=5)

        #Suhu button
        self.menuSuhuButton = tk.Button(master=self.navbar, text="Suhu", cursor="hand2", highlightthickness = 0, bd = 0)
        self.menuSuhuButton.configure(font=SMALL_FONT)
        self.menuSuhuButton.config(background=BG_COLOR)
        self.menuSuhuButton.pack(side=tk.RIGHT, padx=5)

        #Home button
        self.homeButton = tk.Button(master=self.navbar, text="Home", cursor="hand2", highlightthickness = 0, bd = 0, command=lambda : self.controller.show_frame("PenggunaHome"))
        self.homeButton.configure(font=SMALL_FONT)
        self.homeButton.config(background=BG_COLOR)
        self.homeButton.pack(side=tk.RIGHT, padx=5)

        self.title = tk.Label(self,text="PROSES PESANAN USER")
        self.title.config(font=TITLE_FONT)
        self.title.config(background=BG_COLOR)
        self.title.pack(pady=20)

        IDPesanan = tk.StringVar()  
        statusBaru = tk.StringVar()

        self.IDPesananEntry = tk.Entry(self,textvariable=IDPesanan, width="30")
        self.IDPesananEntry.place(x=320, y=70)
        self.statusBaruEntry = ttk.Combobox(self,width=30,textvariable=statusBaru)
        self.statusBaruEntry['values'] = ('On Hold', 'Diterima', 'Ditolak')
        self.statusBaruEntry.place(x=320, y=120)

        self.testButton = tk.Button(self, text="test", command=lambda:self.prosesPesanan(self.IDPesananEntry.get(),self.statusBaruEntry.get()))
        self.testButton.place(x=300, y=220)

    def prosesPesanan(self,idPesanan,statusPesanan):
        
        # Menerima atau menolak pesanan oleh admin
        ID = idPesanan
        status = statusPesanan

        # Mengurangi jumlah kamar yang tersedia jika pesanan diterima
        if (status == 'Diterima'):
            queryKurangiKamar = "UPDATE kamar SET jumlah=jumlah-1 WHERE id IN (SELECT id_kamar FROM pesanan WHERE id_pesanan=" + str(ID) + ");"
            self.controller.mycursor.execute(queryKurangiKamar)
            self.controller.mycursor.dB.commit()
        # IDPesananPilihan = result[nomorPesanan-1][0]

        dummy = updateQuery(status,ID,self.controller.mycursor.dB,self.controller.mycursor)

        mb.showinfo('Berhasil!', 'Status Pesanan berhasil di-update!')

class MenuTampilDataKamar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background = BG_COLOR)

        # Navbar Frame
        self.navbar = tk.Frame(self, width = 560, height = 25, relief = tk.GROOVE, borderwidth=1)
    
        #Order button
        self.menuSuhuButton = tk.Button(master=self.navbar, text="Buat Pesanan", cursor="hand2", highlightthickness = 0, bd = 0, command=lambda:self.controller.show_frame("MenuBuatPesanan"))
        self.menuSuhuButton.configure(font=SMALL_FONT)
        self.menuSuhuButton.config(background=BG_COLOR)
        self.menuSuhuButton.pack(side=tk.LEFT, padx=5)

        self.navbar.grid(row=0,column=0)
        self.navbar.configure(background=BG_COLOR)

        # #Profile button
        # self.menuSuhuButton = tk.Button(master=self.navbar, text="Profile", cursor="hand2", highlightthickness = 0, bd = 0)
        # self.menuSuhuButton.configure(font=SMALL_FONT)
        # self.menuSuhuButton.config(background=BG_COLOR)
        # self.menuSuhuButton.pack(side=tk.RIGHT, padx=5)

        # # Label admin page
        # self.lbl_mainpg = tk.Label(master=self.navbar, text="Sistem Tracking Corona", bg=BG_COLOR)
        # self.lbl_mainpg.pack(side=tk.LEFT, padx=5)

        # #Suhu button
        # self.menuSuhuButton = tk.Button(master=self.navbar, text="Suhu", cursor="hand2", highlightthickness = 0, bd = 0)
        # self.menuSuhuButton.configure(font=SMALL_FONT)
        # self.menuSuhuButton.config(background=BG_COLOR)
        # self.menuSuhuButton.pack(side=tk.RIGHT, padx=5)

        # #Home button
        # self.homeButton = tk.Button(master=self.navbar, text="Home", cursor="hand2", highlightthickness = 0, bd = 0, command=lambda : self.controller.show_frame("PenggunaHome"))
        # self.homeButton.configure(font=SMALL_FONT)
        # self.homeButton.config(background=BG_COLOR)
        # self.homeButton.pack(side=tk.RIGHT, padx=5)

        self.controller.mycursor.execute("SELECT k.nama,rs.nama,rs.alamat,k.harga,k.jumlah FROM kamar as k, rumahsakit as rs WHERE k.id=rs.id;")
        result = self.controller.mycursor.fetchall()
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