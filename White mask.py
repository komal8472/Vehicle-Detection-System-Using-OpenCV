import cv2
from Tracker import *
from itertools import zip_longest

#Load video
cap=cv2.VideoCapture(r'D:\AVS-CODE\Projects\opencv project\Smart Traffic Monitoring System\highway.mp4')

#Check if video opened successfully
if not cap.isOpened():
    print('Error')
    exit()
    
#Create background subtractor
object_detector=cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=40)

while True:
    ret, frame=cap.read()
    if not ret:
        print('Failed to read frame')
        break
    #Apply background subtraction
    mask=object_detector.apply(frame)
    
    #Display the original frame and mask
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    
    #Exit on processing ESC key
    key=cv2.waitKey(30)
    if key==27:
        break
#Release resources
cap.release()
cv2.destroyAllWindows()