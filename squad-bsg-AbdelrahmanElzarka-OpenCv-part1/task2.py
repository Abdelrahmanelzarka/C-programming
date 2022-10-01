import cv2
import numpy as np



cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
cap.set(10, 70)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

size = (frame_width, frame_height)

result = cv2.VideoWriter('H:\Vortex/task1/testvideo.avi',
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)


while True:
        success, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgR = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        imgH = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        C = input()
        print(C)
        if(C=='Q'):
            exit()
        elif(C=='R'):
            cv2.imshow("Output8", imgR)
            cv2.waitKey(0)
        elif(C=='C'):
            cv2.imwrite("H:\Vortex/task1/test.png", img)
        elif(C=='S'):
            i = 0
            while i < 100:
                success, img = cap.read()
                result.write(img)
                i = i + 1
        elif(C=='G'):
            cv2.imshow("Output7", gray)
            cv2.waitKey(0)
        elif(C=='H'):
            cv2.imshow("Output6", imgH)
            cv2.waitKey(0)
        elif(C=='X'):
            cv2.imshow("Output1", imgH)
            cv2.imshow("Output2", gray)
            cv2.imshow("Output3", img)
            cv2.imshow("Output4", imgR)
            cv2.waitKey(0)
        elif(C=='Z'):
            cv2.imshow("Output5", img)
            cv2.waitKey(0)


