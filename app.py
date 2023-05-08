import tkinter as tk 
from tkinter import filedialog, Text
import os 

# import PyPDF2
from PIL import Image, ImageTk

print('is this working?')

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=700, bg='#263d42')
canvas.grid(columnspan=3)
canvas.pack()

frame = tk.Frame(root, bg='#3e646c')
frame.place(relwidth=0.8, relheight=0.8, rely=0.1, relx=0.1 )

#banklogo
logo = Image.open('banklogo.png')
logo = ImageTk.PhotoImage(banklogo)
logo_label = tk.Label(image=logo)
logo_label.image = banklogo
logo_label.grid(column=1, row=0)

root.mainloop()