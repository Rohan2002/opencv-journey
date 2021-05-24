import cv2
import numpy as np
from sys import platform
from api.stack_image_api import stack_images
from api.video_api import put_text_frame

print("Open CV Version", cv2.__version__)

shape_dict = {0: 'Circle', 1: 'point', 2: 'line', 3: 'Triangle', 4: 'Square', 5: 'Pentagon', 6: 'Hexagon',
              7: 'Septagon', 8: 'Octagon'}


def preprocess_image(img):
    # Gray scale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Remove noise
    img_blur = cv2.GaussianBlur(img_gray, (7, 7), 1)  # Higher sigma -> More blur
    # Edge Detection
    img_canny = cv2.Canny(img_blur, 50, 50)
    return img_canny


def getCountours(img, contour_img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # Only external contours.
    for cnt in contours:
        area = cv2.contourArea(cnt)
        cv2.drawContours(contour_img, cnt, -1, (255, 0, 0), 3)
        epsilon = 0.02 * cv2.arcLength(cnt, True)  # arc length is the peri
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        x, y, w, h = cv2.boundingRect(approx)

        if len(approx) == 4:
            aspect_ratio = w / float(h)
            if aspect_ratio > 0.95 and aspect_ratio < 1.05:
                shape = 'Square'
            else:
                shape = 'rectangle'
        else:
            shape = str(shape_dict.get(len(approx)))

        print(shape + " with area " + str(area))

        cv2.rectangle(contour_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        put_text_frame(contour_img, (x, y), shape, '')


if __name__ == '__main__':
    path = '/Users/user/Applications/machine-learning/opencv-stuff/images/shapes.png'
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    contour_img = img.copy()

    preprocess_img = preprocess_image(img)
    getCountours(preprocess_img, contour_img)

    imgStack = stack_images(0.6, ([img, preprocess_img], [contour_img, img]))

    cv2.imshow('stacked', imgStack)
    cv2.waitKey(0)
    cv2.destroyWindow('stacked')
