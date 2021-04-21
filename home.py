import tkinter as tk
import tkinter.messagebox as mb
from style import *
from suhu import *

class AdminHome(tk.Frame):

    def __init__(self, parent, controller):
        # BAGIAN TERATAS: Admin - Pilihan Menu
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background = BG_COLOR)

        # Navbar Frame
        self.navbar = tk.Frame(self, width = 560, height = 25, relief = tk.GROOVE, borderwidth=1)
        self.navbar.place(x=0, y=0, height = 25, width = 560)
        self.navbar.configure(background=BG_COLOR)

        # Label admin page
        self.lbl_mainpg = tk.Label(master=self.navbar, text="Admin - Sistem Tracking Corona", bg=BG_COLOR)
        self.lbl_mainpg.pack(side=tk.LEFT, padx=5)

        # Logout button
        # Button input data Covid-19
        self.btn_logout = tk.Button(master=self.navbar, text="Logout", cursor="hand2", highlightthickness = 0, bd = 0, command = lambda username = self.controller.username : self.logout(username)) # command: fungsi ke modul input data Covid
        self.btn_logout.configure(font=SMALL_FONT)
        self.btn_logout.configure(bg=BG_COLOR)
        self.btn_logout.pack(side=tk.RIGHT)

        # BAGIAN BAWAH: MENU
        # Frame menu
        self.frm_menu = tk.Frame(master=self, width = 560, height = 195, relief = tk.GROOVE, borderwidth=1)
        self.frm_menu.place(x=0,y=25, height = 195, width = 560)
        self.frm_menu.configure(background=BG_COLOR)

        # Label pilihan
        self.lbl_pil = tk.Label(master=self.frm_menu, text="Pilihan Menu Admin", bg=BG_COLOR)
        self.lbl_pil.configure(font=TITLE_FONT)
        self.lbl_pil.pack(side=tk.TOP)

        # Button input data Covid-19
        self.btn_inputcovid = tk.Button(master=self.frm_menu, text="Input data Covid-19") # command: fungsi ke modul input data Covid
        self.btn_inputcovid.configure(font=SMALL_FONT)
        self.btn_inputcovid.pack(pady=10)

        # Button input data RS
        self.btn_inputrs = tk.Button(master=self.frm_menu, text="Input data Rumah Sakit") # command: fungsi ke modul input data RS
        self.btn_inputrs.configure(font=SMALL_FONT)
        self.btn_inputrs.pack(pady=10)

        # Button verifikasi pesanan pengguna
        self.btn_verify = tk.Button(master=self.frm_menu, text="Verifikasi pesanan pengguna") # command: fungsi ke modul verifikasi
        self.btn_verify.configure(font=SMALL_FONT)
        self.btn_verify.pack(pady=10)

    def logout(self, username):
        ucapan = "Sampai jumpa, " + str(username) + "!"
        mb.showinfo("Informasi",ucapan)
        self.controller.show_frame("Login")

class PenggunaHome(tk.Frame):

    def __init__(self, parent, controller):
        # BAGIAN TERATAS: Admin - Pilihan Menu
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background = BG_COLOR)

        # Navbar Frame
        self.navbar = tk.Frame(self, width = 560, height = 25, relief = tk.GROOVE, borderwidth=1)
        self.navbar.place(x=0, y=0, height = 25, width = 560)
        self.navbar.configure(background=BG_COLOR)

        # Label admin page
        self.lbl_mainpg = tk.Label(master=self.navbar, text="Admin - Sistem Tracking Corona", bg=BG_COLOR)
        self.lbl_mainpg.pack(side=tk.LEFT, padx=5)

        # Logout button
        # Button input data Covid-19
        self.btn_logout = tk.Button(master=self.navbar, text="Logout", cursor="hand2", highlightthickness = 0, bd = 0, command = lambda username = self.controller.username : self.logout(username)) # command: fungsi ke modul input data Covid
        self.btn_logout.configure(font=SMALL_FONT)
        self.btn_logout.configure(bg=BG_COLOR)
        self.btn_logout.pack(side=tk.RIGHT)

        # BAGIAN BAWAH: MENU
        # Frame menu
        self.frm_menu = tk.Frame(master=self, width = 560, height = 195, relief = tk.GROOVE, borderwidth=1)
        self.frm_menu.place(x=0,y=25, height = 195, width = 560)
        self.frm_menu.configure(background=BG_COLOR)

        # Label pilihan
        self.lbl_pil = tk.Label(master=self.frm_menu, text="Pilihan Menu", bg=BG_COLOR)
        self.lbl_pil.configure(font=TITLE_FONT)
        self.lbl_pil.pack(side=tk.TOP)

        # Button Upload Suhu
        self.suhuButton = tk.Button(master=self.frm_menu, text="Upload Suhu Harian", cursor="hand2", command=lambda : self.controller.show_frame("MenuSuhu"))
        self.suhuButton.configure(font=SMALL_FONT)
        self.suhuButton.pack(pady=10)

        # Button input data RS
        self.btn_inputrs = tk.Button(master=self.frm_menu, text="Pesan Rumah Sakit", cursor="hand2")
        self.btn_inputrs.configure(font=SMALL_FONT)
        self.btn_inputrs.pack(pady=10)

        # Button verifikasi pesanan pengguna
        self.btn_verify = tk.Button(master=self.frm_menu, text="Lihat Data Harian Covid-19", state="disabled")
        self.btn_verify.configure(font=SMALL_FONT)
        self.btn_verify.pack(pady=10)

    def logout(self, username):
        ucapan = "Sampai jumpa, " + str(username) + "!"
        mb.showinfo("Informasi",ucapan)
        self.controller.show_frame("Login")