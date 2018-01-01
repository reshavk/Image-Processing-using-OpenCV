import numpy as np 
import cv2

pic = np.zeros((500, 500, 3), dtype = 'uint8')
cv2.rectangle(pic, (10,25), (400,150), (121,132,21), 3, lineType = 0, shift = 0)
#cv2.rectangle draws rectangle
#cv2.rectangle(image_name, (x,y) for A, (x,y) for C(diagonal point), (r, g, b), no_of_channels, lineType, shift)
cv2.imshow('dark', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()