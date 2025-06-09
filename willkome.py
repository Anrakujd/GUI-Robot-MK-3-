#*********************************************************************
#******** PROGRAM SISTEM KENDALI ROBOT ARTICULATED TIPE MK-2 *********
#********             Dibuat Oleh : Djukarna                 *********
#********             Tanggal : 11 Maret 2025                *********
#********         Fakultas Keguruan & Pendidikan             *********
#********         Universitas Katolik Parahyangan            *********
#********               Bandung-Jawa Barat                   *********
#*********************************************************************

# Library yang digunakan:
import tkinter as tk
from tkinter import*
from tkinter.ttk import*
from time import sleep
import RPi.GPIO as GPIO
import os
import subprocess

frame = tk.Tk()
frame.geometry('800x400')
frame.title('Robot Mk2')

#Judul GUI
l1 = Label(frame, text = "Sistem Kendali Robot MK-2", font=("Verdana", 20) )
l1.grid(row = 0, column = 1, pady = 5, padx = 5)

l8 = Label(frame, text = "Pilih Interface Yang Akan Digunakan", font=("Verdana", 16) )
l8.grid(row = 3, column = 1, pady = 5, padx = 5)

#Logo UNPAR
img = PhotoImage(file = "logo_UNPAR.png")
img1 = img.subsample(2, 2)
Label(frame, image = img1).grid(row = 0, column = 0)

#open CLI
def run_program_CLI():
    subprocess.Popen([sys.executable, "sequential.py"])
    frame.quit()
    frame.destroy()

#open GUI
def run_program_GUI():
    subprocess.Popen([sys.executable, "GUI robot.py"])
    frame.quit()
    frame.destroy()

#Exit Button
def exitProgram():
    print("Keluar dari Program")
    frame.quit()
    frame.destroy()

#Menu bar
menubar = Menu(frame)
#menu file
file = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file) 
file.add_command(label ='Exit', command = exitProgram)
#menu option
option = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Option", menu = option)
option.add_command(label = "Squensial", command = run_program_CLI)
option.add_command(label = "Manual", command = run_program_GUI)
#menu help
help_ = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Help', menu = help_) 
help_.add_command(label ='Robot Mk-2 Spec', command = None) 
help_.add_command(label ='Demo', command = None)
help_.add_command(label ='Tutorial', command = None) 
help_.add_separator() 
help_.add_command(label ='About Tk', command = None) 

space3 = tk.Label(frame, text=" ", height=2, font=("Arial", 16))
space3.grid(row = 4, column = 0)
space4 = tk.Label(frame, text=" ", height=2, font=("Arial", 16))
space4.grid(row = 6, column = 0)
space5 = tk.Label(frame, text=" ", height=2, font=("Arial", 16))
space5.grid(row = 7, column = 0)


b_GUI = tk.Button(frame,
            text = "MANUAL",
            command=run_program_GUI,
            activebackground="blue", 
            activeforeground="white",
            anchor="center",
            bd=3,
            bg="lightgray",
            cursor="hand2",
            disabledforeground="gray",
            fg="black",
            font=("Arial", 14, "bold"),
            height=3,
            highlightbackground="black",
            highlightcolor="green",
            highlightthickness=2,
            justify="center",
            padx=10,
            pady=5,
            width=20,
            wraplength=130)
b_GUI.grid(row = 5, column = 1)

b_CLI = tk.Button(frame,
            text = "SEQUENSIAL",
            command=run_program_CLI,
            activebackground="blue", 
            activeforeground="white",
            anchor="center",
            bd=3,
            bg="lightgray",
            cursor="hand2",
            disabledforeground="gray",
            fg="black",
            font=("Arial", 14,"bold"),
            height=3,
            highlightbackground="black",
            highlightcolor="green",
            highlightthickness=2,
            justify="center",
            padx=10,
            pady=5,
            width=20,
            wraplength=130)
b_CLI.grid(row = 5, column = 2)


#CopyRight Statement
CopyR = tk.Label(frame, text="Copyright:Djukarna@2025", font=("Arial", 10))
CopyR.grid(row = 8, column = 2)





frame.config(menu = menubar)
frame.mainloop()  #muter-muter terus menerus hingga kiamat :D

