import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
success, frame1 = cap.read()
success, frame2 = cap.read()
while True:
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    dilated = cv.dilate(thresh, None, iterations=3)
    contour, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for contours in contour:
        (x,y,w,h)=cv.boundingRect(contours)
        if cv.contourArea(contours)<100000:
            cv.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
            cv.putText(frame1,"Status: {}".format("Movement"),(10,20),cv.FONT_ITALIC,1,(0,0,255),3)
    cv.imshow("video", frame1)
    frame1 = frame2
    success,frame2 = cap.read()
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
cap.release()
