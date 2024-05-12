import cv2 as cv
import datetime
cap=cv.VideoCapture(0)
cap.set(3,3000)
while True:
    success,frame=cap.read()
    date=str(datetime.datetime.now())
    font=cv.FONT_HERSHEY_DUPLEX
    frame=cv.putText(frame,date,(0,50),1,font,(0,255,255),4,cv.LINE_AA)
    cv.imshow("output",frame)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv.destroyAllWindows()