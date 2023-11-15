import cv2
image = cv2.imread('arch.jpg')
scaling_factor = 2.0
scaled_image = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_LINEAR)
cv2.imshow('Original Image', image)
cv2.imshow('Scaled to a Larger Size', scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
