#*********************************************************************
#******** PROGRAM SISTEM KENDALI ROBOT ARTICULATED TIPE MK-2 *********
#********             Dibuat Oleh : Djukarna                 *********
#********             Tanggal : 11 Maret 2025                *********
#********         Fakultas Keguruan & Pendidikan             *********
#********         Universitas Katolik Parahyangan            *********
#********               Bandung-Jawa Barat                   *********
#*********************************************************************

# Library yang digunakan:

from time import sleep
import RPi.GPIO as GPIO

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

durationFwd = 40000  #forward durasi ( harus dikalibasi ulang disesuaikan dengan reduksi roda gigi
durationBwd = 40000  #backward durasi ( harus dikalibasi ulang disesuaikan dengan reduksi roda gigi

delay = 0.00001      #delay microsecond berhubungan dengan kecepatan putar motor stepper

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

#Tulis Kode Program anda disini !






