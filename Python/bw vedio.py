import cv2 as cv
cap=cv.VideoCapture(0)
while True:
    success,frame=cap.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow("output",gray)
    if cv.waitKey(1) &0xff==ord('qp'):
        break
cap.release()
cv.destroyAllWindows()