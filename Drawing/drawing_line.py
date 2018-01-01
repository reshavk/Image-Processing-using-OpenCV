import numpy as np 
import cv2

pic = np.zeros((500, 500, 3), dtype = 'uint8')

cv2.line(pic, (45, 50), (465, 456), (12,121,32))
cv2.imshow('line', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()