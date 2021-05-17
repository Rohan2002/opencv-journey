import cv2
import numpy as np

from api.video_api import put_text_frame

# reload(api.video_api)
print("Open CV Version", cv2.__version__)


def get_all_events():
    events = [i for i in dir(cv2) if 'EVENT' in i]
    print(events)


def mouse_click_event(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONUP:
        point_str = '(' + str(x) + ", " + str(y) + ")"
        # print(point_str)
        cv2.imshow('image', put_text_frame(frame, (x, y), point_str, 'white'))

    if event == cv2.EVENT_LBUTTONDOWN:
        b = frame[x, y, 0]
        g = frame[x, y, 1]
        r = frame[x, y, 2]
        color_str = '(' + str(r) + ", " + str(g) + ", " + str(b) + ')'
        mColor = np.zeros((512,512,3), np.uint8)
        mColor[:] = [b,g,r]
        print(mColor)
        cv2.imshow('color', mColor)

if __name__ == '__main__':
    frame = cv2.imread('images/skydive.jpg')
    cv2.imshow('image', frame)
    cv2.setMouseCallback('image', mouse_click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows('image')
