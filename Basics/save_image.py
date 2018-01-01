import numpy
import cv2

img = cv2.imread('E796am.jpg')
img = cv2.imwrite('image.png', img)
cv2.imshow('Original png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()