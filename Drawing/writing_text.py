import numpy as np 
import cv2

pic = np.zeros((312, 851, 3), dtype = 'uint8')

font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(pic, 'tenacious', (170, 156), font, 3, (0, 255, 255), 4, cv2.LINE_8)
cv2.imwrite('tenacious.jpg', pic)

cv2.imshow('dark', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()