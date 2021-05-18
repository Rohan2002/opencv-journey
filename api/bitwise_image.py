import cv2
import numpy as np

print("Open CV Version", cv2.__version__)

img1 = np.zeros((250, 500, 3), np.uint8) # Image with a white rectangle in the middle
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = np.zeros((250, 500, 3), np.uint8) # Image with a black rectangle on half and white on the other half
img2 = cv2.rectangle(img2, (500 // 2, 0), (500, 250), (255, 255, 255), -1)


# Black = 0 and White = 1

'''
bit-and

0 and 0 : 0
0 and 1 : 0
1 and 0 : 0
1 and 1 : 1
'''
bit_and = cv2.bitwise_and(img2, img1)

'''
bit-or

0 or 0 : 0
0 or 1 : 1
1 or 0 : 1
1 or 1 : 1
'''
bit_or = cv2.bitwise_or(img2, img1)

'''
bit-xor

0 xor 0 : 0
0 xor 1 : 1
1 xor 0 : 1
1 xor 1 : 0
'''
bit_xor = cv2.bitwise_xor(img2, img1)

'''
bit-not

not 1 = 0
not 0 = 1
'''
bit_not_img1 = cv2.bitwise_not(img1)
bit_not_img2 = cv2.bitwise_not(img2)

# Original Images
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

# Bitwise Transformations
cv2.imshow('bit_and', bit_and)
cv2.imshow('bit_or', bit_or)
cv2.imshow('bit_xor', bit_xor)
cv2.imshow('bit_img1_not', bit_not_img1)
cv2.imshow('bit_img2_not', bit_not_img2)

cv2.waitKey(0)
cv2.destroyWindow('img1')
cv2.destroyWindow('img2')
cv2.destroyWindow('bit_and')
cv2.destroyWindow('bit_or')
cv2.destroyWindow('bit_xor')
cv2.destroyWindow('bit_img1_not')
cv2.destroyWindow('bit_img2_not')