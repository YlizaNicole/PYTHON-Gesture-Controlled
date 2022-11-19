#Search for a program that interest you in youtune
#picked project "https://youtu.be/CKmAZss-T5Y"
#this project uses ai to identify gestures that commands the presentation
#Recreate the project 


from cvzone.HandTrackingModule import HandDetector
import cv2
import os
import numpy as np

# setup variable
width, height = 100, 100
folderPath= "Presentation"
imgNumber = 0
 
# Camera Setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Get list of presentation images
pathImages = sorted(os.listdir(folderPath), key=len)
print(pathImages) 

while True:
    success, img = cap.read()
    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)
    cv2.imshow("Image", img)
    cv2.imshow("Presentation", imgCurrent)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

   