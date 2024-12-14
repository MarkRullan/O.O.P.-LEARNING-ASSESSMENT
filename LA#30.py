#L.A. #30
#Mark J. Rullan

import tkinter as TK

windows = TK.Tk()
name = "Mark J. Rullan"
animeTitle ="Reincarnated as &th Prince"
windows.title(f"OOP LA#30 {name}")
windows.geometry("300x200")
windows.configure(bg="white")

counter = 0
def iPrint():
    global counter
    print(f"My favorite anime is {animeTitle}.")
    counter += 1

frame = TK.Frame(windows)
frame.pack(pady=20)

button = TK.Button(windows, text="Print", command=iPrint)
button.pack(pady=10)
windows.mainloop()