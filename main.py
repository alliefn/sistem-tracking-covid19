import tkinter as tk
import mysql.connector 

# modules
from home import *
from style import *
from suhu import *
from autentikasi_login import *
from rumahsakit import *
from pesanan import *

class VirusTrack(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.dB = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="rahutami",
        database="trackingCovid"
        )

        self.mycursor = self.dB.cursor()

        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS virusTrack")
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS User (username VARCHAR(255) PRIMARY KEY, nama VARCHAR(255), surel VARCHAR(255), password VARCHAR(20), nomor_telepon VARCHAR(100), role VARCHAR(10))")
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS Suhu (id_suhu INT(255) PRIMARY KEY AUTO_INCREMENT, username VARCHAR(255), tanggal_input date, value DOUBLE(3,1), FOREIGN KEY(username) references user(username))")
        command = ""
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.title("Covid-19")
        self.geometry(WINDOW_SIZE)
        self.configure(background=BG_COLOR)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.loggedIn = False
        self.username = ""
        self.role = ""
        self.frames = {}

        for F in (Login, SignUp, AdminHome, PenggunaHome, MenuSuhu, MenuInsertRS, MenuInsertKamar, MenuUpdateKamar, MenuTampilPesanan, MenuBuatPesanan, MenuProsesPesanan,  MenuKonfirmasiPesanan, MenuTampilDataKamar, MenuTampilDataRS, MenuUpdateRS):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
    
        self.show_frame("Login")

    def show_frame(self, page_name):
        # '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def getHome(self):
        if(self.username == "admin"):
            return "AdminHome"
        else:
            return "PenggunaHome"

app = VirusTrack()
app.mainloop()