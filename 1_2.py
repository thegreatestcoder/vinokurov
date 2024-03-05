import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT)

i = 1
while i != 5:
   GPIO.output(24, 1)
   time.sleep(1)
   GPIO.output(24, 0)
   time.sleep(1)
   i+=1

GPIO.cleanup()