#!/usr/bin/python3

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(false)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
print("17 27亮")
GPIO.output(17, GPIO.HIGH)
GPIO.output(27, GPIO.HIGH)