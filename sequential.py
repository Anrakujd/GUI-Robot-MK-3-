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
from tkinter import messagebox
from tkinter import*
from tkinter.ttk import*
from time import sleep
#import RPi.GPIO as GPIO
import os
import subprocess


#************************** berikut ini sesuaikan dengan hardware (robot) ! ****************************
#Variabel dan Konstanta Robot:
PUL_base = 17    #Pulse base
DIR_base = 27    #Direction base
ENA_base = 22    #Enable base

PUL_IA = 18      #Pulse Inner Arm
DIR_IA = 23      #Direction Inner Arm
ENA_IA = 24      #Enable Inner Arm

PUL_OA = 5       #Pulse Outer Arm
DIR_OA = 6       #Direction Outer Arm
ENA_OA = 13      #Enable Outer Arm

jepit = 20       #Gripper jepit
lepas = 21       #Gripper lepas

durationFwd = 1000  #forward durasi ( harus dikalibasi ulang disesuaikan dengan reduksi roda gigi
durationBwd = 1000  #backward durasi ( harus dikalibasi ulang disesuaikan dengan reduksi roda gigi

delay = 0.00001      #delay microsecond berhubungan dengan kecepatan putar motorstepper
#sudut_base = tk.IntVar()

#*********************************************************************************************************

#Setting GPIO Raspberry Pi-3
GPIO.setmode(GPIO.BCM)
GPIO.setup(PUL_base, GPIO.OUT)
GPIO.setup(DIR_base, GPIO.LOW)
GPIO.setup(ENA_base, GPIO.LOW)

GPIO.setup(PUL_IA, GPIO.OUT)
GPIO.setup(DIR_IA, GPIO.LOW)
GPIO.setup(ENA_IA, GPIO.LOW)

GPIO.setup(PUL_OA, GPIO.OUT)
GPIO.setup(DIR_OA, GPIO.LOW)
GPIO.setup(ENA_OA, GPIO.LOW)

#konstruktor 
#root = tk.Tk()
#root.title("Sistem Kendali Robot Sequensial (DOF per DOF)")
#root.geometry("1000x650")
#root.title("Robot MK2")

root = tk.Tk()
root.title("Sistem Kendali Robot Sequensial (DOF per DOF)")
root.geometry("1000x650")
#root.title("Robot MK2")

entries = []
baris_ke = 0

frame = tk.Frame(root)
frame.pack(pady = 10)


#open CLI
def run_program_CLI():
    subprocess.Popen([sys.executable, "sequential.py"])
    root.quit()
    root.destroy()

#open GUI
def run_program_GUI():
    subprocess.Popen([sys.executable, "GUI robot.py"])
    root.quit()
    root.destroy()

#Exit Button
def exitProgram():
    print("Keluar dari Program")
    GPIO.cleanup()
    root.quit()
    root.destroy()

#Menu bar
menubar = Menu(root)
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


#fungsi menambah textbox
def hapus_textbox(index):
    for widget in entries[index]["widgets"]:
        widget.destroy()
    entries.index=None
        

def tambah_textbox():
    global baris_ke
    satu_baris =[]
    widgets = []

    for kolom_ke in range(4):
        entry = tk.Entry(frame, width = 15)
        entry.grid(row = baris_ke, column = kolom_ke, padx=5, pady=5)
        satu_baris.append(entry)
        widgets.append(entry)
        
    btn_hapus = tk.Button(frame, text="Hapus", command = lambda idx=baris_ke: hapus_textbox(idx))
    btn_hapus.grid(row=baris_ke, column = 4, padx = 5)

    widgets.append(btn_hapus)

    entries.append({"entries": satu_baris, "widgets": widgets})
    baris_ke += 1

def tampilkan_isi():
    #print("isi semua texbox:")
    for i, baris in enumerate(entries, start=1):
        if baris is not None:
            isi = [e.get() for e in baris["entries"]]
        print("Baris {}: {}".format(i, isi))

def Run():
    print("menjalakan Program")

tk.Button(root, text="Tambah Baris Program", command=tambah_textbox).pack(pady = 10)
tk.Button(root, text="Run Program", command=Run).pack(pady = 5)

root.config(menu = menubar)
root.mainloop()
        
