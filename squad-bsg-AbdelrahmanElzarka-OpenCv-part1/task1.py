import cv2
import numpy as np

height = 50
width = 50
img1 = np.zeros((height,width,3), np.uint8)
img1[:,:] = (255,0,0)

img2 = np.zeros((height,width,3), np.uint8)
img2[:,:] = (0,255,0)

img3 = np.zeros((height,width,3), np.uint8)
img3[:,:] = (0,0,255)

img4 = np.zeros((height,width,3), np.uint8)
img4[:,:] = (255,255,255)

img5=np.hstack((img1,img2))
img6=np.hstack((img3,img4))
img7=np.vstack((img5,img6))

imgResized = cv2.resize(img7,(200,200))

cv2.imshow("Image",imgResized)
cv2.waitKey(0)
