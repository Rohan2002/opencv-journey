import sys

import cv2
from sys import platform
import os
from datetime import datetime

print("Open CV Version", cv2.__version__)


def read_video(webcam: bool):
    input_video_path = 'videos'

    if not os.path.isdir(input_video_path):
        os.mkdir(input_video_path)
        print('Videos directory is created and now put a video in the directory')
        sys.exit()
    if len(os.listdir(input_video_path)) == 0:
        print("Videos directory is empty!")
        sys.exit()

    video_file_path = f'{input_video_path}/{os.listdir(input_video_path)[0]}'
    if webcam:
        video_file_path = 0

    videoCaptureInstance = cv2.VideoCapture(video_file_path)

    if not videoCaptureInstance.isOpened():
        raise IOError("Cannot open webcam")

    try:
        while True:
            ret, frame = videoCaptureInstance.read()  # ret = True/False availability of frame and frame = multiple picture frames
            convert_frame_to_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('video_window', convert_frame_to_gray)

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


# Access video flags here https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html
def get_video_width_height_frames(videoCaptureInstance: cv2.VideoCapture):
    width = int(videoCaptureInstance.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(videoCaptureInstance.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frames = int(videoCaptureInstance.get(cv2.CAP_PROP_FRAME_COUNT))
    return {"Width": width, "Height": height, "Frames": frames}


def write_video(frames: int, videoCaptureInstance: cv2.VideoCapture, extension: str):
    directory = 'output-videos'

    if not os.path.isdir(directory):
        os.mkdir(directory)
        print(directory + " doesn't exist so creating directory")

    codec = ''
    if extension.lower() == 'mp4':
        codec = 'mp4v'
    elif extension.lower() == 'avi':
        codec = 'XVID'
    else:
        raise TypeError("mp4 or avi are the only extensions allowed.")

    date_time = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    new_video_file = directory + f'/video_{date_time}.{extension.lower()}'
    fourcc_encoding = cv2.VideoWriter_fourcc(*codec)

    videoParamDict = get_video_width_height_frames(videoCaptureInstance)

    videoWriterInstance = cv2.VideoWriter(new_video_file, fourcc_encoding, frames,
                                          (videoParamDict["Width"], videoParamDict["Height"]))

    try:
        while True:
            ret, frame = videoCaptureInstance.read()
            if not ret:
                break
            convert_frame_to_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            videoWriterInstance.write(frame)

            cv2.imshow('video_window', convert_frame_to_gray)

            client_key_press = cv2.waitKey(1) & 0xFF

            # end video stream by escape key
            if client_key_press == 27:
                break

        videoCaptureInstance.release()
        videoWriterInstance.release()
        cv2.destroyWindow('video_window')
        if platform == "darwin":
            cv2.waitKey(1)

    except cv2.error:
        print('Unexpected error occurred with reading image and error code is', cv2.error.code)


if __name__ == '__main__':
    read_video(True)  # True for webcam access or false

    webcamCaptureInstance = cv2.VideoCapture(0)
    # write_video(20, webcamCaptureInstance, 'avi')
