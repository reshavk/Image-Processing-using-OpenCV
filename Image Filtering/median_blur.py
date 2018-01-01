import numpy as np 
import cv2

pic = cv2.imread('noisy.png')

kernel = 3;

median = cv2.medianBlur(pic, kernel)
#Median blur is used to remove the affect of noisy pixels from the image
#Noisy pixels appear as if salt is spread over the image
#In median blur technique the centre pixel is replaced by the median of the neighboring pixels

cv2.imwrite('median.jpg', median)
cv2.imshow('median', median)
cv2.waitKey(0)
cv2.destroyAllWindows()