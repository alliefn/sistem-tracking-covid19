from buatPesanan import buatPesananTest as bPT
from prosesPesanan import *

def test_buatPesanan1():
    assert 0 != len(bPT("Rumah Sakit Tidak Meninggal","Dandelion","gray"))

def test_buatPesanan2():
    try:
        bPT("Rumah Sakit","Dandelion","gray")
        assert False
    except IndexError:
        assert True
    
# Pesanan diterima
def test_prosesPesanan1():
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dika090301", # placeholder
    database="trackingCovid"
    )
    cursor_db = db.cursor()

    assert "Diterima" == str(pP.updateQuery("Diterima",701,db,cursor_db))

# Pesanan on hold
def test_prosesPesanan2():
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dika090301", # placeholder
    database="trackingCovid"
    )
    cursor_db = db.cursor()

    assert "On Hold" == getStringFromResultTest(pP.updateQuery("On Hold",703,db,cursor_db))

# Pesanan ditolak
def test_prosesPesanan3():
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dika090301", # placeholder
    database="trackingCovid"
    )
    cursor_db = db.cursor()

    assert "Ditolak" == getStringFromResultTest(pP.updateQuery("Ditolak",702,db,cursor_db))