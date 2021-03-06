from suhu import uploadSuhuTest
import tkinter as tk

def test_suhu1():
    info, hasil = uploadSuhuTest("gillian", "38.2", "2021-04-22")

    assert info == "Anda sedang mengalami demam" and len(hasil) > 0

def test_suhu2():
    info, hasil = uploadSuhuTest("ryann", "36.2", "2021-04-22")

    assert info == "Suhu tubuh Anda normal" and len(hasil) > 0

def test_suhu3():
    info, hasil = uploadSuhuTest("russell", "33.2", "2021-04-22")

    assert info == "Anda sedang mengalami hypothermia" and len(hasil) > 0

def test_suhu4():
    info, hasil = uploadSuhuTest("elena", "41.2", "2021-04-22")

    assert info == "Anda sedang mengalami hyperpyrexia" and len(hasil) > 0

def test_suhu5():
    info, hasil = uploadSuhuTest("aretha", "ss", "2021-04-22")

    assert info == "Input Anda tidak valid" and len(hasil) == 0
