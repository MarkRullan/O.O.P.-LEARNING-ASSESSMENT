#O.E. #8
#Mark J. Rullan

import tkinter as TK

windows = TK.Tk()

name = "Mark J. Rullan"
windows.title(f"OOP OE#8 {name}")
windows.geometry("300x200")
windows.configure(bg="white")

pangalan = TK.Entry(windows)
pangalan.grid(row=0, column=0, padx=40)

counter = 0
def iPrint():
    global counter
    print(f"{counter}.{pangalan.get()}")
    counter +=1

frame = TK.Frame(windows)
frame.grid(pady=40)

button = TK.Button(windows, text="Print", command=iPrint)
button.grid(row=0, column=1, padx=40, pady=40)
windows.mainloop()