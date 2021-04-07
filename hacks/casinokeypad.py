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

def dot_check(a, img):
    hint = []

    for i in range(0, 5):
        crop_img = img[height[i]:height[i] + 1, length[a]:length[a] + 1]

        if np.mean(crop_img) == 255:
            hint.append(1)
        else:
            hint.append(0)

    return DIGITS_LOOKUP[tuple(hint)]

def check():
    while True:
        screen = ImageGrab.grab(bbox)
        grayImage = cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2GRAY)
        (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 215, 255, cv2.THRESH_BINARY)
        crop_img = blackAndWhiteImage[92:92 + 1, 44:44 + 1]

        if np.mean(crop_img) == 0:
            keyboard.press_and_release('w')
            time.sleep(0.025)
        elif np.mean(crop_img) == 255:
            break