#Search for a program that interest you in youtune
#picked project "https://youtu.be/CKmAZss-T5Y"
#this project uses ai to identify gestures that commands the presentation
#Recreate the project 


from cvzone.HandTrackingModule import HandDetector
import cv2
import os
import numpy as np

# setup variable
width, height = 1500, 100
 
# Camera Setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)
 

while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

   