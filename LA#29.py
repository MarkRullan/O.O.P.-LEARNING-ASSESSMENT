#L.A. #29
#Mark J. Rullan

import tkinter as TK

windows = TK.Tk()
name = "Mark J. Rullan"
section ="BSIT-2A"
windows.title(f"OOP LA#29 {name}")
windows.geometry("300x200")
windows.configure(bg="white")

frame = TK.Frame(windows)
frame.pack(pady=20)

label = TK.Label(frame, text=f"OOP LA#29 {name} {section}")
label.grid(row=0, column=0, padx=10, pady=10 )

windows.mainloop()