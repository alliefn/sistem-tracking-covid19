import mysql.connector

# Jadi fungsi login ini bakal me-set 3 variabel
# Username, login, sama status_pengguna
# Username biar tahu itu siapa yang lagi pake
# status_pengguna dia siapa
# Login buat bisa akses segala fitur (Karena udah login)

import mysql.connector

def login(mycursor, dB):
    print("Selamat datang di aplikasi Sistem Tracking Corona!\n")
    print("Pilih 1 untuk sign in")
    print("Pilih 2 untuk sign up")
    print("> ",end='')

    pilihan = input()

    login = False
    hasil = []

    if (pilihan == '1'):
        print("\nMasukkan username Anda: ",end='')
        uname = input()
        print("Masukkan password Anda: ",end='')
        passw = input()
        sql = "SELECT username, role FROM User WHERE username = '" + uname + "' and " + "password = '" + passw + "'"
        mycursor.execute(sql)
        hasil = mycursor.fetchall()

        # Cek ada hasil atau nggak
        if (len(hasil) == 0):
            print("Tidak ada yang memenuhi\n")
        else:
            print("Selamat datang,", uname)
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
            mycursor.execute("INSERT INTO User(username, nama, password, surel, nomor_telepon, role) VALUES (%s, %s, %s, %s, %s, %s)", (uname, name, passw, surel, noTel, "Pengguna"))
            dB.commit()
            print("Selamat datang,", uname)
            print()
            login = True
            sql = "SELECT username, password FROM User WHERE username = '" + uname + "' and " + "password = '" + passw + "'"
            mycursor.execute(sql)
            hasil = mycursor.fetchall()
    else:
        print("Perintah salah!\n")

    return (login, hasil[0][0], hasil[0][1])
# Keperluan debugging
# login()
