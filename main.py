import mysql.connector
from autentikasi_login import login
from suhu import uploadSuhu

dN = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="rahutami"
        )
mycursor = dN.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS virusTrack")

dB = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="rahutami",
        database="virusTrack"
        )

mycursor = dB.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS User (username VARCHAR(255) PRIMARY KEY, nama VARCHAR(255), surel VARCHAR(255), password VARCHAR(20), nomor_telepon VARCHAR(100), role VARCHAR(10))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Suhu (id_suhu INT(255) PRIMARY KEY AUTO_INCREMENT, username VARCHAR(255), tanggal_input date, value DOUBLE(3,1), FOREIGN KEY(username) references user(username))")
command = ""
loggedIn = False

while(command != "exit"):
    if(not loggedIn):
        loggedIn, username, role = login(mycursor, dB)
        print(username, role)
    else:
        if(command == "suhu"):
            uploadSuhu(username, mycursor, dB)
        command = input()

print("Sampai jumpa ya!")