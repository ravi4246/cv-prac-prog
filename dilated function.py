import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
print(kernel)
path="arch.jpg"
img=cv2.imread(path)
imgDilated=cv2.dilate(img,kernel,iterations=10)
cv2.imshow("Dilated image",imgDilated)
cv2.waitKey(0)
