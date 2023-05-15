import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)

path = "C:/Users/KUSUMA PRIYA/Downloads/Screenshot 2023-05-10 102959.jpg"
img =  cv2.imread(path)
imgDilation = cv2.dilate(img,kernel , iterations = 10)
cv2.imshow("Img Dialation",imgDilation)
cv2.waitKey(0)
