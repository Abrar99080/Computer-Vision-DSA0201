import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)

path ="C:/Users/KUSUMA PRIYA/Downloads/Screenshot 2023-05-10 102959.jpg"
img =  cv2.imread(path)

imgBlur = cv2.GaussianBlur(img,(7,7),0)




cv2.imshow("Img Blur",imgBlur)

cv2.waitKey(0)
