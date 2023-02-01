import cv2
import numpy as np
from PIL import ImageGrab


def detect_pixel_color(screen_image, color):
    hsv = cv2.cvtColor(screen_image, cv2.COLOR_BGR2HSV)
    lower_color = np.array([color[0] - 10, 100, 100])
    upper_color = np.array([color[0] + 10, 255, 255])
    mask = cv2.inRange(hsv, lower_color, upper_color)
    return mask

# capture an image of the screen
screen = np.array(ImageGrab.grab(bbox=(0,0,1920,1080)))

# detect the presence of a specific color in the image
color = [100, 255, 255]
mask = detect_pixel_color(screen, color)

if np.sum(mask) > 0:
    # send a notification to Electron that the color was detected
    print('color detected')
else:
    # send a notification to Electron that the color was not detected
    print('color not detected')
