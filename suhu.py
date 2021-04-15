from datetime import datetime
def uploadSuhu(username, mycursor, dB):
    print("Masukkan suhu badan= ", end = "")
    value = float(input())
    date = datetime.date(datetime.now())
    mycursor.execute("INSERT INTO suhu(username, value, tanggal_input) value(%s,%s,%s)", (username, value, date))
    dB.commit()
    if(value < 35):
        print("Anda sedang mengalami hypothermia")
    elif(value < 37.5):
        print("Suhu tubuh Anda normal")
    elif(value < 40):
        print("Anda sedang mengalami demam")
    else:
        print("Anda sedang mengalami hyperpyrexia")
