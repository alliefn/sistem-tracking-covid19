import tkinter as tk
from datetime import datetime

def menuSuhu(username, mycursor, dB, frame):
    # window = tk.Tk()
    # window.title("Covid-19")
    # window.geometry("800x800")
    # window.configure(background='#c8eed9')

    # #Frame
    # frame = tk.Frame(window)
    # frame.pack(side="top", expand=True, fill="both")
    # frame.config(background = '#c8eed9')

    # Title
    title = tk.Label(frame, text="INPUT SUHU HARIAN")
    title.config(font=("Calibri", 20, 'bold'))
    title.config(background='#c8eed9')
    title.pack(pady=20)

    # Form
    suhuLabel = tk.Label(frame, text="Suhu tubuh Anda hari ini")
    suhuLabel.config(font=("Calibri", 16, 'bold'))
    suhuLabel.config(background='#c8eed9')
    suhuLabel.place(x=30, y=70)

    colon1Label = tk.Label(frame, text=":")
    colon1Label.config(font=("Calibri", 16, 'bold'))
    colon1Label.config(background='#c8eed9')
    colon1Label.place(x=250, y=70)

    suhuEntry = tk.Entry(frame, width="30")
    suhuEntry.place(x=270, y=75)

    #Info
    info = tk.Label(frame, text = "")
    info.config(font=("Calibri", 16, 'bold'))
    info.config(background='#c8eed9')
    info.place(x=30, y=180)   

    def uploadSuhu(username, mycursor, dB):
        val = float(suhuEntry.get())
        date = datetime.date(datetime.now())
        # mycursor.execute("INSERT INTO suhu(username, value, tanggal_input) value(%s,%s,%s)", (username, value, date))
        dB.commit()
        if(val < 35):
            info.config(text = "Anda sedang mengalami hypothermia")
        elif(val < 37.5):
            info.config(text = "Suhu tubuh Anda normal")
        elif(val < 40):
            info.config(text = "Anda sedang mengalami demam")
        else:
            info.config(text = "Anda sedang mengalami hyperpyrexia")

    # Button
    insertSuhuButton = tk.Button(frame, text = "Masukkan suhu", command=lambda uname = username, cursor = mycursor, mydB = dB : uploadSuhu(uname, cursor, mydB))
    insertSuhuButton.place(x=300, y=120)
