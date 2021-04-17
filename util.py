#Menghapus semua widget sebelum ngeload page lain
def clearFrame(frame):
    # destroy all widgets from frame
    for widget in frame.winfo_children():
        widget.destroy()