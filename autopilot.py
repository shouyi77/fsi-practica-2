import cv2
import numpy as np
 
# Capture livestream video content from camera 0
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("prácticaautopilot.mp4")
 
while(1):
 
    # Take each frame
    _, frame = cap.read()
    frame = cv2.resize(frame, (400, 300))
     
    # Convert to HSV for simpler calculations
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     
    # Calculation of Sobelx
    sobel = cv2.Sobel(frame,cv2.CV_8U,1,1,ksize=3)
    # sobel = cv2.Sobel(frame,cv2.CV_8U,1,1,ksize=5)
    # sobel = cv2.Sobel(frame,cv2.CV_8U,1,1,ksize=7)
     
    cv2.imshow('original',frame) 
    cv2.imshow('sobel', sobel)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27: 
        break
 
cv2.destroyAllWindows()
 
#release the frame
cap.release()