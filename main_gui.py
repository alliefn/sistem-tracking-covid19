import mysql.connector
from autentikasi_login import login
from suhu_gui import *

#SETUP GUI
#window
window = tk.Tk()
window.title("Covid-19")
window.geometry("800x800")
window.configure(background='#c8eed9')

#Frame
frame = tk.Frame(window)
frame.pack(side="top", expand=True, fill="both")
frame.config(background = '#c8eed9')

#Menghapus semua widget sebelum ngeload page lain
def clearFrame():
    # destroy all widgets from frame
    for widget in frame.winfo_children():
       widget.destroy()

def loadAdminHome(username, mycursor, dB, frame):
    #Title
    title = tk.Label(frame, text="SISTEM TRACKING CORONA")
    title.config(font=("Calibri", 20, 'bold'))
    title.config(background='#c8eed9')
    title.pack(pady=20)

    #Tombol verif pesanan
    verifPesanan = tk.Button(frame, text = "Verifikasi Pesanan", width="30", command=lambda uname = username, cursor = mycursor, mydB = dB : uploadSuhu(uname, cursor, mydB))
    verifPesanan.pack(pady=10)

    #Tombol upload data rs
    updateRS = tk.Button(frame, text = "Update Data RS", width="30", command=lambda uname = username, cursor = mycursor, mydB = dB : uploadSuhu(uname, cursor, mydB))
    updateRS.pack(pady=10)

def loadPenggunaHome(username, mycursor, dB, frame):
    #Title
    title = tk.Label(frame, text="INPUT SUHU HARIAN")
    title.config(font=("Calibri", 20, 'bold'))
    title.config(background='#c8eed9')
    title.pack(pady=20)

    #Tombol upload suhu harian
    uploadSuhu = tk.Button(frame, text = "Upload Suhu Harian", width="30", command=lambda uname = username, cursor = mycursor, mydB = dB : uploadSuhu(uname, cursor, mydB))
    uploadSuhu.pack(pady=10)
    
    #Tombol pesan rumah sakit
    pesanRS = tk.Button(frame, text = "Pesan Rumah Sakit", width="30", command=lambda uname = username, cursor = mycursor, mydB = dB : uploadSuhu(uname, cursor, mydB))
    pesanRS.pack(pady=10)

#SETUP DATABASE
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

loggedIn = False

loadAdminHome("rahutami", mycursor, dB, frame)
# while(command != "exit"):
#     if(not loggedIn):
#         loggedIn, username, role = login(mycursor, dB)
#         print(username, role)
#     else:
#         if(command == "suhu"):
#             uploadSuhu(username, mycursor, dB)
#         command = input()

window.mainloop()