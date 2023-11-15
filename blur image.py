import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
print(kernel)
path="arch.jpg"
img=cv2.imread(path)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgGaussianblur=cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Gaussianblur",imgGaussianblur)
cv2.waitKey(0)
