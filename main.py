import tkinter as tk  # why not from tkinter import? **
from home import AdminHome, PenggunaHome
from style import TITLE_FONT, BG_COLOR
from suhu import MenuSuhu
import mysql.connector
from loginclass import Login, SignUp

TITLE_FONT = ("Calibri", 16)
class VirusTrack(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.title("Covid-19")
        self.geometry("560x400")
        self.configure(background='#c8eed9')

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.loggedIn = False
        self.username = ""
        self.role = ""
        self.frames = {}

        for F in (Login, SignUp, AdminHome, PenggunaHome, MenuSuhu):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame 
            print(F.__name__)
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
    
        self.show_frame("Login")

        self.dB = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="rahutami",
        database="virusTrack"
        )

        self.mycursor = self.dB.cursor()

        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS virusTrack")
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS User (username VARCHAR(255) PRIMARY KEY, nama VARCHAR(255), surel VARCHAR(255), password VARCHAR(20), nomor_telepon VARCHAR(100), role VARCHAR(10))")
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS Suhu (id_suhu INT(255) PRIMARY KEY AUTO_INCREMENT, username VARCHAR(255), tanggal_input date, value DOUBLE(3,1), FOREIGN KEY(username) references user(username))")
        command = ""

    def show_frame(self, page_name):
        # '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

# class Login(tk.Frame):

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         self.configure(background = BG_COLOR)

#         label = tk.Label(self, text="Login",
#                          font=TITLE_FONT, background = BG_COLOR)
#         label.pack(side="top", fill="x", pady=10)

#         button1 = tk.Button(self, text="Login as Admin",
#                             command=lambda: controller.show_frame("AdminHome"))
#         button2 = tk.Button(self, text="Login as Pengguna",
#                             command=lambda: controller.show_frame("PenggunaHome"))
#         button1.pack()
#         button2.pack()

app = VirusTrack()
app.mainloop()