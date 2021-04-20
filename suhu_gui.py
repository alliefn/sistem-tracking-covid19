from style import *
import tkinter as tk
from datetime import datetime

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

class MenuSuhu(tk.Frame):

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
        self.homeButton = tk.Button(master=self.navbar, text="Home", cursor="hand2", highlightthickness = 0, bd = 0), command=lambda : self.controller.show_frame("PenggunaHome")
        self.homeButton.configure(font=SMALL_FONT)
        self.homeButton.config(background=BG_COLOR)
        self.homeButton.pack(side=tk.RIGHT, padx=5)

        # Title
        self.title = tk.Label(self, text="INPUT SUHU HARIAN")
        self.title.config(font=TITLE_FONT)
        self.title.config(background=BG_COLOR)
        self.title.pack(pady=40)

        # Form
        self.suhuLabel = tk.Label(self, text="Masukkan suhu tubuh Anda hari ini")
        self.suhuLabel.config(font=LARGE_FONT)
        self.suhuLabel.config(background=BG_COLOR)
        self.suhuLabel.pack(pady=20)

        # Entry
        self.suhuEntry = tk.Entry(self, width="30")
        self.suhuEntry.pack(pady=20)

        #Info
        self.info = tk.Label(self, text = "")
        self.info.config(font=LARGE_FONT)
        self.info.config(background=BG_COLOR)
        self.info.pack(pady=20)   

        # Button
        self.insertSuhuButton = tk.Button(self, cursor="hand2", text = "Masukkan suhu", command= self.uploadSuhu)
        self.insertSuhuButton.pack(pady=20)

    def uploadSuhu(self, *args):
        if(isfloat(self.suhuEntry.get())):
            val = float(self.suhuEntry.get())
            date = datetime.date(datetime.now())
            # controller.mycursor.execute("INSERT INTO suhu(username, value, tanggal_input) value(%s,%s,%s)", (controller.username, value, date))
            # controller.dB.commit()
            if(val < 35):
                self.info.config(text = "Anda sedang mengalami hypothermia")
                self.info.config(fg=WARNING_COLOR)
            elif(val < 37.5):
                self.info.config(text = "Suhu tubuh Anda normal")
                self.info.config(fg="black")
            elif(val < 40):
                self.info.config(text = "Anda sedang mengalami demam")
                self.info.config(fg=WARNING_COLOR)
            else:
                self.info.config(text = "Anda sedang mengalami hyperpyrexia")
                self.info.config(fg=WARNING_COLOR)
        
        else:
            self.info.config(text = "Input Anda tidak valid")
            self.info.config(fg=WARNING_COLOR)