import tkinter as tk
from tkinter import filedialog, Text
import os
root = tk.Tk()
apps = []
def addApp():

    for widget in frame.winfo_children():
        widget.destroy()
        #widget is giving us access to everything attached to the frame
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="khaki")
        label.pack()
        #denifition of a loop

def runApps():
    for app in apps:
        os.startfile(app)
        #function that starts the apps

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()
frame = tk.Frame(root, bg="goldenrod")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
#main window styling

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="#263D42", command=addApp)
#OpenFile button definition

openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
#RunApps button definition
runApps.pack()

root.mainloop()

with open ('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')

        #creating a text file with paths that we've opened saved in it

