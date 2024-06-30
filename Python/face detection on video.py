import cv2 as cv
face_cascade=cv.CascadeClassifier('face detection.xml')
cap=cv.VideoCapture(0)
while cap.isOpened():
    _,img=cap.read()
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in face:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    cv.imshow("output",img)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv.destroyAllWindows()