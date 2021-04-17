#Menghapus semua widget sebelum ngeload page lain
def clearFrame(frame):
    # destroy all widgets from frame
    if(len(frame.winfo_children()) > 0):
        for widget in frame.winfo_children():
            widget.destroy()