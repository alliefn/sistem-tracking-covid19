import mysql.connector
from autentikasi_login import login
from suhu_gui import *

#window
window = tk.Tk()
window.title("Covid-19")
window.geometry("800x800")
window.configure(background='#c8eed9')

#Frame
frame = tk.Frame(window)
frame.pack(side="top", expand=True, fill="both")
frame.config(background = '#c8eed9')

def clearFrame():
    # destroy all widgets from frame
    for widget in frame.winfo_children():
       widget.destroy()

dB = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="rahutami",
        database="virusTrack"
        )

mycursor = dB.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS virusTrack")
mycursor.execute("CREATE TABLE IF NOT EXISTS User (username VARCHAR(255) PRIMARY KEY, nama VARCHAR(255), surel VARCHAR(255), password VARCHAR(20), nomor_telepon VARCHAR(100), role VARCHAR(10))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Suhu (id_suhu INT(255) PRIMARY KEY AUTO_INCREMENT, username VARCHAR(255), tanggal_input date, value DOUBLE(3,1), FOREIGN KEY(username) references user(username))")
command = ""
# loggedIn = False

# while(command != "exit"):
#     if(not loggedIn):
#         loggedIn, username, role = login(mycursor, dB)
#         print(username, role)
#     else:
#         if(command == "suhu"):
#             uploadSuhu(username, mycursor, dB)
#         command = input()

clearFrame()
menuSuhu("rahutami", mycursor, dB, frame)
window.mainloop()