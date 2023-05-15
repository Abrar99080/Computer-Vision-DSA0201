import cv2
import numpy as np

img=cv2.imread("C:/Users/KUSUMA PRIYA/Downloads/Screenshot 2023-05-10 102959.jpg")
resize=cv2.resize(img,(1450,1040))
cv2.imshow("resize",resize)
re=cv2.resize(img,(25,25))
cv2.imshow("half",re)
cv2.waitKey(0)
