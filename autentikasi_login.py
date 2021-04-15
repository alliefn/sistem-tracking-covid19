import mysql.connector

dN = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=""
        )
mycursor = dN.cursor()

mycursor.execute("DROP DATABASE IF EXISTS virusTrack")
mycursor.execute("CREATE DATABASE virusTrack")

dB = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="virusTrack"
        )

mycursor = dB.cursor()

mycursor.execute("CREATE TABLE User (username VARCHAR(255) PRIMARY KEY, nama VARCHAR(255), surel VARCHAR(255), password VARCHAR(20), nomor_telepon VARCHAR(100), role VARCHAR(10))")

# PROGRAM UTAMA
pilihan = ""
login = False
while (pilihan != "exit" and not login):
    print("Selamat datang di aplikasi Sistem Tracking Corona!\n")
    print("Pilih 1 untuk sign in")
    print("Pilih 2 untuk sign up")
    print("> ",end='')

    pilihan = input()

    if (pilihan == '1'):
        print("\nMasukkan username Anda: ",end='')
        uname = input()
        print("Masukkan password Anda: ",end='')
        passw = input()
        sql = "SELECT username, password FROM User WHERE username = '" + uname + "' and " + "password = '" + passw + "'"
        mycursor.execute(sql)
        hasil = mycursor.fetchall()

        # Cek ada hasil atau nggak
        if (len(hasil) == 0):
            print("Tidak ada yang memenuhi\n")
        else:
            print(len(hasil))
            for line in hasil:
                for ch in line:
                    if (ch != '(' and ch != "'"):
                        print(ch)
            login = True
    elif (pilihan == '2'):
        print("Masukkan username Anda: ",end='')
        uname = input()
        print("Masukkan nama Anda: ",end='')
        name = input()
        print("Masukkan password Anda: ",end='')
        passw = input()
        print("Masukkan email Anda: ",end='')
        surel = input()
        print("Masukkan nomor telepon Anda: ",end='')
        noTel = input()
        sql = "SELECT username FROM User WHERE username = '" + uname + "'"
        mycursor.execute(sql)
        hasil = mycursor.fetchall()
        if (len(hasil) > 0):
            print("Username sudah digunakan!\n")
        else:
            mycursor.execute("INSERT INTO User VALUES (%s, %s, %s, %s, %s, %s)", (uname, name, passw, surel, noTel, "Pengguna"))
            dB.commit()
            print("Selamat datang,", uname)
            print()
            login = True
    elif (pilihan == "exit"):
        print("Sampai jumpa ya!")
    else:
        print("Perintah salah!\n")
