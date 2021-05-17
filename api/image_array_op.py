import cv2
import numpy as np

print("Open CV Version", cv2.__version__)


def image_shape(image):
    return image.shape


def num_of_pixels(image):
    return image.size


def image_val_datatype(image):
    return image.dtype


def resize_image(image, size):
    return cv2.resize(image, size)


def remove_color_channels(image):
    b, g, r = cv2.split(image)  # each channel divided into 4032,3024
    zero_color = np.zeros((4032, 3024), np.uint8)
    img_red = cv2.merge((zero_color, zero_color, r))
    img_blue = cv2.merge((b, zero_color, zero_color))
    img_green = cv2.merge((zero_color, g, zero_color))
    return img_red, img_blue, img_green


def combine_images(image_one, image_two):
    cv2.add(image_one, image_two)


def combine_images_weighted(image_one, image_two, alpha, beta, gamma):
    if image_one.shape[0] != image_two.shape[0] or image_one.shape[1] != image_two.shape[1]:
        raise TypeError("Image dimensions don't match!")
    return cv2.addWeighted(image_one, alpha, image_two, beta, gamma)


if __name__ == '__main__':
    image = cv2.imread('images/skydive.jpg')
    imageTwo = cv2.imread('images/bike.jpg')
    print('Shape: ' + str(image_shape(image)))  # row, col, channels
    print('Number of pixels: ' + str(num_of_pixels(image)))
    print('Datatype: ' + str(image_val_datatype(image)))

    # img_red, img_blue, img_green = remove_color_channels(image)
    imageTwo = resize_image(imageTwo, (3024, 4032))

    add_weighted = combine_images_weighted(image, imageTwo, 0.5, 0.5, 0)
    cv2.imshow('weighted_add', add_weighted)
    cv2.waitKey(0)
    cv2.destroyWindow('weighted_add')
