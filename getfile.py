#!/usr/bin/python
import os

print os.path.exists('C:/Users/Hugo/Dropbox/Screenshots/toprint/print.png')
if os.path.exists('C:/Users/Hugo/Dropbox/Screenshots/toprint/print.png'):
	print os.remove('C:/Users/Hugo/Dropbox/Screenshots/toprint/print.png')