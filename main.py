# main.py

import Adafruit_DHT
import time
import RPi.GPIO as GPIO  

SENSOR = Adafruit_DHT.DHT11
PIN = 4

try:
    while True:
        lembab, suhu = Adafruit_DHT.read(SENSOR, PIN)

        if lembab is not None and suhu is not None:
            print("Suhu={0:0.1f}*C  Kelembaban={1:0.1f}%".format(suhu, lembab))

            # menambah logic untuk print suatu keadaan suhu 
            # jika: suhu kurang dari || lebih dari sekian temperatur
            if suhu <= 35 and suhu >= 16:
                print("Suhu normal")
            elif suhu >= 35 and suhu <= 47:
                print("Suhu panas")
            elif suhu <= 16 and suhu >= -15 :
                print("Suhu dingin")
            else:
                print("Suhu tidak normal, membahayakan")

        else:
            print("Tidak bisa membaca data dari sensor")
        time.sleep(1)
    
    
# Menghentikan program dengan CTRL + C
except KeyboardInterrupt:
    print("Sensor dihentikan")