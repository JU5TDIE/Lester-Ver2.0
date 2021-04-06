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