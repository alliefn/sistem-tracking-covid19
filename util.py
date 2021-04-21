import re
import random
import datetime
import tkinter as tk
from style import *

def createNavbarAdmin(frame):
    # Navbar Frame
    frame.navbar = tk.Frame(frame, width=560, height=25,
                            relief=tk.GROOVE, borderwidth=1)
    frame.navbar.place(x=0, y=0, height=25, width=560)
    frame.navbar.configure(background=BG_COLOR)
    
    # Label admin page
    frame.lbl_mainpg = tk.Label(
        master=frame.navbar, text="Admin - Sistem Tracking Corona", bg=BG_COLOR)
    frame.lbl_mainpg.pack(side=tk.LEFT, padx=5)

    # Input COvid Button
    frame.menuSuhuButton = tk.Button(
        master=frame.navbar, text="Input Covid", state="disabled", highlightthickness=0, bd=0)
    frame.menuSuhuButton.configure(font=SMALL_FONT)
    frame.menuSuhuButton.config(background=BG_COLOR)
    frame.menuSuhuButton.pack(side=tk.RIGHT, padx=5)

    # Input Kamar Button
    frame.menuInputKamar = tk.Button(master=frame.navbar, text="Input Kamar", cursor="hand2",
                                    highlightthickness=0, bd=0, command=lambda: frame.controller.show_frame("MenuInsertKamar"))
    frame.menuInputKamar.configure(font=SMALL_FONT)
    frame.menuInputKamar.config(background=BG_COLOR)
    frame.menuInputKamar.pack(side=tk.RIGHT, padx=5)

    # Input RS Button
    frame.menuInputRS = tk.Button(master=frame.navbar, text="Input RS", cursor="hand2",
                                    highlightthickness=0, bd=0, command=lambda: frame.controller.show_frame("MenuInsertRS"))
    frame.menuInputRS.configure(font=SMALL_FONT)
    frame.menuInputRS.config(background=BG_COLOR)
    frame.menuInputRS.pack(side=tk.RIGHT, padx=5)

    # Home button
    frame.homeButton = tk.Button(master=frame.navbar, text="Home", cursor="hand2",
                                highlightthickness=0, bd=0, command=lambda: frame.controller.show_frame("AdminHome"))
    frame.homeButton.configure(font=SMALL_FONT)
    frame.homeButton.config(background=BG_COLOR)
    frame.homeButton.pack(side=tk.RIGHT, padx=5)
def createNavbarPengguna(frame):
    # Navbar Frame
    frame.navbar = tk.Frame(frame, width = 560, height = 25, relief = tk.GROOVE, borderwidth=1)
    frame.navbar.place(x=0, y=0, height = 25, width = 560)
    frame.navbar.configure(background=BG_COLOR)

    # Label admin page
    frame.lbl_mainpg = tk.Label(master=frame.navbar, text="Sistem Tracking Corona", bg=BG_COLOR)
    frame.lbl_mainpg.pack(side=tk.LEFT, padx=5)

    #Order button
    frame.menuSuhuButton = tk.Button(master=frame.navbar, text="Order", cursor="hand2", highlightthickness = 0, bd = 0)
    frame.menuSuhuButton.configure(font=SMALL_FONT)
    frame.menuSuhuButton.config(background=BG_COLOR)
    frame.menuSuhuButton.pack(side=tk.RIGHT, padx=5)

    #Suhu button
    frame.menuSuhuButton = tk.Button(master=frame.navbar, text="Suhu", cursor="hand2", highlightthickness = 0, bd = 0)
    frame.menuSuhuButton.configure(font=SMALL_FONT)
    frame.menuSuhuButton.config(background=BG_COLOR)
    frame.menuSuhuButton.pack(side=tk.RIGHT, padx=5)

    #Home button
    frame.homeButton = tk.Button(master=frame.navbar, text="Home", cursor="hand2", highlightthickness = 0, bd = 0, command=lambda : frame.controller.show_frame("PenggunaHome"))
    frame.homeButton.configure(font=SMALL_FONT)
    frame.homeButton.config(background=BG_COLOR)
    frame.homeButton.pack(side=tk.RIGHT, padx=5)

def updateQuery(status,ID,db,cursor_db):
    query = "UPDATE pesanan SET status=\'" + status + "\' WHERE id_pesanan=" + str(ID) + ";"
    cursor_db.execute(query)
    db.commit()
    query = "SELECT status FROM pesanan " + "where id_pesanan=" + str(ID) + ";"
    cursor_db.execute(query)
    hasil = cursor_db.fetchone()
    return hasil[0]

# Mengecek suatu email valid atau tidak
def emailvalid(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if re.search(regex,email):
        return True
    else:
        return False

# Mengecek suatu phone number valid atau tidak,
# phone number harus berasal dari negara +62
def phonevalid(phonenumber):
    regex = '(?:\+62)?0?8\d{2}(\d{8})'
    if re.search(regex, phonenumber):
        return True
    else:
        return False

def getHome(role):
    if str(role).lower == "admin":
        return "AdminHome"
    else:
        return "PenggunaHome"

def getNowDateAsString():
    now = datetime.datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    dateFormat = year + "-" + month + "-" + day
    return dateFormat

def randomIDPesananGenerator(cursor_db):
    randomID = random.randint(700,(10**5)-1)
    # cursor_db.execute("select id_pesanan from pesanan;")
    # checkingResult = cursor_db.fetchall()
    # isDuplikat = False
    # while (not isDuplikat):
    #     for tup in checkingResult:
    #         if (tup == randomID):
    #             isDuplikat = True
    #             break
    #     if (isDuplikat):
    #         randomID = random.randint(700,(10**5)-1)
    #         isDuplikat = False
    return randomID

def getIDRS(cursor_db,namaRS):
    query = "select id from rumahsakit where nama=\'" + namaRS + "\';"
    cursor_db.execute(query)
    result = cursor_db.fetchall()
    return result[0]

def getIDKamar(cursor_db,namaKamar,namaRS):
    idRS = getStringFromResult(getIDRS(cursor_db,namaRS))
    query = "select id from kamar where nama=\'" + namaKamar + "\' and rumah_sakit_id=" + idRS + ";"
    cursor_db.execute(query)
    result = cursor_db.fetchall()
    return result[0]

def checkIfUserBooked(cursor_db,user):
    query = "select username from pesanan where username=\'" + user + "\' and status=\'On Hold\';"
    cursor_db.execute(query)
    result = cursor_db.fetchone()
    if (result == None):
        return False
    else:
        return True

def getStringFromResult(result):
    temp = str(result)
    newString = ""
    for i in temp:
        if (i != "(" and i != ")" and i != ","):
            newString = newString + i
    return newString

def getHarga(stringHarga):
    stringHarga = str(stringHarga)
    result = ""
    
    for c in stringHarga:
        if(c in "0123456789"):
            result += c
        elif(c == '.'):
            break

    return str(result)