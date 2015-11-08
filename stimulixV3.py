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

		# Resize of the art image
		imgOeuvre = Image.open('gfx/bearings.png')
		imgOeuvre = imgOeuvre.resize((384,384 ))
		imgOeuvre = imgOeuvre.rotate(90)

		# Resize of the art image
		image = Image.open('gfx/print.png')
		imageRotated = image.resize((384*2,384 ))
		imageRotated = imageRotated.rotate(90)
		imageRotated = imageRotated.convert("L")
		
		# Printing of the two tickets
		# Tickets 1
		printer.println("#stimulix #museomixmtl")
		printer.printImage(imageRotated, True)
		printer.printImage(imgOeuvre, False)
		printer.feed(3)
		time.sleep(5)

		# Tickets 2
		printer.println("#stimulix #museomixmtl")
		printer.printImage(imageRotated, True)
		printer.printImage(imgOeuvre, False)
		printer.feed(3)
		time.sleep(3)

		# remove temporary graph
		os.remove('gfx/print.png')
	else:
		time.sleep(3)

