import mysql.connector
import autentikasi_login as al

def test_checkmail1():
    assert al.emailvalid("qwerty") == False

def test_checkmail2():
    assert al.emailvalid("alif@informatika.org") == True

def test_checkphone1():
    assert al.phonevalid("081989768976") == True

def test_checkphone2():
    assert al.phonevalid("+19i86544") == False

def test_checkphone3():
    assert al.phonevalid("+6281919191919") == True

def test_checksignin1():
    dB = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="trackingCovid"
            )
    mycursor = dB.cursor()
    assert 0 != len(al.verify_credential_signin("aretha","aretha123",dB,mycursor))

def test_checksignin2():
    dB = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="trackingCovid"
            )
    mycursor = dB.cursor()
    assert 0 == len(al.verify_credential_signin("alif","erfededf",dB,mycursor))

def test_checksignup1():
    dB = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="trackingCovid"
            )
    mycursor = dB.cursor()
    assert 0 == len(al.verify_credential_signup("churchil",dB,mycursor))

def test_checksignup2():
    dB = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="trackingCovid"
            )
    mycursor = dB.cursor()
    assert 0 != len(al.verify_credential_signup("admin1",dB,mycursor))