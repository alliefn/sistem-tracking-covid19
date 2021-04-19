# GUI Proses Pesanan khusus Admin
from pesanan import *
import tkinter as tk
import mysql.connector

# Establish connection to RS DB
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="rs_covid"
# )
# cursor_db = db.cursor()

window = tk.Tk()
window.title("Proses Pesanan")
window.geometry("800x800")
window.configure(background='#c8eed9')

title = tk.Label(text="PROSES PESANAN USER")
title.config(font=("Calibri", 20, 'bold'))
title.config(background='#c8eed9')
title.pack(pady=20)

testButton = tk.Button(window, text="test", command=prosesPesanan)
testButton.place(x=300, y=220)

window.mainloop()