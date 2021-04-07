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

def calculate(numbers):
    keyboardgo = []

    for i in range(0, 6):
        if i == 0:
            if numbers[i] == 1:
                keyboardgo.append('1')
            elif numbers[i] == 2:
                keyboardgo.append('s')
            elif numbers[i] == 3:
                keyboardgo.append('s')
                keyboardgo.append('s')
            elif numbers[i] == 4:
                keyboardgo.append('s')
                keyboardgo.append('s')
                keyboardgo.append('s')
            elif numbers[i] == 5:
                keyboardgo.append('s')
                keyboardgo.append('s')
                keyboardgo.append('s')
                keyboardgo.append('s')
        if i > 0:
            a = i - 1
            if numbers[i] == numbers[a]:
                keyboardgo.append('1')
            elif numbers[i] < numbers[a]:
                value = numbers[a] - numbers[i]
                for i in range(0, value):
                    keyboardgo.append('w')
            elif numbers[i] > numbers[a]:
                value = numbers[i] - numbers[a]
                for i in range(0, value):
                    keyboardgo.append('s')
        keyboardgo.append('return')

    print(keyboardgo)
    for key in keyboardgo:
        keyboard.press_and_release(key)
        if key == 's' or 'w':
            time.sleep(0.025)
        if key == 'return':
            time.sleep(2.2)

    print('end')
