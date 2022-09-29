# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
#"F:\OneDrive - University of Engineering and Technology Taxila\7th semester\fyp\code\ast.mp4"
cap = cv2.VideoCapture('ast.mp4')
 
 
# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")
 
# Read until video is completed
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
 
        cv2.imshow('Frame', frame)
       # print('video captured')
 #
        ## Press Q on keyboard to  exit
        if cv2.waitKey(1)& 0xFF  == ord('q'):
            break
 
    # Break the loop
    else:
        break
 
# When everything done, release the video capture object

cap.release()
 

cv2.destroyAllWindows()