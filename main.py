import sys
import time
import pynput
import win32gui
from threading import Thread
from hacks import casinofingerprint, casinokeypad, cayofingerprint, cayovoltage

def PrintBanner():
    print('''

██╗░░░░░███████╗░██████╗████████╗███████╗██████╗░  ██╗░░░██╗███████╗██████╗░  ██████╗░░░░░█████╗░
██║░░░░░██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗  ██║░░░██║██╔════╝██╔══██╗  ╚════██╗░░░██╔══██╗
██║░░░░░█████╗░░╚█████╗░░░░██║░░░█████╗░░██████╔╝  ╚██╗░██╔╝█████╗░░██████╔╝  ░░███╔═╝░░░██║░░██║
██║░░░░░██╔══╝░░░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗  ░╚████╔╝░██╔══╝░░██╔══██╗  ██╔══╝░░░░░██║░░██║
███████╗███████╗██████╔╝░░░██║░░░███████╗██║░░██║  ░░╚██╔╝░░███████╗██║░░██║  ███████╗██╗╚█████╔╝
╚══════╝╚══════╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚══════╝╚═╝░╚════╝░
                                                                                          ''')

def PrintCredits():
	print('''
Made by JUSTDIE
Special thanks to RedHeadEmile
	''')																					
	
def check_window():
	print('[*] Searching Grand Theft Auto V...')

	while True:
		hwnd = win32gui.FindWindow(None, "Grand Theft Auto V")
		
		if hwnd:
			print('[*] Grand Theft Auto V Detected!')
			print('')
			print('=============================================')
			return True
		
		time.sleep(1)

def casino_fingerprint():
	thread = Thread(target = casinofingerprint.main)
	thread.start()

def casino_keypad():
	thread = Thread(target = casinokeypad.main)
	thread.start()

def cayo_fingerprint():
	thread = Thread(target = cayofingerprint.main)
	thread.start()

def cayo_voltage():
	thread = Thread(target = cayovoltage.main)
	thread.start()

def shutdown():
	sys.exit()

def main():
	PrintBanner()
	PrintCredits()

	if check_window():
		with pynput.keyboard.GlobalHotKeys({
				'<F4>': shutdown,
                '<F5>': casino_fingerprint,
                '<F6>': casino_keypad,
                '<F7>': cayo_fingerprint,
                '<F8>': cayo_voltage}) as h:
			h.join()

if __name__ == "__main__":
	main()