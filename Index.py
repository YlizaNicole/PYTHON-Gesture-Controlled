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
folderPath= "Presentation"

 
# Camera Setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Get list of presentation images
pathImages = sorted(os.listdir(folderPath), key=len)
print(pathImages) 

# Img Variables
imgNumber = 0
hs, ws = int(120 * 1), int(213 * 1)  # width and height of small image
gestureThreshold = 300

# Hand Detector
detectorHand = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success, img = cap.read()
    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

 # Find the hand and its landmarks
    hands, img = detectorHand.findHands(img, flipType=False)  # with draw
    # Draw Gesture Threshold line
    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0, 255, 0), 10)
#coditions for gestures
    if hands:
        hand = hands[0]
        fingers = detectorHand.fingersUp(hand)
        cx, cy = hand["center"]
        if cy <= gestureThreshold:
            if fingers == [1, 0, 0, 0, 0]:
                print("left")
                if imgNumber > 0:
                    imgNumber -= 1
            if fingers == [0, 0, 0, 0, 1]:
                if imgNumber < len (pathImages) -1:
                    imgNumber += 1
                print("right")
            
 #adding image to cam
    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = imgCurrent.shape
    imgCurrent[0:hs, w-ws:w]=imgSmall 
    cv2.imshow("Image", img)
    cv2.imshow("Presentation", imgCurrent)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

   