import os
import cv2
import time
import keyboard
import numpy as np
from PIL import ImageGrab

DIGITS_LOOKUP = {
    (1, 0, 0, 0, 0): 1,
	(0, 1, 0, 0, 0): 2,
	(0, 0, 1, 0, 0): 3,
	(0, 0, 0, 1, 0): 4,
	(0, 0, 0, 0, 1): 5
}

height = [2, 110, 218, 326, 434]
length = [50, 158, 266, 374, 482, 590]

bbox = (454, 300, 1080, 830)