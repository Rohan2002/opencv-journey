import cv2
from sys import platform

print("Open CV Version", cv2.__version__)


def read_image(input_file: str):
    try:
        frame = cv2.imread(input_file,
                           cv2.IMREAD_UNCHANGED)  # reads the image, keys are cv2.IMREAD_COLOR(1) or cv2.IMREAD_GRAYSCALE(0) or cv2.IMREAD_UNCHANGED(-1)

        cv2.imshow("Output", frame)  # title, image-input
        cv2.setMouseCallback('Output', frame)
        client_key_press = cv2.waitKey(0) & 0xFF  # 0 is infinite or 1000 milliseconds = 1 second to show image
        if client_key_press == 27:
            cv2.destroyAllWindows()  # Destroy window on escape key
        if platform == "darwin":
            cv2.waitKey(1)
    except cv2.error:
        print('Unexpected error occurred with reading image and error code is', cv2.error.code)


if __name__ == '__main__':
    read_image("../images/skydive.jpg")
