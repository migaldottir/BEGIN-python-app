import tkinter as tk
from tkinter import filedialog, Text
import os
root = tk.Tk()
canvas = tk.Canvas(root, height=600, width=600, bg="#263D42")
canvas.pack()
frame = tk.Frame(root, bg="blue")
frame.place(relwidth=0.8, relheight=0.8)

root.mainloop()

