from style import *
import tkinter as tk
from datetime import datetime
import mysql.connector
from util import createNavbarPengguna

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

        createNavbarPengguna(self)

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
            username = self.controller.username
            val = float(self.suhuEntry.get())
            date = datetime.date(datetime.now())
            self.controller.mycursor.execute("DELETE FROM suhu where username = %s and tanggal_input = %s", (username, date))
            self.controller.mycursor.execute("INSERT INTO suhu(username, value, tanggal_input) value(%s,%s,%s)", (username, val, date))
            self.controller.dB.commit()
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

def uploadSuhuTest(username, val, date):
    dB = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="trackingCovid"
    )

    mycursor = dB.cursor()
    
    if(isfloat(val)):
        val = float(val)
        mycursor.execute("DELETE FROM suhu where username = %s and tanggal_input = %s", (username, date))
        mycursor.execute("INSERT INTO suhu(username, value, tanggal_input) value(%s,%s,%s)", (username, val, date))
        dB.commit()
        if(val < 35):
            info = "Anda sedang mengalami hypothermia"
        elif(val < 37.5):
            info = "Suhu tubuh Anda normal"
        elif(val < 40):
            info = "Anda sedang mengalami demam"
        else:
            info = "Anda sedang mengalami hyperpyrexia"
    
    else:
        info = "Input Anda tidak valid"

    mycursor.execute("select * from suhu where username = %s and tanggal_input = %s and value = %s", (username, date, val))
    hasil = mycursor.fetchall()
    return info, hasil
