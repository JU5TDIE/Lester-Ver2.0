import os
import cv2
import time
import keyboard
import numpy as np
from PIL import ImageGrab

DIGITS_LOOKUP = {
    (1, 1, 1, 0, 1, 1, 1): 0,
	(0, 0, 1, 0, 0, 1, 0): 1,
	(1, 0, 1, 1, 1, 0, 1): 2,
	(1, 0, 1, 1, 0, 1, 1): 3,
	(0, 1, 1, 1, 0, 1, 0): 4,
	(1, 1, 0, 1, 0, 1, 1): 5,
	(1, 1, 0, 1, 1, 1, 1): 6,
	(1, 0, 1, 0, 0, 1, 0): 7,
	(1, 1, 1, 1, 1, 1, 1): 8,
	(1, 1, 1, 1, 0, 1, 1): 9
}

RIGHT_SYMBOLS = {
	(0, 1): 10,
	(1, 0): 2,
	(0, 0): 1
}

moves = {
	(0, 0, 1, 1, 2, 2): ['return', 'return', 'return', 'return', 'return', 'return'], # (1-1) + (2-2) + (3-3)
	(0, 0, 1, 2, 2, 1): ['return', 'return', 'return', 's', 'return', 'return', 'return'], # (1-1) + (2-3) + (3-2)
	(0, 1, 1, 0, 2, 2): ['return', 's', 'return', 'return', 'w', 'return', 'return', 'return'], #(1-2) + (2-1) + (3-3)
	(0, 1, 1, 2, 2, 0): ['return', 's', 'return', 'return', 'return', 'return', 'return'], # (1-2) + (2-3) + (3-1)
	(0, 2, 1, 0, 2, 1): ['return', 'w', 'return', 'return', 'w', 'return', 'return', 'return'], # (1-3) + (2-1) + (3-2)
	(0, 2, 1, 1, 2, 0): ['return', 'w', 'return', 'return', 'return', 'return', 'return'] # (1-3) + (2-2) + (3-1) 
}

bbox = (0, 0, 1920, 1080)

# objective numbers
objectivenumber_height = [123, 137, 137, 154, 173, 173, 195] #objective numbers have same height
objectivenumber_length_0 = [865, 849, 881, 865, 849, 881, 865] # first number
objectivenumber_length_1 = [955, 939, 971, 955, 939, 971, 955] # second number
objectivenumber_length_2 = [1043, 1029, 1061, 1043, 1029, 1061, 1043] # third number

# left numbers
leftnumber_length = [509, 495, 527, 509, 495, 527, 509] # left nubmers have same length
leftnumber_height_0 = [271, 287, 287, 303, 323, 323, 343] # first number
leftnumber_height_1 = [507, 522, 522, 540, 557, 557, 579] # second number
leftnumber_height_2 = [741, 755, 755, 773, 791, 791, 813] # third number

# right symbols
rightsymbol_length = [1351, 1349] # right symbols have same length
rightsymbol_height_0 = [305, 277] # first symbol
rightsymbol_height_1 = [541, 513] # second symbol
rightsymbol_height_2 = [775, 747] # third symbol