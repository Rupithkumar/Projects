import cv2 as cv
face_cascade=cv.CascadeClassifier('face detection.xml')
eye_cascade=cv.CascadeClassifier('eye detection.xml')
img=cv.imread("group1.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
face=face_cascade.detectMultiScale(gray,1.1,4)
for (x,y,w,h) in face:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 255), 5)
cv.imshow("output",img)
cv.waitKey(0)
cv.destroyAllWindows()