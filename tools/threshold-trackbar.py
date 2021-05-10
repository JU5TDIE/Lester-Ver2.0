import cv2
import numpy as np
from PIL import Image

def nothing(x):
    pass

cv2.namedWindow('binary')
cv2.createTrackbar('threshold', 'binary', 0, 255, nothing)
cv2.setTrackbarPos('threshold', 'binary', 127)

img_color = Image.open('.png')
img_gray = cv2.cvtColor(np.array(img_color), cv2.COLOR_RGB2GRAY)

while True:
    low = cv2.getTrackbarPos('threshold', 'binary')
    ret, img_binary = cv2.threshold(img_gray, low, 255, cv2.THRESH_BINARY)

    cv2.imshow('binary', img_binary)
    if cv2.waitKey(1)&0xFF == 27:
        break

cv2.destroyAllWindows()
