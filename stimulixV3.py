#!/usr/bin/python

# Main script for Adafruit Internet of Things Printer 2.  Monitors button
# for taps and holds, performs periodic actions (Twitter polling by default)
# and daily actions (Sudoku and weather by default).
# Written by Adafruit Industries.  MIT license.
#
# MUST BE RUN AS ROOT (due to GPIO access)
#
# Required software includes Adafruit_Thermal, Python Imaging and PySerial
# libraries. Other libraries used are part of stock Python install.
#
# Resources:
# http://www.adafruit.com/products/597 Mini Thermal Receipt Printer
# http://www.adafruit.com/products/600 Printer starter pack

from __future__ import print_function
import RPi.GPIO as GPIO
import subprocess, time, Image, socket, os
from Adafruit_Thermal import *


buttonPin    = 23
holdTime     = 2     # Duration for button hold (shutdown)
tapTime      = 0.01  # Debounce time for button taps
nextInterval = 0.0   # Time of next recurring operation
dailyFlag    = False # Set after daily trigger occurs
lastId       = '1'   # State information passed to/from interval script
printer      = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

# Initialization

# Use Broadcom pin numbers (not Raspberry Pi pin numbers) for GPIO
GPIO.setmode(GPIO.BCM)



# Processor load is heavy at startup; wait a moment to avoid
# stalling during greeting.
time.sleep(3)

# Print greeting image
while(True):
	if os.path.exists('gfx/print.png'):
		image = Image.open('gfx/print.png')
		# imageRotated = image
		imageRotated = image.rotate(90)
		imageRotated = imageRotated.resize((384*image.size[1]/image.size[0],384 *2 ))
		imageRotated = imageRotated.convert("L")
		
		
		printer.printImage(imageRotated, True)
		printer.feed(3)
		time.sleep(5)
		printer.printImage(imageRotated, True)
		printer.feed(3)
		time.sleep(3)
		os.remove('gfx/print.png')
	else:
		time.sleep(3)

