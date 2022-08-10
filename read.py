#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        print("Please scan an RFID sticker/card")
        id = reader.read()[0]
        print("The corresponding ID to this card is:", id)
        
finally:
        GPIO.cleanup()
