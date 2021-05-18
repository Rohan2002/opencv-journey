import cv2
import numpy as np

from api.stack_image_api import stack_images

print("Open CV Version", cv2.__version__)


def callback(x):
    pass


window = 'Trackbars'

cv2.namedWindow(window)
cv2.resizeWindow(window, 640, 250)

cv2.createTrackbar('hue_min', window, 0, 179, callback)
cv2.createTrackbar('hue_max', window, 179, 179, callback)
cv2.createTrackbar('sat_min', window, 0, 255, callback)
cv2.createTrackbar('sat_max', window, 255, 255, callback)
cv2.createTrackbar('val_min', window, 0, 255, callback)
cv2.createTrackbar('val_max', window, 255, 255, callback)

img = cv2.imread('/Users/user/Applications/machine-learning/opencv-stuff/images/bike.jpg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

video = False
if video:
    videoCaptureInstance = cv2.VideoCapture(0)

while True:

    hue_min = cv2.getTrackbarPos('hue_min', window)
    hue_max = cv2.getTrackbarPos('hue_max', window)
    sat_min = cv2.getTrackbarPos('sat_min', window)
    sat_max = cv2.getTrackbarPos('sat_max', window)
    val_min = cv2.getTrackbarPos('val_min', window)
    val_max = cv2.getTrackbarPos('val_max', window)

    low = np.array([hue_min, sat_min, val_min])
    high = np.array([hue_max, sat_max, val_max])

    hsv_filter = cv2.inRange(img_hsv, low, high)

    if video:
        ret, frame = videoCaptureInstance.read()
        if not ret:
            break
        video_frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv_filter = cv2.inRange(video_frame_hsv, low, high)

    object_detection = cv2.bitwise_and(img, img, mask=hsv_filter)
    print(hue_min, sat_min, val_min, hue_max, sat_max, val_max)

    stacked = stack_images(0.6, ([img, img_hsv], [hsv_filter, object_detection]))
    cv2.imshow('stacked_hsv', stacked)
    k = cv2.waitKey(1000) & 0xFF  # large wait time to remove freezing
    if k == 27:
        break
videoCaptureInstance.release()
cv2.destroyWindow('stacked_hsv')
