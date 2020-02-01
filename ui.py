import tkinter as tk


window = tk.Tk()
window.title("Guess The Number")
window.geometry("300x250")

header_frame = tk.Frame(window)
header_frame.pack()
heading = tk.Label(header_frame, text="Guess The Number").pack()

window.mainloop()
