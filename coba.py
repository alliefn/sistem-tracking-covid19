import tkinter as tk

def printUser(userToBeInput):
    print(userToBeInput + " hello")

window2 = tk.Tk()
window2.title("Konfirmasi Pesanan")
window2.geometry("800x800")
window2.configure(background='#c8eed9')

user = tk.StringVar()
userEntry = tk.Entry(window2, textvariable=user, width="30")
userEntry.place(x=260, y=255)
userToBeInput = user.get()

konfirmasiButton = tk.Button(window2, text="Konfirmasi Pesanan", command= lambda: printUser(userToBeInput))
konfirmasiButton.place(x=320, y=290, height=50, width=150)

window2.mainloop()