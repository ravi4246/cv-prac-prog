import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
print(kernel)
path="arch.jpg"
img=cv2.imread(path)
imgErosion=cv2.erode(img,kernel,iterations=2)
cv2.imshow("Erosion",imgErosion)
cv2.waitKey(0)
