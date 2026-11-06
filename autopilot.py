import cv2
import numpy as np


####### Operador de Sobel #######

# Capture livestream video content from camera 0
# cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("prácticaautopilot.mp4")
 
# while(1):
 
#     # Take each frame
#     _, frame = cap.read()
#     frame = cv2.resize(frame, (400, 300))
     
#     # Convert to HSV for simpler calculations
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     
#     # Calculation of Sobelx
#     sobel = cv2.Sobel(frame,cv2.CV_8U,1,1,ksize=3)
#     # sobel = cv2.Sobel(frame,cv2.CV_8U,1,1,ksize=5)
#     # sobel = cv2.Sobel(frame,cv2.CV_8U,1,1,ksize=7)
     
#     cv2.imshow('original',frame) 
#     cv2.imshow('sobel', sobel)
    
#     k = cv2.waitKey(5) & 0xFF
#     if k == 27: 
#         break
 
# cv2.destroyAllWindows()
 
# #release the frame
# cap.release()

# matriz=[[138,138,138,149,198],[138,138,149,198,214],[138,149,198,214,214],[149,198,214,214,214],[198,214,214,214,214]]
# matriz=np.array(matriz)
# print(matriz)

# # Calcula soble en la matriz
# sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
# sobel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

# res = np.zeros(matriz.shape)

# for i in range(1, matriz.shape[0]-1):
#     for j in range(1, matriz.shape[1]-1):
#         region = matriz[i-1:i+2, j-1:j+2]
#         gx = np.sum(sobel_x * region)
#         gy = np.sum(sobel_y * region)
#         res[i, j] = np.sqrt(gx**2 + gy**2)

# print(res)


####### Binarización con Histéresis #######
# cap = cv2.VideoCapture("prácticaautopilot.mp4")


# # loop runs if capturing has been initialized
# while(1):

# 	# reads frames from a camera
# 	ret, frame = cap.read()
# 	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# 	# Display an original image
# 	cv2.imshow('Original',frame)

# 	# finds edges in the input image and
# 	# marks them in the output map edges
# 	edges = cv2.Canny(frame,100,200)

# 	# Display edges in a frame
# 	cv2.imshow('Edges',edges)

# 	# Wait for Esc key to stop
# 	k = cv2.waitKey(5) & 0xFF
# 	if k == 27:
# 		break


# # Close the window
# cap.release()

# # De-allocate any associated memory usage
# cv2.destroyAllWindows()

