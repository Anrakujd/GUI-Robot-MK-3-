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
frame = tk.Tk()
frame.geometry("1000x650") #untuk window ukuran:  1000px x 600px
frame.title("Robot MK2")


#Judul GUI
l1 = Label(frame, text = "Sistem Kendali Robot MK-2", font=("Verdana", 20) )
l1.grid(row = 0, column = 1, pady = 5, padx = 5)

l8 = Label(frame, text = "Gerak Joint ke Joint", font=("Verdana", 16) )
l8.grid(row = 2, column = 1, pady = 5, padx = 5)

#Logo UNPAR
img = PhotoImage(file = "logo_UNPAR.png")
img1 = img.subsample(2, 2)
Label(frame, image = img1).grid(row = 0, column = 0)

#open SLI
def run_program_CLI():
    subprocess.Popen([sys.executable, "-m", "idlelib", "-e", "python", "CLI robot.py"])
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
    GPIO.cleanup()
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

#Posisi Home
def home():
    print("test gerak 2 dof")
    sudut = sudut_base.get() * 101
    sudut3 = sudut_OA.get() * 101

    GPIO.output(ENA_base, GPIO.HIGH)
    GPIO.output(ENA_OA, GPIO.HIGH)
    sleep(.5) 
    GPIO.output(DIR_base, GPIO.LOW)
    GPIO.output(DIR_OA, GPIO.HIGH)
    
    for x in range(sudut): 
        GPIO.output(PUL_base, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL_base, GPIO.LOW)
        sleep(delay)
    sleep(1)
    for y in range(sudut3): 
        GPIO.output(PUL_OA, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL_OA, GPIO.LOW)
        sleep(delay)
        
    GPIO.output(ENA_base, GPIO.HIGH)   
    GPIO.output(ENA_OA, GPIO.HIGH) 
    sleep(1) 
    return

#Home Control
l2 = Label(frame, text = "Posisi Home :", font=("Verdana", 16))
l2.grid(row = 2, column = 3)
b_home = tk.Button(frame,
            text = "Home",
            command=home,
            activebackground="blue", 
            activeforeground="white",
            anchor="center",
            bd=3,
            bg="lightgray",
            cursor="hand2",
            disabledforeground="gray",
            fg="black",
            font=("Arial", 12),
            height=2,
            highlightbackground="black",
            highlightcolor="green",
            highlightthickness=2,
            justify="center",
            padx=10,
            pady=5,
            width=10,
            wraplength=100)
b_home.grid(row = 2, column = 4)

#------------------------------ base Program -----------------------
def Base_CW():
    print("Base berputar searah jarum jam")
    sudut = sudut_base.get() * 101
    GPIO.output(ENA_base, GPIO.HIGH)
    sleep(.5) 
    GPIO.output(DIR_base, GPIO.HIGH)
    for x in range(sudut): 
        GPIO.output(PUL_base, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL_base, GPIO.LOW)
        sleep(delay)
    GPIO.output(ENA_base, GPIO.HIGH) 
    sleep(1) 
    return
  
def Base_CCW():
    print("Base berputar berlawanan jarum jam")
    sudut = sudut_base.get() * 101
    GPIO.output(ENA_base, GPIO.HIGH)
    sleep(.5) 
    GPIO.output(DIR_base, GPIO.LOW)
    
    for y in range(sudut): 
        GPIO.output(PUL_base, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL_base, GPIO.LOW)
        sleep(delay)
        
    GPIO.output(ENA_base, GPIO.HIGH) 
    sleep(1) 
    return

#inner arm-----------------------------------------------------------------
def IA_CW():
    print("IA berputar searah jarum jam")
    sudut1 = sudut_IA.get() * 101
    GPIO.output(ENA_IA, GPIO.HIGH)
    sleep(.5) 
    GPIO.output(DIR_IA, GPIO.HIGH)
    
    for x in range(sudut1): 
        GPIO.output(PUL_IA, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL_IA, GPIO.LOW)
        sleep(delay)
        
    GPIO.output(ENA_IA, GPIO.HIGH) 
    sleep(1) 
    return

def IA_CCW():
    print("IA berputar berlawanan jarum jam")
    print("IA berputar berlawanan jarum jam")
    sudut1 = sudut_IA.get() * 101
    GPIO.output(ENA_IA, GPIO.HIGH)
    sleep(.5) 
    GPIO.output(DIR_IA, GPIO.LOW)
    
    for y in range(sudut1): 
        GPIO.output(PUL_IA, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL_IA, GPIO.LOW)
        sleep(delay)
        
    GPIO.output(ENA_IA, GPIO.HIGH) 
    sleep(1) 
    return

#outer arm----------------------------------------------------------------
def OA_CW():
    print("IA berputar searah jarum jam")
    sudut3 = sudut_OA.get() * 101
    GPIO.output(ENA_OA, GPIO.HIGH)
    sleep(.5) 
    GPIO.output(DIR_OA, GPIO.HIGH)
    for x in range(sudut3): 
        GPIO.output(PUL_OA, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL_OA, GPIO.LOW)
        sleep(delay)
    GPIO.output(ENA_OA, GPIO.HIGH) 
    sleep(1) 
    return

def OA_CCW():
    print("OA berputar berlawanan jarum jam")
    sudut3 = sudut_OA.get() * 101
    GPIO.output(ENA_OA, GPIO.HIGH)
    sleep(.5) 
    GPIO.output(DIR_OA, GPIO.LOW)
    
    for y in range(sudut3): 
        GPIO.output(PUL_OA, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL_OA, GPIO.LOW)
        sleep(delay)
        
    GPIO.output(ENA_OA, GPIO.HIGH) 
    sleep(1) 
    return

#gripper--------------------------------------------------------------
def gripper_jepit():
    print("Jepit objek")

def gripper_lepas():
    print("Lepas objek")
    
l3 = tk.Label(frame, text = "Keluar :", font=("Verdana", 16))
l3.grid(row = 13, column = 3, sticky = "e")
b_exit = tk.Button(frame,
            text = "Keluar",
            command=exitProgram,
            activebackground="blue", 
            activeforeground="white",
            anchor="center",
            bd=3,
            bg="lightgray",
            cursor="hand2",
            disabledforeground="gray",
            fg="black",
            font=("Arial", 12),
            height=2,
            highlightbackground="black",
            highlightcolor="green",
            highlightthickness=2,
            justify="center",
            padx=10,
            pady=5,
            width=10,
            wraplength=100)
b_exit.grid(row = 13, column = 4)

#gerak putar per join
#Base
# 1 putaran = 200 pulse ----> jika ustep = 1 artinya 1 putaran butuh 200 pulse
# jika uStep =1600 artinya 1 putaran butuh 1600 pulse
# hasil kalibrasi di dapat 4544 pulse setara dengan 45 derajat pada base robot
# artinya 1 derajat = 101 pulse


sudut_base = tk.IntVar()
sudut_base.set(90)              #set nilai derajat
input_sudut_base = tk.Entry(frame,
                            textvariable = sudut_base,
                            font=('calibre', 12, 'bold'),
                            width = 8)
input_sudut_base.grid(row=5, column = 0)

l4 = tk.Label(frame, text = "Gerak Base Robot", font=("Arial", 14))
l4.grid(row = 3, column = 0)
label_sudut_base = tk.Label(frame, text = "Sudut Putar (deg):", font=("Arial", 12))
label_sudut_base.grid(row=4, column =0)

b_base_CW = tk.Button(frame,
            text = "SJJ",
            command=Base_CW,
            activebackground="blue", 
            activeforeground="white",
            anchor="center",
            bd=3,
            bg="lightgray",
            cursor="hand2",
            disabledforeground="gray",
            fg="black",
            font=("Arial", 12),
            height=2,
            highlightbackground="black",
            highlightcolor="green",
            highlightthickness=2,
            justify="center",
            padx=10,
            pady=5,
            width=8,
            wraplength=100)
b_base_CW.grid(row = 6, column = 0)

b_base_CCW = tk.Button(frame,
            text = "BJJ",
            command=Base_CCW,
            activebackground="blue", 
            activeforeground="white",
            anchor="center",
            bd=3,
            bg="lightgray",
            cursor="hand2",
            disabledforeground="gray",
            fg="black",
            font=("Arial", 12),
            height=2,
            highlightbackground="black",
            highlightcolor="green",
            highlightthickness=2,
            justify="center",
            padx=10,
            pady=5,
            width=8,
            wraplength=100)
b_base_CCW.grid(row = 7, column = 0)

#Inner Arm
sudut_IA = tk.IntVar()
sudut_IA.set(5)
input_sudut_IA = tk.Entry(frame,
                            textvariable = sudut_IA,
                            font=('calibre', 12, 'bold'),
                            width = 8)
input_sudut_IA.grid(row=5, column = 1)

l5 = tk.Label(frame, text = "Gerak Inner Arm", font=("Arial", 14))
l5.grid(row = 3, column = 1)
label_sudut_IA = tk.Label(frame, text = "Sudut Putar (deg):", font=("Arial", 12))
label_sudut_IA.grid(row=4, column =1)

b_inner_arm_CW = tk.Button(frame,
                text = "TURUN",
                command=IA_CW,
                activebackground="blue", 
                activeforeground="white",
                anchor="center",
                bd=3,
                bg="lightgray",
                cursor="hand2",
                disabledforeground="gray",
                fg="black",
                font=("Arial", 12),
                height=2,
                highlightbackground="black",
                highlightcolor="green",
                highlightthickness=2,
                justify="center",
                padx=10,
                pady=5,
                width=8,
                wraplength=100)
b_inner_arm_CW.grid(row = 6, column = 1)

b_inner_arm_CCW = tk.Button(frame,
                text = "NAIK",
                command=IA_CCW,
                activebackground="blue", 
                activeforeground="white",
                anchor="center",
                bd=3,
                bg="lightgray",
                cursor="hand2",
                disabledforeground="gray",
                fg="black",
                font=("Arial", 12),
                height=2,
                highlightbackground="black",
                highlightcolor="green",
                highlightthickness=2,
                justify="center",
                padx=10,
                pady=5,
                width=8,
                wraplength=100)
b_inner_arm_CCW.grid(row = 7, column = 1)

#Outer Arm
sudut_OA = tk.IntVar()
sudut_OA.set(5)
input_sudut_OA = tk.Entry(frame,
                            textvariable = sudut_OA,
                            font=('calibre', 12, 'bold'),
                            width = 8)
input_sudut_OA.grid(row=5, column = 2)
l6 = tk.Label(frame, text = "Gerak Outer Arm", font=("Arial", 14))
l6.grid(row = 3, column = 2)
label_sudut_OA = tk.Label(frame, text = "Sudut Putar (deg):", font=("Arial", 12))
label_sudut_OA.grid(row=4, column =2)

b_outer_arm_CW = tk.Button(frame,
                text = "NAIK",
                command=OA_CW,
                activebackground="blue", 
                activeforeground="white",
                anchor="center",
                bd=3,
                bg="lightgray",
                cursor="hand2",
                disabledforeground="gray",
                fg="black",
                font=("Arial", 12),
                height=2,
                highlightbackground="black",
                highlightcolor="green",
                highlightthickness=2,
                justify="center",
                padx=10,
                pady=5,
                width=8,
                wraplength=100)
b_outer_arm_CW.grid(row = 6, column = 2)

b_outer_arm_CCW = tk.Button(frame,
                text = "TURUN",
                command=OA_CCW,
                activebackground="blue", 
                activeforeground="white",
                anchor="center",
                bd=3,
                bg="lightgray",
                cursor="hand2",
                disabledforeground="gray",
                fg="black",
                font=("Arial", 12),
                height=2,
                highlightbackground="black",
                highlightcolor="green",
                highlightthickness=2,
                justify="center",
                padx=10,
                pady=5,
                width=8,
                wraplength=100)
b_outer_arm_CCW.grid(row = 7, column = 2)

# gripper
l7 = tk.Label(frame, text = "Gripper", font=("Arial", 14))
l7.grid(row = 5, column = 4)

b_gripper_open = tk.Button(frame,
                text = "Lepas",
                command=gripper_lepas,
                activebackground="blue", 
                activeforeground="white",
                anchor="center",
                bd=3,
                bg="lightgray",
                cursor="hand2",
                disabledforeground="gray",
                fg="black",
                font=("Arial", 12),
                height=2,
                highlightbackground="black",
                highlightcolor="green",
                highlightthickness=2,
                justify="center",
                padx=10,
                pady=5,
                width=8,
                wraplength=100)
b_gripper_open.grid(row = 6, column = 4)

b_gripper_close = tk.Button(frame,
                text = "Jepit",
                command=gripper_jepit,
                activebackground="blue", 
                activeforeground="white",
                anchor="center",
                bd=3,
                bg="lightgray",
                cursor="hand2",
                disabledforeground="gray",
                fg="black",
                font=("Arial", 12),
                height=2,
                highlightbackground="black",
                highlightcolor="green",
                highlightthickness=2,
                justify="center",
                padx=10,
                pady=5,
                width=8,
                wraplength=100)
b_gripper_close.grid(row = 7, column = 4)


#gerak cartesian (Inverse Kinematik)



#display koordinat end effector
l7 = tk.Label(frame, text = "Koord (X, Y, Z)", font=("Arial", 12, "bold"))
l7.grid(row = 9, column = 1, sticky='w')

X = tk.StringVar()
X.set("123")
Y = tk.StringVar()
Y.set("456")
Z = tk.StringVar()
Z.set("789")

labelX = tk.Label(frame, textvariable = X,
                         bg="lightblue",      
                         height=1,              
                         width=10,              
                         bd=3,                  
                         font=("Arial", 12, "bold"),   
                         fg="red",             
                         padx=2,               
                         pady=2,                
                         justify=tk.LEFT,    
                         relief=tk.SUNKEN,     
                         underline=0,           
                         wraplength=50,
                         anchor = "w"
                        )
labelX.grid(row = 10, column = 1, padx = 10, sticky='w')
labelX1=Label(frame, text="Posisi di sumbu X:", font=("Arial",12,"bold"))
labelX1.grid(row = 10, column = 0)

labelY = tk.Label(frame, textvariable = Y,
                         bg="lightblue",      
                         height=1,              
                         width=10,              
                         bd=3,                  
                         font=("Arial", 12, "bold"), 
                         fg="red",             
                         padx=2,               
                         pady=2,                
                         justify=tk.LEFT,    
                         relief=tk.SUNKEN,     
                         underline=0,           
                         wraplength=50,
                         anchor = "w"
                        )
labelY.grid(row = 11, column = 1, padx = 10, sticky='w')
labelY1=Label(frame, text="Posisi di sumbu Y:", font=("Arial",12,"bold"))
labelY1.grid(row = 11, column = 0)

labelZ = tk.Label(frame, textvariable = Z,
                         bg="lightblue",      
                         height=1,              
                         width=10,              
                         bd=3,                  
                         font=("Arial", 12, "bold"),  
                         fg="red",             
                         padx=2,               
                         pady=2,                
                         justify=tk.LEFT,    
                         relief=tk.SUNKEN,     
                         underline=0,           
                         wraplength=50,
                         anchor = "w"
                        )
labelZ.grid(row = 12, column = 1, padx = 10, sticky='w')
labelZ1=Label(frame, text="Posisi di sumbu Z:", font=("Arial",12,"bold"))
labelZ1.grid(row = 12, column = 0)

frame.config(menu = menubar)
frame.mainloop()  #muter-muter terus menerus hingga kiamat :D
