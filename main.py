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

pressed = []
def on_press(key):
	if key in pressed:
		return True
	pressed.append(key)

	try:
		k = key.char
	except:
		k = key.name

	if k == "f4":
		return False

	elif k == "f5":
		thread = Thread(target = casinofingerprint.main)
		thread.start()

	elif k == "f6":
		thread = Thread(target = casinokeypad.main)
		thread.start()

	elif k == "f7":
		thread = Thread(target = cayofingerprint.main)
		thread.start()

	elif k == "f8":
		thread = Thread(target = cayovoltage.main)
		thread.start()

def on_release(key):
	if key in pressed:
		pressed.remove(key)

def main():
	PrintBanner()
	PrintCredits()

	if check_window():
		listener = pynput.keyboard.Listener(on_press = on_press, on_release = on_release)
		listener.start()
		listener.join()

if __name__ == "__main__":
	main()