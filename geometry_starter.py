import cv2
from sys import platform
import numpy as np

print("Open CV Version", cv2.__version__)

if __name__ == '__main__':
    try:
        # image = cv2.imread('images/bike.jpg', cv2.IMREAD_UNCHANGED)  # -> retval matrix
        image = np.zeros([512,512,3], np.uint8)
        height, width, channels = image.shape

        print("Height: " + str(height) + " Width: " + str(width))

        image = cv2.rectangle(image, (0, 0), (width, 3000), (200, 0, 0), 20)
        image = cv2.circle(image, (width // 2, height // 2), 100, (200, 0, 0), -1)

        image = cv2.putText(image, 'OpenCv', (10, height // 2), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 255), 10, cv2.LINE_AA)

        cv2.imshow('image-show', image)

        client_key_press = cv2.waitKey(0) & 0xFF
        if client_key_press == 27:
            cv2.destroyAllWindows('image-show')
        if platform == "darwin":
            cv2.waitKey(1)

    except cv2.error:
        print('Unexpected error occurred with reading image and error code is', cv2.error.code)
