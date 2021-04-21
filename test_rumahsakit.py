import mysql.connector
import rsgui


def test_addRumahSakit():
    dB = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="trackingCovid"
    )
    mycursor = dB.cursor()
    assert 0 == len(rsgui.addRumahSakitTest(
        "Rs Boromeus", "Dimanasaja", dB, mycursor))


def test_addKamar():
    dB = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="trackingCovid"
    )
    mycursor = dB.cursor()
    assert 0 == len(rsgui.addKamarTest(
        2, 1200000, 10, "anggrek", dB, mycursor))


def test_updateRumahSakit():
    dB = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="trackingCovid"
    )
    mycursor = dB.cursor()
    assert 0 == len(rsgui.updateRumahSakitTest(
        1, "Rs Boromeus", "Dimanasaja", dB, mycursor))


def test_addKamar():
    dB = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="trackingCovid"
    )
    mycursor = dB.cursor()
    assert 0 == len(rsgui.updateKamarTest(
        1, 1, 1200000, 10, "anggrek", dB, mycursor))
