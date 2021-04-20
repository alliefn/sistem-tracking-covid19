import mysql.connector
import random
import datetime
import tkinter as tk

# BACA CATATAN DI FUNGSI masukanPesanan()

# Establish connection to RS DB
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dika090301",
    database="trackingCovid"
)
cursor_db = db.cursor()

# 1. Tampilkan data kamar dan pilih kamar. Return tuple berisi detail kamar yang udah diupdate
# Dependencies: cursor_db = cursor db yang diload
# def dataKamar():
#     # Menampilkan data kamar
#     # cursor_db.execute("SELECT * FROM kamar;")
#     # result = cursor_db.fetchall()
#     # print("No \t ID Kamar \t\t Nama RS \t\t Harga \t\t Jumlah")
#     # i = 0
#     # for tup in result:
#     #     i = i + 1
#     #     namaRS = getNamaRS(tup[1], cursor_db) # tup[1] itu ID rumah sakit yg jadi foreign key di relasi kamar
#     #     print(i+" \t "+tup[0]+" \t\t "+namaRS+" \t\t "+tup[2]+" \t\t "+tup[3])
    
#     # Membuat pesanan kamar
#     kamarPilihan = int(input("Masukkan No kamar yang ingin dipesan (kolom paling kiri): "))
#     while (result[kamarPilihan-1][3] == 0): # Mengecek jika kamar yang dipilih tidak tersedia (jumlah = 0)
#         print("Kamar tidak tersedia. Silakan pilih kamar lain")
#         kamarPilihan = int(input("Masukkan No kamar yang ingin dipesan (kolom paling kiri): "))
    
#     # Update database
#     jumlahKamarPilihanSekarang = result[kamarPilihan-1][3] - 1
#     idKamarPilihan = result[kamarPilihan-1][0]
#     query = "UPDATE kamar SET jumlah=" + jumlahKamarPilihanSekarang + " WHERE id=" + idKamarPilihan + ";"
#     cursor_db.execute(query)

#     return result[kamarPilihan-1]

# 2. Memasukkan data kamar yang dipesan ke tabel pesanan
# Dependencies: cursor_db = cursor db yang diload
#               username = username pengguna yang login saat itu
# def masukanPesanan(username):
#     kamarPesanan = dataKamar()
#     newID = random.randint(10**9,(10**10)-1)
#     IDKamar = kamarPesanan[0]
#     nowDate = getNowDateAsString()
#     status = "On Hold"
#     query = "INSERT INTO pesanan VALUES (" + newID + "," + IDKamar + "," + username + "," + nowDate + "," + status + ");"# Asumsi udah sesuai sama urutan di tabel
#     cursor_db.execute(query)
# Catatan   : Ada perubahan dari desain model relasional awal soalnya kamar mana
#             yg dipesan ga dicatet di tabel pesanan. Jadi, disitu gua tambahin
#             ID kamar yang dipesan.  

# 3. Proses pesanan yang masuk oleh admin. Ga Return nilai apa-apa
# def prosesPesanan():
#     # Menampilkan data pesanan
#     cursor_db.execute("SELECT * FROM pesanan;")
#     result = cursor_db.fetchall()
#     print("No \t ID Pesanan \t\t ID Kamar \t\t Username \t\t Tanggal Pesan \t\t Status")
#     i = 0
#     for tup in result:
#         i = i + 1
#     #     print(i+" \t "+tup[0]+" \t\t "+tup[1]+" \t\t "+tup[2]+" \t\t "+tup[3]+" \t\t "+tup[4])

    
#     # Menerima atau menolak pesanan oleh admin
#     isProsesLagi = True
#     while (isProsesLagi):
#         nomorPesanan = int(input("Masukkan No pesanan yang ingin diproses (kolom paling kiri): "))
#         statusBaru = input("Masukkan status baru untuk pesanan yang dipilih (Diterima/Ditolak): ")
#         while (statusBaru != "Diterima" or statusBaru != "Ditolak"):
#             print("Masukkan salah. Silakan coba lagi")
#             statusBaru = input("Masukkan status baru untuk pesanan yang dipilih (Diterima/Ditolak): ")
#         IDPesananPilihan = result[nomorPesanan-1][0]
#         # query = "UPDATE pesanan SET status=" + statusBaru + " WHERE id=" + IDPesananPilihan + ";"
#         # cursor_db.execute(query)
#         print("Pesanan berhasil di-update!")
#         prosesLagi = input("Apakah Anda ingin melakukan pemrosesan pesanan lagi? (y/n): ")
#         if (prosesLagi == "n" or prosesLagi == "N"):
#             isProsesLagi = False

# Fungsi getNamaRS. Return nama RS dalam bentuk string
# Dependencies: idRS = id dari RS yang mau dicari namanya
#               cursor_db = cursor dari db yang diload     
# def getNamaRS(idRS, cursor_db):
#     query = "SELECT nama FROM rs WHERE id=" + idRS + ";"
#     cursor_db.execute(query)
#     result = cursor_db.fetchall()
#     return result[0]

# Fungsi getNowDateAsString. Return tanggal saat ini dalam bentuk string
# def getNowDateAsString():
#     now = datetime.datetime.now()
#     year = now.strftime("%Y")
#     month = now.strftime("%m")
#     day = now.strftime("%d")
#     dateFormat = year + "-" + month + "-" + day
#     return dateFormat