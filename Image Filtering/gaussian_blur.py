import numpy as np 
import cv2

pic = cv2.imread('image.png')
matrix = (7,7)

blur = cv2.GaussianBlur(pic, matrix, 0)
#In gaussian blur we replace the central pixel by the average of the neighbouring pixels

cv2.imwrite('blurred.png', blur)
cv2.imshow('blurred', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()