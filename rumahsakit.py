import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kytnsx88",
    database="rs_covid"
)

cursor = db.cursor()


def help():
    print("1 = Input data rumah sakit baru")
    print("2 = Input data kamar baru")
    print("3 = Semua data rumah sakit")
    print("4 = Semua data kamar")
    print("5 = Exit")
    print("6 = Help")


while(1):
    help()

    inputVal = int(input("Masukkan pilihan yang diinginkan: "))

    if(inputVal == 1):
        nama = input("Masukkan nama rumah sakit : ")
        alamat = input("Masukkan alamat rumah sakit : ")

        query = "INSERT INTO RUMAHSAKIT (nama, alamat) VALUES (%s, %s)"
        cursor.execute(query, (nama, alamat))
        db.commit()

        print(cursor.rowcount, "record inserted.")
    elif(inputVal == 2):
        idRumahSakit = int(input("Masukkan id rumah sakit : "))
        harga = float(input("Masukkan harga : "))

        query = "INSERT INTO KAMAR (rumah_sakit_id, harga) VALUES (%s, %s)"
        cursor.execute(query, (idRumahSakit, harga))
        db.commit()

        print(cursor.rowcount, "record inserted.")
    elif(inputVal == 3):
        cursor.execute("SELECT * FROM rumahsakit")
        result = cursor.fetchall()

        print()
        for rumah_sakit in result:
            print(rumah_sakit)
        print()
    elif(inputVal == 4):
        idRumahSakit = (int(input("Masukkan id rumah sakit : ")), )

        query = "SELECT * FROM kamar WHERE rumah_sakit_id = %s"
        cursor.execute(query, idRumahSakit)
        result = cursor.fetchall()

        print()
        for kamar in result:
            print(kamar)
        print()
    elif(inputVal == 5):
        print("Exit Application!")
        break
    elif(inputVal == 6):
        help()
    else:
        print("Command not found")
