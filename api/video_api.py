import sys
from typing import Union

import cv2
from sys import platform
import os
from datetime import datetime

from util import check_dir

print("Open CV Version", cv2.__version__)


def read_video(webcam: bool, gray: bool, text: bool):
    input_video_path = '../videos'

    if not check_dir(input_video_path):
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

            if not ret:
                break

            # Text
            if text:
                resolution_text = 'Width: ' + str(
                    videoCaptureInstance.get(cv2.CAP_PROP_FRAME_WIDTH)) + " Height: " + str(
                    videoCaptureInstance.get(cv2.CAP_PROP_FRAME_HEIGHT))
                date_text = str(datetime.now().strftime('%Y-%m-%d_%H:%M:%S'))
                frame = put_text_frame(frame, (10, 30), resolution_text, 'black')
                frame = put_text_frame(frame, (10, 60), date_text, 'black')
            # Colorful
            if gray:
                convert_frame_to_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imshow('video_window', convert_frame_to_gray)
            else:
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


def set_resolution(videoCaptureInstance: cv2.VideoCapture, width: int, height: int) -> tuple:
    videoCaptureInstance.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    videoCaptureInstance.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    return str(videoCaptureInstance.get(cv2.CV_CAP_PROP_FRAME_WIDTH)), str(
        videoCaptureInstance.get(cv2.CV_CAP_PROP_FRAME_HEIGHT))


def put_text_frame(frame, text_position, text: str, color: str):
    text_font = cv2.FONT_HERSHEY_SIMPLEX
    text_font_scale = 1
    text_line_type = 2
    text_font_color = 0
    if color.lower() == 'white':
        text_font_color = (255, 255, 255)
    return cv2.putText(frame, text, text_position, text_font, text_font_scale, text_font_color, text_line_type)


if __name__ == '__main__':
    read_video(True, False, True)  # webcam, gray, text

    webcamCaptureInstance = cv2.VideoCapture(0)
    # write_video(20, webcamCaptureInstance, 'avi')
