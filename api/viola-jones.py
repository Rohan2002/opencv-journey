import cv2
from sys import platform

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def preprocess_image(img):
    # Gray scale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img_gray


def face_detect(frame):
    preprocess_frame = preprocess_image(frame)
    faces = faceCascade.detectMultiScale(preprocess_frame, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


def read_video():
    videoCaptureInstance = cv2.VideoCapture(0)

    if not videoCaptureInstance.isOpened():
        raise IOError("Cannot open webcam")

    try:
        while True:
            ret, frame = videoCaptureInstance.read()  # ret = True/False availability of frame and frame = multiple picture frames

            if not ret:
                break

            face_detect(frame)

            cv2.imshow('video_window', frame)

            client_key_press = cv2.waitKey(1) & 0xFF

            # end video stream by escape key
            if client_key_press == 27:
                break
        videoCaptureInstance.release()  # Important: release current active webcam or stream in order for other instance of webcam
        cv2.destroyWindow('video_window')
        if platform == "darwin":
            cv2.waitKey(1)
    except cv2.error:
        print('Unexpected error occurred with reading image and error code is', cv2.error.code)


if __name__ == '__main__':
    read_video()
