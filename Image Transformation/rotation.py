import numpy as np 
import cv2

pic = cv2.imread('tenacious.jpg')
rows = pic.shape[0]
cols = pic.shape[1]
center = (rows/2, cols/2)
angle = -30
M = cv2.getRotationMatrix2D(center, angle, 1)
rotate = cv2.warpAffine(pic, M, (cols, rows))

#NOTE : Both translation and rotation is carried out using warpAffine function
#difference between the two cases of rotation and translation is the Matrix that is supplied to the function

cv2.imshow('Rotated', rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()