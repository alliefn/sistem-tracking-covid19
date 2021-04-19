from suhu_gui import *
import tkinter as tk
import pytest

def test_info():
    window = tk.Tk()
    window.title("Covid-19")
    window.geometry("800x800")
    window.configure(background='#c8eed9')
    suhuEntry = tk.Entry(window, width="30")
    suhuEntry.place(x=270, y=95)
    suhuEntry.config(text = "33")
    menuSuhu.