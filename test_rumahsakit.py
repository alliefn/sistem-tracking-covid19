import mysql.connector
import rumahsakit


def test_addRumahSakit():
    dB = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="trackingCovid"
    )
    mycursor = dB.cursor()
    assert 0 == len(rumahsakit.addRumahSakitTest(
        "Rs Boromeus", "Dimanasaja", dB, mycursor))


def test_addKamar():
    dB = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="trackingCovid"
    )
    mycursor = dB.cursor()
    assert 0 == len(rumahsakit.addKamarTest(
        2, 1200000, 10, "anggrek", dB, mycursor))


def test_updateRumahSakit():
    dB = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="trackingCovid"
    )
    mycursor = dB.cursor()
    assert 0 == len(rumahsakit.updateRumahSakitTest(
        1, "Rs Boromeus", "Dimanasaja", dB, mycursor))


def test_addKamar():
    dB = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="trackingCovid"
    )
    mycursor = dB.cursor()
    assert 0 == len(rumahsakit.updateKamarTest(
        1, 1, 1200000, 10, "anggrek", dB, mycursor))
