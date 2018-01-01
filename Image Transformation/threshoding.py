import numpy as np 
import cv2

pic = cv2.imread('image.png', 0)
threshold_value = 100

(T_value, binary_threshold) = cv2.threshold(pic, threshold_value, 255, cv2.THRESH_BINARY)

cv2.imwrite('binary.png', binary_threshold)
cv2.imshow('binary', binary_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()