import time
import pynput
import win32gui
from threading import Thread
from hacks import casinofingerprint, casinokeypad, cayofingerprint, cayovoltage

def check_window():
	print('[*] Searching Grand Theft Auto V...')

	while True:
		hwnd = win32gui.FindWindow(None, "Grand Theft Auto V")
		
		if hwnd:
			print('[*] Grand Theft Auto V Detected!')
			print('')
			print('')
			return True
		
		time.sleep(1)