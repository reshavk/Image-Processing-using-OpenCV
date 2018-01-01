import numpy as np 
import cv2 

pic = cv2.imread('image.png')

threshold1 = 50
threshold2 = 100

canny = cv2.Canny(pic, threshold1, threshold2)
#Canny edge detector is quite similar to image thresholding
#Function says that in pic all pixels having values less than threshold1 should be 0 an all pixels having value freater than threshold2 should be 1
#This leads to the formation of an edge in between
#These edges are called canny edges

cv2.imwrite('canny.png', canny)
cv2.imshow('canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()