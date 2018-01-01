import numpy
import cv2

img = cv2.imread('E796am.jpg')
#img = cv2.imread('E796am.jpg', 0) grayscale image displayed
#img = cv2.imread('E796am.jpg', 4) image displayed using all colours RGB
#img = cv2.imread('E796am.jpg', -1) image read as is using the alpha channel

cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()