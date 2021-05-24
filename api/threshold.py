import cv2
import numpy as np

from api.stack_image_api import stack_images

print("Open CV Version", cv2.__version__)

# Global Threshold
def binary_threshold(image, thres, inverse):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    th = None
    _, th = cv2.threshold(image, thres, 255, cv2.THRESH_BINARY)
    if inverse:
        _, th = cv2.threshold(image, thres, 255, cv2.THRESH_BINARY_INV)
    return th


# pixels less than k will remain it's original value and other pixels great than k will change to k
def trunk_threshold(image, thres):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, th = cv2.threshold(image, thres, 255, cv2.THRESH_TRUNC)
    return th


# less than k will be 0 else unchanged
def zero_threshold(image, thres, inverse):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    th = None
    _, th = cv2.threshold(image, thres, 255, cv2.THRESH_TOZERO)
    if inverse:
        _, th = cv2.threshold(image, thres, 255, cv2.THRESH_TOZERO_INV)
    return th


if __name__ == '__main__':
    image = cv2.imread('/Users/user/Applications/machine-learning/opencv-stuff/images/bike.jpg')

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    Thresh = 200

    th_binary = binary_threshold(image, Thresh, False)
    th_binary_inv = binary_threshold(image, Thresh, True)
    th_trunk = trunk_threshold(image, 127)

    th_zero = zero_threshold(image, 127, False)
    th_zero_inv = zero_threshold(image, 127, True
                                 )
    stacked = stack_images(0.6, ([th_binary, th_binary_inv], [th_trunk, gray_image], [th_zero, th_zero_inv]))
    cv2.imshow('stacked_threshold', stacked)
    cv2.waitKey(0)
    cv2.destroyWindow('stacked_threshold')
