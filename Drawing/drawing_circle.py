import numpy as np 
import cv2

pic = np.zeros((500, 500, 3), dtype = 'uint8')
color = (122,1,121)

cv2.circle(pic, (250, 250), 100, color)
cv2.imshow('dark', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()