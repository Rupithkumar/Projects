import cv2 as cv
face_cascade=cv.CascadeClassifier('face detection.xml')
img=cv.imread("group2.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
face=face_cascade.detectMultiScale(gray,1.1,4)
for (x,y,w,h) in face:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
cv.imshow("output",img)
cv.waitKey(0)
cv.destroyAllWindows()